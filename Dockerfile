FROM python:3.10.2-slim as python-base

WORKDIR /api
COPY . /api

RUN apt-get update -y \
    && apt-get install build-essential -y \
    && rm -rf /var/lib/apt/lists/* \
    && pip install flit \
    && FLIT_ROOT_INSTALL=1 flit install --deps production \
    && rm -rf $(pip cache dir)

CMD gunicorn krm_template_python.main:api -c krm_template_python/gunicorn_config.py
