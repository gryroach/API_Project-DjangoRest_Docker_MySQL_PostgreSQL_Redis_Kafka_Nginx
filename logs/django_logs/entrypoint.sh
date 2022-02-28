#!/bin/sh

#set -e # exit if errors happen anywhere
python manage.py migrate --noinput
python manage.py collectstatic --no-input --clear
#gunicorn django_logs.wsgi:application --bind 0.0.0.0:8000
#uwsgi --socket :8000 --master --enable-threads --module django_logs.wsgi
#gunicorn django_logs.wsgi:application --bind 0.0.0.0:8000
