from elasticsearch import Elasticsearch
import random
import schedule
import time


#   Random Student Data

NAME_FIRSTNAME_MALE = [
    'Jayeed',
    'Tawsif',
    'Sadat',
    'Pavel',
    'Noel',
    'Juel',
    'Sid',
    'John',
    'James',
    'Arefin',
    'Joseph',
    'Robert',
    'William',
    'Thomas',
    'Christopher']

NAME_FIRSTNAME_FEMALE = [
    'Mary',
    'Patricia',
    'Jennifer',
    'Linda',
    'Elizabeth',
    'Barbara',
    'Susan',
    'Jessica',
    'Sarah',
    'Karen',
    'Nancy',
    'Lisa',
    'Betty']

NAME_LASTNAME = [
    'Dickson',
    'Harry',
    'Mohammad',
    'Baratheon',
    'Drogo',
    'Ferrera',
    'Kissinger',
    'Bond',
    'Holland']

GENDER = ['Male', 'Female']

ADDRESS = [
    'Dhaka',
    'Comilla',
    'Pabna',
    'Rajshahi',
    'Chittagong',
    'Bogura',
    'Rangpur',
    'Dinajpur',
    'Noakhali',
    'Barisal',
    'Begumganj',
    'Germany',
    'US',
    'Canada']

CONTACT = [
    '0167xxx',
    '01920xxx',
    '01310xxx',
    '0171yyy',
    '01820xxx',
    '01552zzz']

DOC_TYPE = 'student_info'

gen = (x for x in range(1, 200))


#  Creating connection with elastic search at PORT 2048

client = Elasticsearch("http://localhost:2048")
client.indices.create(index='students')


# Specify n according to need. By default, n is 10 which will produce a
# timeframe of 10 minutes as the runtime of this script

n = 10
loop_end_time = n * 60
execution_time = time.time()


def create_random_student():

    gender = random.choice(GENDER)
    if gender == 'Female':
        f_name = random.choice(NAME_FIRSTNAME_FEMALE)
    else:
        f_name = random.choice(NAME_FIRSTNAME_MALE)

    fullName = f_name + ' ' + random.choice(NAME_LASTNAME)
    age = random.choice(range(18, 35))
    address = random.choice(ADDRESS)
    contact = random.choice(CONTACT)
    studentx = {

        'name': fullName,
        'age': age,
        'gender': gender,
        'address': address,
        'contact': contact

    }

    client.index(
        index='students',
        doc_type=DOC_TYPE,
        id=next(gen),
        body=studentx)


def execute_once():

    create_random_student()
    return schedule.CancelJob


schedule.every(2).seconds.do(execute_once)
schedule.every(32).seconds.do(create_random_student)

while True:

    schedule.run_pending()

    time_difference = time.time() - execution_time
    if time_difference >= loop_end_time:
        break
