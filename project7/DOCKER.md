> docker pull nginx:latest # to pull an images

> docker images    # To list all the images

> docker run nginx:latest    # To run the image in a container

>docker container ls     # To list the running containers

> docker run - d nginx:latest    # To run the image in a container in a detached mode

> docker ps    # lists all the containers

> docker stop containerID     # to stop the container

> docker run - d  -p 8080:80 nginx:latest    # To run the image in a container in a detached mode to be mapped to port 8080

> docker rm containerID    # To remove the container not just stop

> docker ps -aq     # Will list only the container ids

> docker rm $(docker ps -aq)     # Will remove all the containers

NOTE: You cant remove a running container. You need to stop it before removing or you can force quit using -f as below

> docker rm -f $(docker ps -aq)     # Will remove all the containers will force quit running containers before removing

> docker run - d  -p 8080:80 -p 3000:80 nginx:latest    # To run the image in a container in a detached mode to be mapped to two ports 8080 and 3000

> docker run --name mywebsite - d  -p 8080:80 -p 3000:80 nginx:latest    # To run the image in a container in a detached mode to be mapped to two ports 8080 and 3000 to give a name to the server

> docker ps --format '{{ .Names }}\t{{.RunningFor}}\t{{ .Ports }}'     # Docker list format

> docker run --name mywebsite -v $(pwd):/usr/share/nginx/html:ro -d -p 8080:80 nginx    # run the container and load a index.html volume on it.

> docker exec -it mywebsite bash    # This is to open an interactive session

> docker build --tag mywebsite:latest .     # This is to build an image in the current directory

> docker tag mywebsite:latest rbnrao/mainwebsite:1 # Attaching tags to a new image

> docker push rbnrao/mainwebsite:1     # To push to docker repo

> docker pull rbnrao/mainwebsite:1

> docker describe containerID    # To describe a container

> docker logs containerID    # To see logs of the container

> docker inspect containerID.    # To inspect the container