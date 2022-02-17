# pull official base image
FROM python:3.8.10

# copy project
COPY ./app_logs src/app_logs
COPY ./django_logs src/django_logs
COPY manage.py src/


# set work directory
WORKDIR /src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt