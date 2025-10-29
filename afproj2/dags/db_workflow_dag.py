from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres_operator import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime


# Python function to insert data dynamically
def insert_dynamic_data():
    hook = PostgresHook(postgres_conn_id="postgres_demo")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO my_table (name, created_at) VALUES (%s, %s)",
        ("Airflow", datetime.now()),
    )
    conn.commit()
    cursor.close()
    conn.close()


# Python function to read and print data
def read_data():
    hook = PostgresHook(postgres_conn_id="postgres_demo")
    records = hook.get_records("SELECT * FROM my_table")
    for row in records:
        print(row)


with DAG(
    dag_id="db_workflow_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    # Task 1: Create table (if not exists)
    create_table = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres_demo",
        sql="""
        CREATE TABLE IF NOT EXISTS my_table (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL
        );
        """,
    )

    # Task 2: Insert data (static query)
    insert_static = PostgresOperator(
        task_id="insert_static",
        postgres_conn_id="postgres_demo",
        sql="INSERT INTO my_table (name, created_at) VALUES ('StaticData', NOW());",
    )

    # Task 3: Insert dynamic data (via Python)
    insert_dynamic = PythonOperator(
        task_id="insert_dynamic", python_callable=insert_dynamic_data
    )

    # Task 4: Read data from DB
    read_db = PythonOperator(task_id="read_db", python_callable=read_data)

    create_table >> insert_static >> insert_dynamic >> read_db
