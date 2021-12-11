   #!/bin/bash
   
   source buildimage
   set -x #echo on
    
   git clone https://github.com/teekay2203/webappforjokes.git

   cd ./webappforjokes/app/flask

   docker build  --network=host --no-cache -t $DOCKER_HUB_USER_NAME/$WEBAPPIMAGE:$VERSION_WEBAPP .

   cd ./webappforjokes/app/flask

   docker build --network=host --no-cache -t $DOCKER_HUB_USER_NAME/$PROXYIMAGE:$VERSION_NGINX .


   docker images 

   docker login -u=$DOCKER_HUB_USER_NAME -p $DOCKER_HUB_PWD
     

  # docker tag $WEBAPPIMAGE:$VERSION_WEBAPP  $DOCKER_HUB_USER_NAME/$WEBAPPIMAGE:$VERSION_WEBAPP

   #docker tag $PROXYIMAGE:$VERSION_NGINX  $DOCKER_HUB_USER_NAME/$PROXYIMAGE:$VERSION_NGINX


   docker push $DOCKER_HUB_USER_NAME/$WEBAPPIMAGE:$VERSION_WEBAPP
   docker push $DOCKER_HUB_USER_NAME/$PROXYIMAGE:$VERSION_NGINX
