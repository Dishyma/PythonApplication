# PythonApplication

This is simple python web application with flask

## requirements

this application can be run on any operating system, but we base it on linux systems, therefore we use .sh files

## How to install our application

- first you have to clone our repository into your environment

### Https

    git clone https://github.com/Dishyma/PythonApplication.git
    cd PythonApplication/

### SSh

    git clone https://github.com/Dishyma/PythonApplication.git
    cd PythonApplication/

## Important

If you are running this application within a cloud environment, you must modify the web.py file and change the localhost address to your public IP address, in the same way it is recommended to use elastic IPs

![enter image description here](https://i.ibb.co/xGZcg0h/Screenshot-2023-05-08-105201.png)

## Running the application

- Run inicio.sh

This file will update the package repository, and install docker compose along with two images, mysql and ubuntu, finally, it will run the docker-compose.yml file, which will create three containers.

     sudo sh ./inicio.sh

### Another operating system**

    >  If you have another operating system, you must download docker
    > compose, and the images manually (mysql, ubuntu), and finally run the file
    > docker-compose.yml

## Finally

    > enter your localhost, or public ip through port 8080
