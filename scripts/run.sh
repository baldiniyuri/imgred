#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

whoami

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8100




uwsgi --socket :9100 --workers 4 --master --enable-threads --module app.wsgi

