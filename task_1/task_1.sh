if [[ $(which docker) && $(docker --version) ]]; then
    echo "Update docker"
    # To completely uninstall Docker:
    # Step 1

    apt-get purge -y docker-engine docker docker.io docker-ce docker-ce-cli
    sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce  
    #The above commands will not remove images, containers, volumes, or user created configuration files on your host. If you wish to delete all images, containers, and volumes run the following commands:
    sudo rm -rf /var/lib/docker /etc/docker
    sudo rm /etc/apparmor.d/docker
    sudo groupdel docker
    sudo rm -rf /var/run/docker.sock
    #You have removed Docker from the system completely.
  else
    echo "Install docker"
    # command
fi


# update system
sudo apt-get update

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker’s official GPG key:
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Use the following command to set up the stable repository. To add the nightly or test repository, add the word nightly or test (or both) after the word stable in the commands below. Learn about nightly and test channels.
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# install docker 
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# pull the images of elastic search and kibana
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.7.0
docker pull docker.elastic.co/kibana/kibana:7.7.0