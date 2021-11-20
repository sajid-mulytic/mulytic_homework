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
    API_URL = 'http://127.0.0.1:{0}/students/_search/'.format(ES_PORT)
    response = requests.get(API_URL)
    print(response.content)
    # dump_data(response.content.decode("UTF-8"), 'data.txt')
    return response.content


def dump_data(content, file_name):
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
