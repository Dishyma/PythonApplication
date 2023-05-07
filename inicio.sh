##Update repository
sudo apt update

##Download docker compose
sudo apt install -y docker-compose

##Pull images
sudo docker pull ubuntu:latest
sudo docker pull mysql:latest

## Start with the containers
sudo docker-compose up