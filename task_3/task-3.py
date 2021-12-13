# import required packages
import time
import schedule
from faker import Faker
from elasticsearch import Elasticsearch
from elasticsearch import helpers

# Settings for elasticsearch
host = "localhost"
port = 2049

# Settings for fake student data generation with Faker
fake = Faker() # create instance of Faker
filed_list = ['name','sex','blood_group','birthdate','mail','address'] # List of fileds data that will be generated.


def connect_elasticsearch(index_name):
    """ This method will try to establish connection with elasticserach installed locally and create provided index if doesn't exist """
    es = None
    es = Elasticsearch([{'host': host, 'port': port}])

    # Check whether connection is successful or not
    if es.ping():
        print('Connection with Elasticsearch is successful.')
    else:
        print('Failed to connect with Elasticserch.')
        return es
    
    # Create index in elastic search if doesn't exist
    if not es.indices.exists(index=index_name):
        print(f"Index '{index_name}' is creating.....")
        es.indices.create(index=index_name, ignore=400)
    else:
        print(f"Index '{index_name}' already in system.")
    
    return es

def fake_data_generator(num_students):  
    """ 
    This method will generate n number of students data
    parameters
    ----------------
    num_students: integer; take an integer number to generate fake student detail

    return: list
    ------------
    a list of dictionary contains the fake student detail.
    """
    
    fake_data = []
    for _ in range(num_students):
        student_detail = fake.profile(filed_list) # generate fake profile detail
        student_detail["contact"] = fake.phone_number() # add contact number in the profile detail
        fake_data.append(student_detail) # Add data to the list.
    
    return fake_data


def add_to_index(es_object, index_name, type_name):
    """ 
        This mehtod added the generated fake students data in the Elastic search with a index.

        parameters
        ----------
        index_name:: str; take a string which will be the index of the Elasticsearch.
    """
    # Generate 10 fake student details
    fake_data = fake_data_generator(10)

    # Creating data to add in the elastic search index.
    actions = []
    for fd in fake_data:
        actions.append({
            "_index": index_name,
            "_type": type_name,
            "_source": fd
        })
    
    # Bulk data insertion
    helpers.bulk(es_object, actions)

    print(f"::::::::::>>  Sucessfully data added to index:{index_name}, type:{type_name} of Elasticsearch.")


def data_adding_elasticsearch():
    """ This method will add data to elasticsearhc index if there is a successfull connection. """
    if es:
        # Add fake students data in Elasticsearch index.
        add_to_index(es, 'students', 'student detail')



# Establish connection with Elasticsearch installed locally.
es = connect_elasticsearch(index_name='students')

# initialize a job with scheduler
schedule.every(5).minutes.do(data_adding_elasticsearch)

# Start job
while True:
    # Run the pending schedule job if there is any.
    schedule.run_pending()
    time.sleep(1)

