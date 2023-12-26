IMAGE_NAME := property_based_testing
DOCKER_RUN := docker run -v ${CURDIR}:/srv ${IMAGE_NAME}

image:
	docker build -t ${IMAGE_NAME} .

mypy:
	${DOCKER_RUN} mypy .

flake:
	${DOCKER_RUN} flake8 --ignore E501 .

tests:
	${DOCKER_RUN} pytest -q .

deploy:
	${DOCKER_RUN} ./deploy.sh

full-pipeline: image mypy tests flake
