import uuid
import json
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from kafka import KafkaProducer
import logging


from cassandra.cluster import Cluster
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType

default_args = {
    'owner': 'zahra',
    'start_date': datetime(2024, 8, 10, 10, 00)
}

def get_data():
    """Fetch random user data from API."""
    import requests
    res = requests.get("https://randomuser.me/api/")
    res = res.json()['results'][0]
    return res  # Directly return the fetched data

def format_data(res):
    """Format the fetched data."""
    data = {}
    location = res['location']
    data['id'] = str(uuid.uuid4())  # Convert to string for JSON compatibility
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data  # Return formatted data to be passed to the next task

def stream_data(formatted_data):
    """Stream the formatted data to Kafka."""
    # producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    # topic_name = 'users_created'
    
    # # Log the data being streamed
    # logging.info(f"Streaming data to Kafka: {formatted_data}")
    
    # # Send the data to Kafka
    # producer.send(topic_name, json.dumps(formatted_data).encode('utf-8'))
    import json
    from kafka import KafkaProducer
    import time
    import logging

    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 20: #20 seconds
            break
        try:
            res = get_data()
            res = format_data(res)

            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue


# Define the DAG
with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    # Task 1: Get data from the API
    get_data_task = PythonOperator(
        task_id='get_data_task',
        python_callable=get_data
    )

    # Task 2: Format the fetched data
    format_data_task = PythonOperator(
        task_id='format_data_task',
        python_callable=format_data,
        op_args=[get_data_task.output],  # Pass the output of get_data_task as input
    )

    # Task 3: Stream the formatted data to Kafka
    stream_data_task = PythonOperator(
        task_id='stream_data_task',
        python_callable=stream_data,
        op_args=[format_data_task.output],  # Pass the output of format_data_task as input
    )

    # Task dependencies
    get_data_task >> format_data_task >> stream_data_task