FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk update 

ADD . /usr/src/app/
RUN pip install -r requirements.txt