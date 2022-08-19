#!/bin/sh -ex

# Sort imports one per line, so autoflake can remove unused imports
isort --force-single-line-imports krm_template_python tests scripts

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place krm_template_python tests scripts --exclude=__init__.py
black krm_template_python tests scripts
isort krm_template_python tests scripts
