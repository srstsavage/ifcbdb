#!/bin/bash

docker compose exec ifcbdb python manage.py collectstatic --no-input
