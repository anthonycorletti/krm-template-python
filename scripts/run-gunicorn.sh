#!/bin/sh -ex

gunicorn krm_template_python.main:api -c krm_template_python/gunicorn_config.py
