include .env

DOCKER_IMAGE_GCR_URI := gcr.io/${PROJECT_ID}/${CLOUD_RUN_SERVICE_NAME}:latest

.PHONY: all build push deploy

all: build push deploy

build:
	docker buildx build --platform linux/amd64 -t ${DOCKER_IMAGE_GCR_URI} ./

push:
	docker push ${DOCKER_IMAGE_GCR_URI}

deploy:
	gcloud run deploy ${CLOUD_RUN_SERVICE_NAME} --region asia-northeast1 --project ${PROJECT_ID} --image=${DOCKER_IMAGE_GCR_URI}
