#!/bin/sh
gunicorn -c gunicorn_config.py wsgi:app