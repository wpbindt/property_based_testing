IMAGE_NAME := property_based_testing
DOCKER_RUN := docker run -v ${CURDIR}:/srv ${IMAGE_NAME}
DOCKER_RUN_WITH_SECRETS := docker run -v ${CURDIR}:/srv --env-file secrets.env ${IMAGE_NAME}

.PHONY: image
image:
	docker build -t ${IMAGE_NAME} .

.PHONY: mypy
mypy:
	${DOCKER_RUN} mypy .

.PHONY: flake
flake:
	${DOCKER_RUN} flake8 --ignore E501 .

.PHONY: tests
tests:
	${DOCKER_RUN} pytest -q .

.PHONY: deploy
deploy: full-pipeline
	${DOCKER_RUN_WITH_SECRETS} ./deploy.sh

.PHONY: full-pipeline
full-pipeline: image mypy tests flake
