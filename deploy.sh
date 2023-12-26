#!/usr/bin/env sh
python setup.py sdist
twine upload --non-interactive dist/*
