FROM python:3.8.10-slim-buster

WORKDIR /home/app

RUN pip install --upgrade pip
COPY ./notify/requirements.txt /home/app/requirements.txt
RUN pip install -r requirements.txt
