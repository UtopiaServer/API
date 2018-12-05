# UtopiaServer API Dockerfile
FROM python:3.7-alpine

RUN apk add --update mariadb-connector-c-dev build-base

RUN mkdir /srv/api
COPY requirements.txt /srv/api
COPY entrypoint.sh /srv/api
RUN pip install -r /srv/api/requirements.txt
COPY ./src /srv/api/src

# Allow root recursively on the folder
RUN chown root:root -R /srv/api

# Make the sources file, the working directory
WORKDIR /srv/api/src