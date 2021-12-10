FROM alpine:latest

#FROM python:3.9-alpine


  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip

#RUN pip3 install --upgrade pip

RUN pip3 install --no-cache --upgrade pip setuptools==3.3

RUN pip3 install pip==21.0.1

#RUN python3 -m pip install bpy && bpy_post_install

RUN apk add --no-cache python3 py3-pip

#RUN pip3 install --upgrade pip

RUN apk add python3-dev build-base linux-headers pcre-dev

#RUN apk add  python-dev

#RUN apk add python39-devel

#RUN python3 -m pip3 install bpy && bpy_post_install

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN apk add gcc build-base linux-headers

# Install the dependencies
RUN pip3 install -r requirements.txt


# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
