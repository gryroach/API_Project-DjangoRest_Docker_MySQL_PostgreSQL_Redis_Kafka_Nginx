#!/bin/sh

#set -e # exit if errors happen anywhere
python manage.py migrate

#uwsgi --socket :8000 --master --enable-threads --module django_logs.wsgi
gunicorn django_logs.wsgi:application --bind 0.0.0.0:8000
