IMAGE_NAME := property_based_testing
image:
	docker build -t $IMAGE_NAME .
mypy:
	docker run -v ${CURDIR}:/srv ${IMAGE_NAME} mypy /srv
