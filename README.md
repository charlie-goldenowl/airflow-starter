### start server (terminal1)
```shell
airflow webserver
```
### start scheduler (terminal2)
```shell
airflow scheduler
```

### set AIRFLOW_HOME
```shell
export AIRFLOW_HOME=/Users/vuong/labs/pythonProject/airflow_demo
```

### create new dag
```shell
touch dags/hello_world_dag.py
```
example
```python
#datetime
from datetime import timedelta, datetime

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
		tags=['example, helloworld']
)

# python callable function
def print_hello():
		return 'Hello World!'

# Creating first task
start_task = EmptyOperator(task_id='start_task', dag=hello_world_dag)

# Creating second task
hello_world_task = PythonOperator(task_id='hello_world_task', python_callable=print_hello, dag=hello_world_dag)

# Creating third task
end_task = EmptyOperator(task_id='end_task', dag=hello_world_dag)

# Set the order of execution of tasks.
start_task >> hello_world_task >> end_task
```

### show all dags
```shell
airflow dags list
```


### create default user:
```shell
airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
```