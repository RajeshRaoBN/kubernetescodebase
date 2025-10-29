from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
import json
import random


# Extract function
def extract_data():
    data = [{"id": i, "value": random.randint(1, 100)} for i in range(10)]
    return data


# Transform functions
def filter_data(ti):
    data = ti.xcom_pull(task_ids="extract.extract_task")
    filtered = [d for d in data if d["value"] > 50]
    return filtered


def normalize_data(ti):
    data = ti.xcom_pull(task_ids="transform.filter_task")
    normalized = [{"id": d["id"], "value": d["value"] / 100} for d in data]
    return normalized


# Load function
def save_data(ti):
    data = ti.xcom_pull(task_ids="transform.normalize_task")
    with open("/tmp/final_data.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Data saved to /tmp/final_data.json")


default_args = {"retries": 2, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="production_etl",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    # Extract group
    with TaskGroup("extract") as extract_group:
        extract_task = PythonOperator(
            task_id="extract_task", python_callable=extract_data
        )

    # Transform group
    with TaskGroup("transform") as transform_group:
        filter_task = PythonOperator(task_id="filter_task", python_callable=filter_data)

        normalize_task = PythonOperator(
            task_id="normalize_task", python_callable=normalize_data
        )

        filter_task >> normalize_task

    # Load group
    with TaskGroup("load") as load_group:
        save_task = PythonOperator(task_id="save_task", python_callable=save_data)

        cleanup_task = BashOperator(
            task_id="cleanup_task", bash_command="echo 'Cleaning up temporary files...'"
        )

        save_task >> cleanup_task

    extract_group >> transform_group >> load_group
