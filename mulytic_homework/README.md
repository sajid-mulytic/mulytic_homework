![Mulytic Labs GmbH](https://mulytic-web-content.s3.amazonaws.com/media/Mulytic/Photos/Logo/Color_logo_-_no_background.png)

# mulytic_homework 

This is a simple test for people who are interested in joining in the dynamic 
role of a Software Engineer at **[Mulytic Labs GmbH](https://mulyticlabs.io/)**.

You must write this code alone. But, don't worry, you are free to take help 
from online resources. Consider `Ubuntu` as your base OS as we are heavily 
dependent on this and this is our primary OS.

## Task 1
First, create a bash script that will install the latest version of `Docker`.
keep in mind, if there is any older version of docker is installed in the 
system, you have to remove it first.  
After installing `Docker`, the script will pull the images of `Elasticsearch` 
and `Kibana` (any version between 7.7 to 7.12). 

## Task 2
Now, create another bash script that will run `Elasticsearch` on **port 2048** 
and `Kibana` on **port 4096** in the background. You should be able to access 
Kibana at [http://localhost:4096](http://localhost:4096). 

## Task 3
Let's say, You need to FAKE some student details for some education purpose. 
But, you can not create more than 10 student on a five minutes window. You may 
wonder, "WHY"? Believe me, I don't know either. So, you are going to create a 
`python` script that will generate 10 FAKE student details i.e. name, age, 
gender, address, contact and so on for a student and store that to an **index**
naming `students` on the very same `Elasticsearch` you have launched in the 
first task. Please don't use the childish `time.sleep()` method in your script.
Instead, use some kind of scheduler, and you are free to choose any of your 
favourite one.

## Task 4
The last, but the most important task that makes you different from everyone 
else, the **DOCUMENTATION**. Prepare an awesome document describing the 
step-by-step solutions and procedure to execute them(in other words, the user 
guide!!) of the above-mentioned Tasks. 

>If you are confident enough that you are the right person for 
**[Mulytic Labs GmbH](https://mulyticlabs.io/)**, Please feel free to send us 
a **PR** with the solutions of the above-mentioned tasks. 