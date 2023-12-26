IMAGE_NAME := property_based_testing

image:
	docker build -t ${IMAGE_NAME} .

mypy:
	docker run -v ${CURDIR}:/srv ${IMAGE_NAME} mypy .

flake:
	docker run -v ${CURDIR}:/srv ${IMAGE_NAME} flake8 --ignore E501 .

tests:
	docker run -v ${CURDIR}:/srv ${IMAGE_NAME} pytest -q .

deploy:
	docker run -v ${CURDIR}:/srv ${IMAGE_NAME} python setup.py sdist

full-pipeline: image mypy tests flake
