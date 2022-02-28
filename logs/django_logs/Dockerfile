# pull official base image
FROM python:3.8.10

# copy project
COPY app_logs src/app_logs
COPY django_logs src/django_logs
COPY manage.py src/
COPY entrypoint.sh src/
RUN mkdir -p src/staticfiles


# set work directory
WORKDIR /src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ENV UWSGI_WORKERS=2 UWSGI_THREADS=4

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
#python manage.py collectstatic --no-input --clear
#CMD ["/src/entrypoint.sh"]
CMD ["sh", "/src/entrypoint.sh"]