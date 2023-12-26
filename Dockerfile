FROM python:3.11.7-alpine

RUN pip install mypy
RUN pip install pytest
RUN pip install flake8
RUN pip install setuptools
RUN pip install types-setuptools
RUN pip install wheel
RUN pip install twine

WORKDIR /srv
