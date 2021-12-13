   #!/bin/bash 
   source buildimage
   set -x #echo on

   cd ansible

   #run anible plybook to deploy docker on controller
   ansible-playbook builddocker.yml

   #changinr permission on controller to run docker without sudo
   sudo  chmod +x /var/run/docker.sock
   sudo  chown $USER /var/run/docker.sock

   #list empty docker images
   docker images

   #building app image
   cd ../app/flask


   docker build  --network=host --no-cache -t $DOCKER_HUB_USER_NAME/$WEBAPPIMAGE:$VERSION_WEBAPP .

   #building proxy image

   cd ../nginx

   docker build --network=host --no-cache -t $DOCKER_HUB_USER_NAME/$PROXYIMAGE:$VERSION_NGINX .

  #list images
   docker images

   #pushing to docker hub
   docker login -u=$DOCKER_HUB_USER_NAME -p $DOCKER_HUB_PWD


   docker push $DOCKER_HUB_USER_NAME/$WEBAPPIMAGE:$VERSION_WEBAPP
   docker push $DOCKER_HUB_USER_NAME/$PROXYIMAGE:$VERSION_NGINX

   # for deployment on target machines running ansible playbook
   cd ../../ansible

   ansible-playbook deployapp.yml
