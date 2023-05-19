# AplicaciónPython

Esta es una aplicación web de python simple con matraz

## requisitos

esta aplicación se puede ejecutar en cualquier sistema operativo, pero la basamos en sistemas linux, por lo tanto usamos archivos .sh

## Cómo instalar nuestra aplicación

- primero tienes que clonar nuestro repositorio en tu entorno

### HTTPS

    git clone https://github.com/Dishyma/PythonApplication.git
    cd PythonApplication/

### SSH

    git clone https://github.com/Dishyma/PythonApplication.git
    cd PythonApplication/

## Importante

Si está ejecutando esta aplicación dentro de un entorno de nube, debe modificar el archivo web.py y cambiar la dirección localhost a su dirección IP pública, de la misma manera se recomienda utilizar direcciones IP elásticas.

![ingrese la descripción de la imagen aquí](https://i.ibb.co/xGZcg0h/Screenshot-2023-05-08-105201.png)

Si está en un entorno de nube, habilite también el puerto 8080 y el puerto 5600 en los grupos de seguridad

![ingrese la descripción de la imagen aquí](https://i.ibb.co/Lpqn0KF/Screenshot-2023-05-08-111725.png)

## Ejecutando la aplicación

- Ejecutar inicio.sh

Este archivo actualizará el repositorio de paquetes e instalará docker compose junto con dos imágenes, mysql y ubuntu, finalmente, ejecutará el archivo docker-compose.yml, que creará tres contenedores.

     sudo sh ./inicio.sh

### Otro sistema operativo**

    > Si tienes otro sistema operativo, debes descargar docker
    > compose, y las imágenes manualmente (mysql, ubuntu), y finalmente ejecutar       el archivo
    > docker-compose.yml

## Finalmente

    debemos esperar un poco, hasta que los tres contenedores este corriendo de forma correcta
    > ingrese su host local o IP pública a través del puerto 8080

    > Si es primera vez deves registrarte primero, y luego ingresar!



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

If you are in a cloud environment, also enable port 8080 and port 5600 in the security groups

![enter image description here](https://i.ibb.co/Lpqn0KF/Screenshot-2023-05-08-111725.png)

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
