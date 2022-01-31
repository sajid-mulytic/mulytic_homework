# Documentation of Mulytic's Assesment

## In here, I described each tasks with their step-by-step solutions and procedure.
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#task_1">Task_1</a>
      <ul>
        <li><a href="Task_1_problem">Task_1_problem</a></li>
        <li><a href="Task_1_Solution">Task_1_Solution</a></li>
      </ul>
    </li>
    <li>
      <a href="#Task_2">Task_2</a>
      <ul>
        <li><a href="#Task_2_problem">Task_2_problem</a></li>
        <li><a href="#Task_2_Solution">Task_2_Solution</a></li>
      </ul>
    </li>
    <li><a href="#Task_3">Task_3</a></li>
    <li><a href="#Task_4">Task_4</a></li>

  </ol>
</details>


<!-- Task_1 -->
## Task_1

## Task_1_problem

First, create a bash script that will install the latest version of `Docker`.
keep in mind, if there is any older version of docker is installed in the 
system, you have to remove it first.  
After installing `Docker`, the script will pull the images of `Elasticsearch` 
and `Kibana` (any version between 7.7 to 7.12). 

## Task_1_Solution

As per instructions, I needed to remove the older version of docker first & then install the updated docker & pull the image of Elasticsearch` and `Kibana`.

### Here is the procedure

# 1. Removing the old version of docker

# 2. Updating the system

# 3. pull the images of elastic search and kibana




## Run/Exceute task_1 :

1. Open the terminal & go to the task_1 directory then run the " ./soultion_of_task_1.sh" command in terminal.

However, If there any "Permission denied" issues shows up, please allow to file executable mode by using

1. File executable : 
   chmod +x path/filename
   ex: chmod +x ./solution_of_task_1.sh

2. To check docker status 
    sudo systemctl status docker
    sudo systemctl status docker.service


<!-- Task_2 -->
## Task_2

## Task_2_problem

Now, create another bash script that will run `Elasticsearch` on **port 2048** 
and `Kibana` on **port 4096** in the background. You should be able to access 
Kibana at [http://localhost:4096](http://localhost:4096). 

## Task_2_Solution

1.  Change the Elasticsearch port to 2048 & run Elasticsearch
2.  Change the Kibana port to 4096 & run Kibana


## Run/Exceute task_2 :

1. Open the terminal & go to the task_2 directory then run the " ./soultion_of_task_2.sh" command in terminal.

## If there any "Permission denied" issues shows up, please allow to file executable mode by using

File executable: 

   chmod +x path/filename
   ex: chmod +x ./solution_of_task_1.sh

## If docker image conflit related issues shows up, remove the container by using below command
    sudo docker rm [containter id]
    ex: sudo docker rm 7c77bcc81880f3f72782a7f4520cf8786e34e93d65d555b619737b967e105c87


2. By http://localhost:2048 we can access elasticsearch.
3. By http://localhost:4096 we can access Kibana.


<!-- Task_3 -->
## Task_3

## Task_3_problem

Let's say, You need to FAKE some student details for some education purpose. 
But, you can not create more than 10 student on a five minutes window. You may 
wonder, "WHY"? Believe me, I don't know either. So, you are going to create a 
`python` script that will generate 10 FAKE student details i.e. name, age, 
gender, address, contact and so on for a student and store that to an **index**
naming `students` on the very same `Elasticsearch` you have launched in the 
first task. Please don't use the childish `time.sleep()` method in your script.
Instead, use some kind of scheduler, and you are free to choose any of your 
favourite one.

## Task_3_problem

We have used three python packages to automate this task.
1. requests: Sending HTTP request to the specified URL.
2. Faker: Generating fake student data.
3. apscheduler: For scheduling task.


Here we generated fake student data and convert it to JSON and make a HTTP POST request with this data to the elasticsearch students index. we have just save this data by using `apscheduler` to make a HTTP call after 2 seconds.



## Run/Exceute task_3 :

To install required libray & packages please run :


1. pip install requirements.txt 

Then run the python file by using bellow command on terminal:

2. python3 solution_of_task_3.py


<!-- Task_4 -->
## Task_4

As it was making a proper project documentation, I tried my best.