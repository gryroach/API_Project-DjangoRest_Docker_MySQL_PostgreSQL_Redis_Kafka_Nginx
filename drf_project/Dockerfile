# pull official base image
FROM python:3.9

# copy project
COPY ./drf_app src/drf_app
COPY ./drf_project src/drf_project
COPY manage.py src/


# set work directory
WORKDIR /src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt update
RUN apt-get install -y netcat

COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT [ "/bin/bash", "entrypoint.sh"]