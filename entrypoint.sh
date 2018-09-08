#!/bin/sh
python manage.py makemigrations --settings=api.prod_settings
python manage.py migrate --settings=api.prod_settings
python manage.py runserver 0.0.0.0:80 --settings=api.prod_settings
