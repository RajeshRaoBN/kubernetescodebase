from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


# Task 1: Python function to create a message
def create_message():
    message = (
        f"Hello from Airflow! Today's date is {datetime.now().strftime('%Y-%m-%d')}"
    )
    return message  # Returning pushes data to XCom automatically


# Task 2: Python function to receive the message
def print_message(ti):
    msg = ti.xcom_pull(task_ids="create_message_task")
    print(f"Received message: {msg}")


# Task 5: Python function to print completion
def print_completion():
    current_file = "~/airflow/dags/output.txt"
    fil = open(current_file, 'r')
    file_contents = fil.read()
    print(file_contents)
    fil.close()


# Define the DAG
with DAG(
    dag_id="multi_task_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@hourly",
    catchup=False,
) as dag:

    # Task 1 - Create a message
    create_message_task = PythonOperator(
        task_id="create_message_task", python_callable=create_message
    )

    # Task 2 - Print the message
    print_message_task = PythonOperator(
        task_id="print_message_task", python_callable=print_message
    )

    # Task 3 - Run a bash command
    bash_task1 = BashOperator(
        task_id="bash_task1", bash_command="echo 'Running shell command...' && date"
    )

    # Task 4 - Run second bash command
    bash_task2 = BashOperator(
        task_id="bash_task2", bash_command="echo 'Airflow rocks!' > ~/airflow/dags/output.txt"
    )

    # Task 5 - Print the completion
    print_completion_task = PythonOperator(
        task_id="print_completion_task", python_callable=print_completion
    )

    # Set dependencies: Task1 → Task2 → Task3
    create_message_task >> print_message_task >> bash_task1 >> bash_task2 >> print_completion_task
