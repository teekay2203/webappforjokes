# webappforjokes
This repository contains code for deploying a python app which displays Jokes From Chuck Noris api. User has to give the host name to display random joke. If he wants to see what category jokes are available , he can give /category in url bar to see the list of available category. However, on main page also 16 categories are mentioned for simplification. User can give any particular category in address bar to list jokes for that category.

# Prerequisite
1. Ansible should be deployed on controller machine.
2. Target machines should be available. 
3. Controller machine should be able to connect to target machines via ssh.

# Assumption
1. User will give version, name of image, and docker hub account login id pwd in config file .
2. As of now current version of images "teekay2203/myjokes:3.0" and "teekay2203/mynginx:3.0" have been mentioned in ansible-playbook.
3. User can change on his own.

# Building and Deploying of project

Buidling and deployment of project is fully automated. user can clone the repository into his machine and go to the folder webappforjokes which gets generated after the cloning.
User has to run ./buildimage.sh script for build, integrate and deployment. 

# working of buildimage.sh script
1. First it reads the config file which is named buildimage and placed in same directory. This config file contains version number for our app and proxy image , user name of our docker-hub account and the password of docker hub account, name of image to be given to our app and proxy server.
2. Then it runs first ansible play book to install docker on host machine . In "hosts" file which is placed at path webappforjokes/ansible/ , docker host address has to be mentioned.
3. Then it goes in app/flask directory to build the image of application.This app has been developed using "flask" of python with "uWSGI" as applciation server. Setting for this has been done in "app.ini" file and proxy address has been modified in Nginx image. It also tags the image with latest version mention in config file.
3. Then it builds proxy-server image which is Nginx in our case. This image contains Nginx image with changed setting for our app.It also tags the image with latest version mention in config file.
4. Then it logins to docker hub for pushing the images and push them on docker hub.
5. Then it runs the second playbook to deploy those images on target machines. Target machines address have to be specified in webappforjokes/ansible/hosts file.
6. This playbook install docker in target machine/s , pull the images from docker hub (name given in the ansible playbook as variable), and run them as container.
7. user can check the output using "curl http://localhost" command or directly can hit the external ip of machine from any browser(internet).

# Note:
Docker-Compose has also been installed on controller and target machine.

docker-compose.yml and docker-compose-main.yml are also present. So if someone wants to build or run images using compose , he can do that as well.

docker-compose.yml will build the images and run them as container.

docker-compose-main.yml will pull the images pushed on docker-hub and run them as container.
