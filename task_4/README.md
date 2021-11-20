

# DOCUMENTATION

Let's describing the step-by-step solutions and procedure for each task 🎉

## Task 1
`solution_1.sh`
```bash
install_docker() {
    echo "Let's install latest version of docker!"
    # First, update your existing list of packages
    sudo apt update

    # Next, install a few prerequisite packages
    sudo apt install apt-transport-https ca-certificates curl software-properties-common

    # Then add the GPG key for the official Docker repository to your system
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    # Add the Docker repository to APT sources
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

    # Next, update the package database with the Docker packages from the newly added repo
    sudo apt update

    # Make sure you are about to install from the Docker repo instead of the default Ubuntu repo
    apt-cache policy docker-ce

    # Finally, Lets install Docker :)
    sudo apt install docker-ce

    # Docker should now be installed, Let's check docker status :)
    sudo systemctl status docker
    sudo systemctl status docker.service
    lets_do_some_fun

}

lets_do_some_fun() {
    sudo apt install sl
    sl
}

remove_docker() {
    # To identify what installed package actually I have
    dpkg -l | grep -i docker

    sudo apt-get purge -y docker-engine docker docker.io docker-ce docker-ce-cli
    sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce

    sudo rm -rf /var/lib/docker /etc/docker
    sudo rm /etc/apparmor.d/docker
    sudo groupdel docker
    sudo rm -rf /var/run/docker.sock

    echo "Docker is now completely uninstalled :("
}


check_is_outdated() {
    pat="^$1/"
    if [ -z "$(apt list --upgradable | grep -e $pat)" ]; then
        lets_do_some_fun
        echo "You have latest version of $1 :)"

    else
        echo "Lets uninstall old version of docker first"
        remove_docker
        echo "Lets install latest version of docker :)"
        install_docker

    fi
}

pull_elasticsearch() {
    sudo docker network create elastic
    sudo docker pull docker.elastic.co/elasticsearch/elasticsearch:7.12.1

}

pull_kibana() {
    sudo docker pull docker.elastic.co/kibana/kibana:7.12.1

}


check_is_outdated docker
pull_elasticsearch
pull_kibana
```
 <p> 💬 The following script contains six functions.let's discuss 💭 </p>
<ol>
    <li>check_is_outdated</li>
    <li>install_docker</li>
    <li>remove_docker</li>
    <li>lets_do_some_fun</li>
    <li>pull_elasticsearch</li>
    <li>pull_kibana</li>
</ol>

* `check_is_outdated` takes only one parameter(package) and perform the operations like that param package is outdated or installed in your machine or not. If the following package is outdated then it calls a function named `remove_docker`. It will remove docker from your machine.After removing old version of docker then it will call another function named `install_docker` to install new version of docker.If the new version of docker is installed in your machine then it will call a funny function named  `lets_do_some_fun`. It will just display a funny screen in your terminal 😄.

* After installing docker we have another 2 functions names `pull_elasticsearch` and `pull_kibana`. Both of two functions will pull Elasticsearch and Kibana as a docker images.
## Task 2
Now, We have another bash script named `solution_2.sh` that will run `Elasticsearch` on **port 2048** 
and `Kibana` on **port 4096** in the background.So You can access 
Elasticsearch at [http://localhost:2048](http://localhost:2048). 
Kibana at [http://localhost:4096](http://localhost:4096). 
```bash
start_elk() {
    sudo docker rm es
    sudo docker run --name es -d -p 127.0.0.1:2048:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.12.1
  
    # To get es container ip for kibana as though it is dynamic
    es_ip=$(sudo docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' es)
  
    sudo docker rm kibana
    sudo docker run --name kibana -d -p 127.0.0.1:4096:5601 -e "ELASTICSEARCH_HOSTS=http://$es_ip:9200" docker.elastic.co/kibana/kibana:7.12.1

}

start_elk
```

## Task 3
`solution_3.py`
```python
import sys
import requests
import json
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from faker import Faker

fake = Faker()
scheduler = BlockingScheduler()

ES_PORT = 2048


def get_age(birth_year):
    # calculate total age from birth year
    age_in_years = datetime.now().year - birth_year
    return str(age_in_years)


global counter
counter = 0


def save_data():
    # It will save fake student data to specific elasticsearch index
    global counter
    if counter < 10:
        API_URL = 'http://127.0.0.1:{0}/students/_doc/'.format(ES_PORT)
        headers = {'Content-type': 'application/json'}
        data_dict = {
            "name": fake.name(),
            "age": get_age(fake.date_of_birth().year),
            "gender": "Male",
            "address": fake.address(),
            "contact": fake.email()
        }

        data = json.dumps(data_dict)
        response = requests.post(API_URL, data=data, headers=headers)
        print(response.content)
        counter +=1
    else:
        scheduler.remove_job('my_job_id')
        print('Yes!!! My job is done :) ')
        sys.exit()


def get_data():
    # To check elasticsearch index data
    API_URL = 'http://127.0.0.1:{0}/students/_search/'.format(ES_PORT)
    response = requests.get(API_URL)
    print(response.content)
    # dump_data(response.content.decode("UTF-8"), 'data.txt')
    return response.content


def dump_data(content, file_name):
    # If required to save data in a file 
    fp = open(file_name, "w")
    json.dump(content, fp)
    fp.close()


def perform_schedule_task():
    # Schedule job_function to be called every ....
    scheduler.add_job(save_data, 'interval', hours=0, minutes=0, seconds=2, id='my_job_id')
    scheduler.start()


def main():
    # get_data()
    perform_schedule_task()


if __name__ == '__main__':
    main()

```
Here I have used three python packages for automate this task.
I have used `Faker` for generating fake student data.
`apscheduler` for scheduling task. I had a plan to use celery for scheduler but it will be overwhelming for this simple task.
I have used `requests` for HTTP request to the specified URL.
I have just generate fake student data and convert it to JSON and make a HTTP POST request with this data to the elasticsearch students index. I have just save this data by using `apscheduler` to make a HTTP call after 2 seconds.

## Task 4
I have tried my level best to solve this tasks with documentation.
Hope you will enjoy my code :)