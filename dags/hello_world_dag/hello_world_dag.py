# datetime
from datetime import timedelta, datetime
import random

# The DAG object
from airflow import DAG

# Operators
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

# initializing the default arguments
default_args = {
    'owner': 'Ranga',
    'start_date': datetime(2022, 3, 4),
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

# Instantiate a DAG object
hello_world_dag = DAG('hello_world_dag',
                      default_args=default_args,
                      description='Hello World DAG',
                      schedule='* * * * *',
                      catchup=False,
                      tags=['example', 'helloworld']
                      )


# python callable function
def print_hello():
    if random.random() < 0.5:
        raise Exception('Task failed randomly')
    return 'Hello World!'


# Creating first task
start_task = EmptyOperator(task_id='start_task', dag=hello_world_dag)

# Creating second task
hello_world_task = PythonOperator(task_id='hello_world_task', python_callable=print_hello, dag=hello_world_dag)

# Creating third task
end_task = EmptyOperator(task_id='end_task', dag=hello_world_dag)

# Set the order of execution of tasks.
start_task >> hello_world_task >> end_task
