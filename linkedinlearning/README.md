$ kubectl cluster-info

# To get the Kubernetes control plane where it is running and the CoreDNS

# miniKube creates the cluster from scratch while kubectl to interact with the cluster

$ kubectl get nodes

# To get nodes from the minikube

$ kubectl get namespaces

# To get namespaces from the minikube

$ kubectl get pods -A

# To get all the pods from all the namespaces

$ kubectl get services -A

# To get all the services from all the namespaces

$ kubectl apply -f namespace.yaml

# To create a namespace from the namespace.yaml file

$ kubectl delete -f namespace.yaml

# To delete the namespace from the namespace.yaml file

$ kubectl get deployments -n development

# To get all the deployments from the development namespace

$ kubectl get pods -n development

# To get all the pods from the development namespace

$ kubectl delete pod pod-info-deployment-blah-blaw -n development

# To delete a pod from the development namespace

$ kubectl get pods -n development -o wide

# To get all the pods from the development namespace with more information

$ kubectl exec -it busybox-blahblah -- /bin/sh

# To get into the pod and execute commands inside the pod

/ # wget -O- ipaddress:port

/ # wget -O- http://whatever-service.namespace.svc.cluster.local

/ # wget -O- whatever-service

/ # exit

$ kubectl logs pod-info-deployment-blah-blaw -n development

# To get the logs from the pod in the development namespace

$ kubectl get services -n development

# To get all the services from the development namespace

$ kubectl api-resources

# To get all the api resources from the cluster

$ kubectl get pods -n kube-system

# To get all the pods from the kube-system namespace

$ snyk iac test deployment.yaml

# To scan the deployment.yaml file for any vulnerabilities








$ minikube start --driver=docker

# To start the minikube with docker driver

$ minikube status

# To check the status of the minikube

$ kubectl cluster-info

# To get the Kubernetes control plane where it is running and the CoreDNS

$ kubectl get nodes

# To get nodes from the minikube

$ kubectl get pods keepr -o json

# To get the etcdkeeper pod details in json format

$ kubectl api-versions

# To get all the api versions from the cluster

$ kubectl create ns raj

# To create a namespace raj

$ kubectl get sa -n raj

# To get all the service accounts from the raj namespace

$ kubectl get secret -n raj

# To get all the secrets from the raj namespace





$ minikube start --network-plugin=cni --cni=calico -p demo

# To start the minikube with calico cni plugin and profile name demo