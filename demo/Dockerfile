FROM python:3.7.2
LABEL maintainer ZoeLiao
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'demo.settings.prod'
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api
RUN pip install -r requirements.txt
