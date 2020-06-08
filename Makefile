#!make
PROJECT_VERSION := 0.0.6

SHELL := /bin/bash
IMAGE := tschm/scribble
PORT  := 8888
WORK  := /home/jovyan/work

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

jupyter: build
	echo "http://localhost:${PORT}"
	docker-compose up jupyter

jupyterlab: build
	echo "http://localhost:${PORT}/lab"
	docker-compose up jupyter
