import sys
import requests
import json
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from faker import Faker

fake = Faker()
scheduler = BlockingScheduler()

elastic_port = 2048



# Finding the age
def find_age(birth_year):
    
    age = datetime.now().year - birth_year
    return str(age)


global count
count = 0


def save_data():
    global count
    if count< 10:
        API_URL = 'http://127.0.0.1:{0}/students/_doc/'.format(elastic_port)
        headers = {'Content-type': 'application/json'}
        data_dict = {
            "name": fake.name(),
            "age": find_age(fake.date_of_birth().year),
            "gender": "Male",
            "contact": fake.email(),
            "address": fake.address()
           
        }

        data = json.dumps(data_dict)
        response = requests.post(API_URL, data=data, headers=headers)
        print(response.content)
        count +=1
    else:
        scheduler.remove_job('my_job_id')
        sys.exit()


def get_data():
    API_URL = 'http://127.0.0.1:{0}/students/_search/'.format(elastic_port)
    response = requests.get(API_URL)
    print(response.content)
    return response.content


def dump_data(content, file_name):
    fp = open(file_name, "w")
    json.dump(content, fp)
    fp.close()


def perform_schedule_task():
    scheduler.add_job(save_data, 'interval', hours=0, minutes=0, seconds=2, id='my_job_id')
    scheduler.start()


def main():
    perform_schedule_task()


if __name__ == '__main__':
    main()
