curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
docker-compose up airflow-init
docker-compose up

# Docker installing Airflow

When running Apache Airflow with Docker Compose, the default username and password for accessing the Airflow web interface are:

Username: airflow
Password: airflow

These credentials are automatically created during the initialization of the Airflow environment within the Docker containers. You can use them to log into the web UI, typically available at http://localhost:8080 after the services have started.
