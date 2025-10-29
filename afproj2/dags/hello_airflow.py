from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def greet():
    print("Hello from Airflow!")


def complete():
    print("Lesson 1 completed!")


with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2025, 1, 1),
    schedule="*/5 * * * *",
    catchup=False,
) as dag:
    task1 = PythonOperator(task_id="greet_task", python_callable=greet),
    task2 = PythonOperator(task_id="complete_task", python_callable=complete)
