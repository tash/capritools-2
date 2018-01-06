#!/bin/bash
#set -eo pipefail

if [ -e capritools.sqlite ]; then
	echo "Apply migrations"
	python manage.py migrate
else
	echo "Import SDE"
	python manage.py migrate
	python import.py
fi

echo "Starting server"
python manage.py runserver 0.0.0.0:8000