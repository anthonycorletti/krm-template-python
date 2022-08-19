#!/bin/sh -ex

mypy krm_template_python tests
flake8 krm_template_python tests
black krm_template_python tests --check
isort krm_template_python tests scripts --check-only
