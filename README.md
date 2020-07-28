# Prerequsits 
* An Ubuntu linux box
* download the sonic docker image and save it in your home directory. 
* Pre-built sonic-mgmt can also be downloaded from [here](https://sonic-jenkins.westus2.cloudapp.azure.com/job/bldenv/job/docker-sonic-mgmt/lastSuccessfulBuild/artifact/sonic-buildimage/target/docker-sonic-mgmt.gz)

# sonic-mgmt docker environment preparation: useful commands
### Installing docker
* sudo apt-get update
* sudo apt-get remove docker docker-engine docker.io
* sudo apt install docker.io
* sudo systemctl start docker
* sudo systemctl enable docker
### Unzip sonic Image
* gzip -d docker-sonic-mgmt.gz
### Load the docker Image
* sudo docker images
* sudo docker load -i docker-sonic-mgmt
* sudo docker run -it --name sonic docker-sonic-mgmt
### stopping a docer session
* sudo docker stop sonic
### reconnect to a stopped docer session
* sudo docker start -i sonic
### When you are done you may remove the image sonic
* sudo docker rm sonic
### remove docker by image Id
* sudo docker rmi -f <image-id>
### Running a sonic docker with local directoy mounted in it.
* sudo docker run -it --name sonic --privileged -v /home/ubuntu/adhar/:/var/johnar/adhar --workdir /var/johnar/adhar --user johnar:gjohnar docker-sonic-mgmt

# SONiC testbed management infrastructure
* The SONiC testbed consists of multiple interrelated configuration files that are difficult and error-prone edit manually.
* They are not frequently modified and only handful of persons like owners/admin has authority to modify them. But creating the initial setup or retrieving a broken setup is more challenging task for them.
* User scripts runs inside the docker container loads and access these files, and if the container is corrupted or crashed these files will be lost and will be difficult to get back easily. This will be challenging time for the user who doesn’t have the knowledge of interrelationship of the files.
# So how do we onboard engineer to write tests?
* Keep the testbed files in the separate repository outside the SONiC docker image.
* Provision the engineers to keep the code in their local machine and mount them while loading the docker container. So, code will be in the local directory and won’t get lost if the container is wrecked.
* Give the engineer a script to build the testbed from the stored files in the repository.
# Workflows
### workflow1
* Sync the sonic-mgmt in the local directory.
  * git clone https://github.com/abhijit-dhar/sonic-mgmt
* load the docker image such that it mounts sonic-mgmt inside the container.
  * sudo docker run -it --name sonic --privileged -v /home/ubuntu/sonic-mgmt/:/var/johnar/sonic-mgmt  --user johnar:gjohnar docker-sonic-mgmt
* Inside the container clone sonic-testbed-manager.
  * git clone https://github.com/abhijit-dhar/sonic-testbed-manager
* Run the script dev-env.sh form the directory /var/johnar/sonic-testbed-manager/ixia-calbases-lab
  * cd /var/johnar/sonic-testbed-manager/ixia-calbases-lab
  * sh ./dev-env.sh
* Run the test
  * cd ~/sonic-mgmt/tests/
  * py.test --inventory ../ansible/ixia-sonic --host-pattern sonic-s6100-dut --module-path ../ansible/library/ --testbed vms-ixia-sonic --testbed_file ../ansible/testbed.csv --show-capture=stdout --log-cli-level  info  --showlocals -ra --allow_recover --skip_sanity --disable_loganalyzer ixia/test_ixia_traffic_restpy.py
 * In this workflow your test script or code will remain intact even if docker image is destroyed unintentionally since you are actually keeping the code in the (mounted) local directory.
### workflow2
* Simply load the docker image no mounts of local folders are required.
  * sudo docker run -it --name sonic docker-sonic-mgmt
* Inside the container clone the sonic-mgmt.
  * git clone https://github.com/abhijit-dhar/sonic-mgmt
* Inside the container clone sonic-testbed-manager.
  * git clone https://github.com/abhijit-dhar/sonic-testbed-manager
* Run the script dev-env.sh form the directory /var/johnar/sonic-testbed-manager/ixia-calbases-lab
  * cd /var/johnar/sonic-testbed-manager/ixia-calbases-lab
  * sh ./dev-env.sh
* Run the test
  * cd ~/sonic-mgmt/tests/
  * py.test --inventory ../ansible/ixia-sonic --host-pattern sonic-s6100-dut --module-path ../ansible/library/ --testbed vms-ixia-sonic --testbed_file ../ansible/testbed.csv --show-capture=stdout --log-cli-level  info  --showlocals -ra --allow_recover --skip_sanity --disable_loganalyzer ixia/test_ixia_traffic_restpy.py
* In this workflow if you make certain local change inside the folder ~/sonic-mgmt/ that will not be saved if the container got corrupted somehow.
