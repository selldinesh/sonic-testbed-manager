# SONiC testbed management infrastructure
* The SONiC testbed consists of multiple interrelated configuration files that are difficult and error-prone edit manually.
* They are not frequently modified and only handful of persons like owners/admin has authority to modify them. But creating the initial setup or retrieving a broken setup is more challenging task for them.
* User scripts runs inside the docker container loads and access these files, and if the container is corrupted or crashed these files will be lost and will be difficult to get back easily. This will be challenging time for the user who doesn’t have the knowledge of interrelationship of the files.
# So how do we onboard engineer to write tests?
* Keep the testbed files in the separate repository outside the SONiC docker image.
* Provision the engineers to keep the code in their local machine and mount them in the while loading the docker container. So, code will be in the local directory and won’t get lost if the container is wrecked.
* Give the engineer a script to build the testbed from the stored files in the repository.
# Workflow
* Sync the sonic-mgmt in the local directory.
  * git clone https://github.com/abhijit-dhar/sonic-mgmt
* load the docker image such that it mounts sonic-mgmt inside the container.
  * sudo docker run -it --name sonic --privileged -v /home/ubuntu/sonic-mgmt/:/var/johnar/sonic-mgmt  --user johnar:gjohnar docker-sonic-mgmt
* Inside the container clone sonic-testbed-manager.
  * git clone https://github.com/abhijit-dhar/sonic-testbed-manager
* Run the script dev-env.sh form the directory /var/johnar/sonic-testbed-manager/ixia-calbases-lab
  * cd /var/johnar/sonic-testbed-manager/ixia-calbases-lab
  * sh ./dev-env.sh




