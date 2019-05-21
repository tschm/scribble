#!make
PROJECT_VERSION := $(shell python setup.py --version)

SHELL := /bin/bash
PACKAGE := risk_orm
IMAGE := tschm/scribble

# needed to get the ${PORT} environment variable
include .env
export

.PHONY: help build jupyter tag hub

.DEFAULT: help

help:
	@echo "make build"
	@echo "       Build the docker image."
	@echo "make jupyter"
	@echo "       Start the Jupyter server."
	@echo "make tag"
	@echo "       Make a tag on Github."
	@echo "make hub"
	@echo "       Push Docker Image to DockerHub."

build:
	docker-compose build jupyter

tag:
	git tag -a ${PROJECT_VERSION} -m "new tag"
	git push --tags

hub: tag
	docker build --tag ${IMAGE}:latest --no-cache --target production .
	docker push ${IMAGE}:latest
	docker tag ${IMAGE}:latest ${IMAGE}:${PROJECT_VERSION}
	docker push ${IMAGE}:${PROJECT_VERSION}
	docker rmi -f ${IMAGE}:${PROJECT_VERSION}

jupyter: build
	echo "http://localhost:${PORT}"
	docker-compose up jupyter
