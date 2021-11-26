#! /bin/bash


echo "# This Script will remove any docker component and install latest stable docker  #"
echo "Removing docker if any . . ."

apt remove docker docker-engine docker.io containerd runc -y 2>/dev/null
apt update -y
systemctl stop docker.socket
sleep 1

apt-get purge docker-ce docker-ce-cli containerd.io -y 
rm -rf /var/lib/docker
rm -rf /var/lib/containerd


echo "==> Installing dependencies"

apt install apt-transport-https ca-certificates curl software-properties-common -y

echo " Adding the GPG key for official Docker Repo "
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

echo " Adding the Docker Repo to apt source"
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" -y

echo "Updating package database"
apt update -y

echo "Installing Docker"
apt-cache policy docker-ce | head -5

echo "==> Now installing docker....." 
apt install docker-ce -y

if [[ $? -ne 0 ]]
then
	echo "Failed"
	exit 2
fi
echo "Docker installation successful - $(hostname -s)"
if systemctl status docker &>/dev/null 
then
	echo "it is up and running. You can verify it using cmd: systemctl status docker"
else
	echo "=it is not running. You can start it manually using cmd: systemctl start docker"
fi
<< comment
echo "#############################################"
echo "# Now, You can play with docker  ############"
echo "# Docker Info on $(hostname -s) is: #########"
echo "#############################################"
comment
echo "###################################################################################"
echo "# Now it will pull elasticsearch and kibana docker images 7.7.0 respectively #"
echo "###################################################################################"
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.7.0
docker pull docker.elastic.co/kibana/kibana:7.7.0
echo "Done"
