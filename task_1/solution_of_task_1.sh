### Uninstall Docker Engine

# 1. Uninstall the Docker Engine, CLI, and Containerd packages:
sudo apt-get purge docker-ce docker-ce-cli containerd.io
sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce

# 2. Images, containers, volumes, or customized configuration files on your host are not automatically removed. To delete all images, containers, and volumes:

 sudo rm -rf /var/lib/docker

 sudo rm -rf /var/lib/containerd
 
## Package update

# Update the apt package index and install packages to allow apt to use a repository over HTTPS:

 sudo apt-get update

 sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker’s official GPG key:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg    


# set up the stable repository. To add the nightly or test repository, add the word nightly or test (or both) after the word stable
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update the apt package index, and install the latest version of Docker Engine and containerd,
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# pull the images of elastic search and kibana

sudo docker pull docker.elastic.co/elasticsearch/elasticsearch:7.10.0
sudo docker pull docker.elastic.co/kibana/kibana:7.10.0