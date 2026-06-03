#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
DJANGO_SUPERUSER_PASSWORD="Pial4200" python manage.py createsuperuser --username "pial_admin" --email "admin@example.com" --noinput || true