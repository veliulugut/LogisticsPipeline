from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import json
from kafka import KafkaProducer

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 12, 25),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

def get_kafka_producer():
    return KafkaProducer(
        bootstrap_servers=['kafka:29092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )

def generate_and_send_customer():
    try:
        response = requests.get('http://logistics-api:8088/generate_data')
        if response.status_code == 200:
            data = response.json()
            producer = get_kafka_producer()
            producer.send('logistics_topic', value=data)
            producer.flush()
            print(f"Generated and sent data: {data}")
        else:
            print(f"Error generating data: {response.status_code}")
    except Exception as e:
        print(f"Error: {str(e)}")

dag = DAG(
    'logistics_data_generator',
    default_args=default_args,
    description='Generate logistics data and send to Kafka every 2 minutes',
    schedule_interval=timedelta(minutes=2),
    catchup=False
)

generate_task = PythonOperator(
    task_id='generate_and_send_data',
    python_callable=generate_and_send_customer,
    dag=dag
)
