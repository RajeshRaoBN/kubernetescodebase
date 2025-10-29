from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import random


# Branching logic
def decide_path():
    if datetime.now().weekday() >= 5:
        return "weekend_task"
    else:
        return "weekday_task"


# Branching logic 2
def decide_path2():
    if generate_numbers() >= 50:
        return "big_number_task"
    else:
        return "small_number_task"


# Dynamic task function
def process_number(num):
    print(f"Processing number: {num}")

BashOperator(
    task_id="unstable_task",
    bash_command="exit 1",  # Simulates failure
    retries=3,
    retry_delay=timedelta(minutes=2),
)


with DAG(
    dag_id="branching_dynamic_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    # Branching task
    branch_task = BranchPythonOperator(
        task_id="branch_task", python_callable=decide_path
    )

    # Branching task no. 2
    branch_task2 = BranchPythonOperator(
        task_id="branch_task2", python_callable=decide_path2
    )

    weekend_task = BashOperator(
        task_id="weekend_task", bash_command="echo 'It’s weekend! 🎉 Take a break.'"
    )

    weekday_task = BashOperator(
        task_id="weekday_task", bash_command="echo 'It’s a weekday! Time to work.'"
    )
    
    branch_task >> [weekend_task, weekday_task]

    big_number_task = BashOperator(
        task_id="big_number_task", bash_command="echo 'It’s a very very big number.'"
    )

    small_number_task = BashOperator(
        task_id="small_number_task", bash_command="echo 'It’s a small number!'"
    )
    
    branch_task2 >> [big_number_task, small_number_task]

    # Dynamic Task Mapping — process random numbers
    from airflow.decorators import task

    @task
    def generate_numbers():
        return [random.randint(1, 100) for _ in range(5)]

    @task
    def process(num):
        print(f"Processing number: {num}")

    nums = generate_numbers()
    processed = process.expand(num=nums)

    branch_task >> branch_task2 >> nums >> processed  
