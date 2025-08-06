> kubectl create deployment my-nginx --image=nginx --replicas=3

### This is to run 3 replicas of nginx images

> kubectl expose deployment my-nginx --port=80

### This is to expose port 80 to the pods

> kubectl get svc my-nginx

> kubectl port-forward svc/my-nginx 8080:80

### This is for port forwarding to 8080

### CLEAN UP

> kubectl delete service my-nginx

### First service

> kubectl delete deployment my-nginx

### Then the deployment as it will stop all the pods