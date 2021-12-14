# Instuctions

Here is the instuctions to run all of the task


## Task - 1

The directory task_1 contain a bash file named as `task-1.sh` which automates the installation of **Docker** and pull the images of the **Elasticsearch** and **Kibana** of version `7.10.0`. You can change the version by editing the bash script.

### How to execute?

To run the bash script follow these steps
- Open the terminal
- Type the file path and press enter.

In terminal

    path/task-1.sh

It will ask for system password.

If it gives permission realted error try the following command to provide executable permissions to the file.

    chmod +x path/filename

    chmod +x ./task-1.sh

### What it does?

The bash script will first check whether the docker already installed or not. If already installed it will completely remove the installed docker and installed a fresh lates version of docker. If not installed then it will installed **docker** in the system.
After installation of **Docker** it will pull the image of the **Elasticsearch** and **Kibana** version `7.10.0`.

To change the version of the **Elasticsearch** and **Kibana** change on the end of these two lines: `7.10.0` with your version.

    sudo docker pull docker.elastic.co/elasticsearch/elasticsearch:7.10.0
    sudo docker pull docker.elastic.co/kibana/kibana:7.10.0


## Task - 2

The directory task_2 contain the bash script to automate the running of **Elasticsearch** (on port `2048`) and **Kibana** (on port `4096`). And provide the access through `http://localhost:2048` for **Elasticsearch** ; `http://localhost:4096` for **Kibana**.

### How to execute?

First make sure you create the network for Elastic search through the following command

    sudo docker network create elastic

To run the bash script follow these steps
- open the terminal
- type the file path and press enter.

    $./task-2.sh

#### To change the port of *Elasticserach*

Change the port number `2048` with your preferable one.

    sudo docker run --name es01-test --net elastic -p 127.0.0.1:2048:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.10.0

#### To change the port of *Kibana*

Change the port number `4096` with your preferable one.

    sudo docker run --name kib01-test --net elastic -p 127.0.0.1:4096:5601 -e "ELASTICSEARCH_HOSTS=http://es01-test:9200" docker.elastic.co/kibana/kibana:7.10.0

You may need to stop the running elastic search or running Kibana.

#### To stop

    sudo docker stop es01-test
    sudo docker stop kib01-test

#### To Remove

To remove created elastic network

    sudo docker network rm elastic

#### To remove

Elasticserach and kibana

    sudo docker rm es01-test
    sudo docker rm kib01-test



## Task - 3

The directory task_3 contain the python script which will geenrate 20 fake students detail in every 10 minutes and insert into the **Elasticsearch** with the index `students`.

### How to exucute?

*Create a virtual environment and install the following packages*

    faker
    elasticserach
    schedule

*Set the port and host of **elasticsearch** inside the script for successful connection with the elasticseach.*

*Run the script with python environment*

    python path/task-3.py

*You can change the number of fake students generation, fake student generation time interval, index name etc.*
