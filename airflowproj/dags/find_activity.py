from airflow.decorators import dag
from pendulum import datetime
import requests

@dag(
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    tags=["activity"],
    catchup=False,
)

def find_activity():
    @task
    def get_activity():
        r = requests.get(API, timeout=10)
        return r.json()
    
    @task
    def write_activity_to_file(response):
    
    get_activity()
    
find_activity()