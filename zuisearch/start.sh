#!/bin/sh
source env/bin/activate
nohup gunicorn --env DJANGO_SETTINGS_MODULE=zuisearch.settings -b 127.0.0.1:81 zuisearch.wsgi&
/etc/init.d/nginx restart
