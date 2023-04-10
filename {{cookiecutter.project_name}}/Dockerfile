# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /{{cookiecutter.project_name}}
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
COPY requirements.txt requirements.txt
RUN pip3 install psycopg2-binary
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]