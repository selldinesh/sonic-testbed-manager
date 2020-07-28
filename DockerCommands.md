# Prerequisites 
* An Ubuntu Linux box
* The sonic docker image in your home directory. 
  * Pre-built sonic-mgmt can also be downloaded from [here](https://sonic-jenkins.westus2.cloudapp.azure.com/job/bldenv/job/docker-sonic-mgmt/lastSuccessfulBuild/artifact/sonic-buildimage/target/docker-sonic-mgmt.gz)
* Basic knowledge of docker commands.
* Docker-tools should be there installed in your system.
# sonic-mgmt docker environment preparation: useful commands (for Ubuntu system)
**Installing docker**<br>
``sudo apt-get update``<br>
``sudo apt-get remove docker docker-engine docker.io``<br>
``sudo apt install docker.io``<br>
``sudo systemctl start docker``<br>
``sudo systemctl enable docker``<br><br>
**Unzip sonic Image**<br>
``gzip -d docker-sonic-mgmt.gz``<br><br>
**Load the docker Image**<br>
``sudo docker images``<br>
``sudo docker load -i docker-sonic-mgmt``<br>
``sudo docker run -it --name sonic docker-sonic-mgmt``<br><br>
**Stopping a docer session**<br>
``sudo docker stop sonic``<br><br>
**Reconnect to a stopped docer session**<br>
``sudo docker start -i sonic``<br><br>
**When you are done you may remove the image sonic**<br>
``sudo docker rm sonic``<br><br>
**Remove docker by image Id**<br>
``sudo docker rmi -f <image-id>``<br><br>
**Running a sonic docker with local directoy mounted in it.**<br>
``sudo docker run -it --name sonic --privileged -v /home/ubuntu/adhar/:/var/johnar/adhar --workdir /var/johnar/adhar --user johnar:gjohnar docker-sonic-mgmt``<br><br>

