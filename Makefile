IMAGE_NAME := property_based_testing

image:
	docker build -t ${IMAGE_NAME} .

mypy:
	docker run -v ${CURDIR}:/srv ${IMAGE_NAME} mypy /srv

flake:
	docker run -v ${CURDIR}:/srv ${IMAGE_NAME} flake8 --ignore E501 /srv

tests:
	docker run -v ${CURDIR}:/srv ${IMAGE_NAME} pytest -q /srv

full-pipeline: mypy tests flake
