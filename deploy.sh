#!/usr/bin/env sh
set -e
python setup.py sdist
#twine upload --non-interactive dist/*
echo deploying version $(cat property_based_testing/__init__.py)