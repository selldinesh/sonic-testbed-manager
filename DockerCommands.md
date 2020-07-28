# Prerequisites 
* An Ubuntu Linux box
* The sonic docker image in your home directory. 
  * Pre-built sonic-mgmt can also be downloaded from [here](https://sonic-jenkins.westus2.cloudapp.azure.com/job/bldenv/job/docker-sonic-mgmt/lastSuccessfulBuild/artifact/sonic-buildimage/target/docker-sonic-mgmt.gz)
* Basic knowledge of docker commands.
* Docker-tools should be there installed in your system.
# sonic-mgmt docker environment preparation: useful commands (for Ubuntu system)
#### Installing docker
``sudo apt-get update``<br>
``sudo apt-get remove docker docker-engine docker.io``<br>
``sudo apt install docker.io``<br>
``sudo systemctl start docker``<br>
``sudo systemctl enable docker``<br>
#### Unzip sonic Image
``gzip -d docker-sonic-mgmt.gz``
#### Load the docker Image
``sudo docker images``

``sudo docker load -i docker-sonic-mgmt``

``sudo docker run -it --name sonic docker-sonic-mgmt``

#### Stopping a docer session
``sudo docker stop sonic``
#### Reconnect to a stopped docer session
``sudo docker start -i sonic``
#### When you are done you may remove the image sonic
``sudo docker rm sonic``
#### Remove docker by image Id
``sudo docker rmi -f <image-id>``
#### Running a sonic docker with local directoy mounted in it.
``sudo docker run -it --name sonic --privileged -v /home/ubuntu/adhar/:/var/johnar/adhar --workdir /var/johnar/adhar --user johnar:gjohnar docker-sonic-mgmt``

