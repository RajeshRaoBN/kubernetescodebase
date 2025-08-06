> python3 -m venv ./venv

> source ./venv/bin/activate

> pip install fastapi
> pip install uvicorn
> pip freeze

> code requirement.txt

> pip install -r requirement.txt




> docker build -t k8s-fast-api .

> docker run -p 8000:80 k8s-fast-api

> docker push rbnrao/k8s-fast-api-getting-started

> kubectl port-forward fast-api-deployment-xxxx-xxxx 8080:80