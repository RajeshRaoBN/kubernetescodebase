from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.hooks.http import HttpHook
from datetime import datetime
import json


# Step 2: Extract function
def extract_data():
    http_hook = HttpHook(http_conn_id="http_demo_api", method="GET")
    response = http_hook.run(endpoint="/posts")
    data = response.json()
    return data[:5]  # Return first 5 records for demo


# Step 3: Transform function
def transform_data(ti):
    records = ti.xcom_pull(task_ids="extract_task")
    transformed = [{"title": rec["title"], "userId": rec["userId"]} for rec in records]
    return transformed


# Step 4: Load function
def load_data(ti):
    transformed = ti.xcom_pull(task_ids="transform_task")
    with open("/tmp/etl_output.json", "w") as f:
        json.dump(transformed, f, indent=2)
    print("Data saved to /tmp/etl_output.json")


with DAG(
    dag_id="etl_api_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    # Step 1: Wait for API
    wait_for_api = HttpSensor(
        task_id="wait_for_api",
        http_conn_id="http_demo_api",
        endpoint="/posts",
        poke_interval=10,
        timeout=60,
    )

    extract_task = PythonOperator(task_id="extract_task", python_callable=extract_data)

    transform_task = PythonOperator(
        task_id="transform_task", python_callable=transform_data
    )

    load_task = PythonOperator(task_id="load_task", python_callable=load_data)

    wait_for_api >> extract_task >> transform_task >> load_task
