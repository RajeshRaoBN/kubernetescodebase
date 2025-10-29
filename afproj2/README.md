brew install pyenv

pyenv install 3.11.9
pyenv global 3.11.9

python3 -m venv py_env  # Virtual env intiated

source py_env/bin/activate # venv activated

pip install apache-airflow==3.0.0 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.0/constraints-3.11.txt"

pip install apache-airflow[amazon,google]==3.0.0 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.0/constraints-3.11.txt"

export AIRFLOW_HOME=~/airflow

airflow standalone

http://localhost:8080