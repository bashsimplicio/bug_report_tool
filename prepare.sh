#!/usr/bin/env bash

echo "Activating db..."

export DATABASE_URL="postgres://postgres:jasonmraz@127.0.0.1:5432/bug_report_tool"

python manage.py runserver_plus 8001

