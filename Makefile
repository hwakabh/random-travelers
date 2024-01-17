MAKEFLAGS += --warn-undefined-variables
SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help

MYSQL_CONTAINER_NAME := "rt-mysql"

# all targets are phony
.PHONY: $(shell egrep -o ^[a-zA-Z_-]+: $(MAKEFILE_LIST) | sed 's/://')

--check-docker:
	@echo ">>> Checking docker engine exists ..."
	@echo "Server: `docker version --format '{{.Server.Version}}'`"
	@echo "Client: `docker version --format '{{.Client.Version}}'`"
	@echo ''


--check-poetry:
	@echo ">>> Checking poetry installed ..."
	@poetry --version
	@echo ''


db: --check-docker ## Starting MySQL container
	@echo ">>> Starting MySQL container ..."
	@docker start ${MYSQL_CONTAINER_NAME} 2> /dev/null || docker run -d \
		--name ${MYSQL_CONTAINER_NAME} \
		-p 3306:3306 \
		-e MYSQL_DATABASE='rt' \
		-e MYSQL_ROOT_PASSWORD='root' \
		--health-cmd "mysqladmin ping --user=root --password=root" \
		--health-interval 10s \
		--health-retries 5 \
		--health-timeout 5s \
		bitnami/mysql:latest
	@while [ "`docker inspect -f {{.State.Health.Status}} ${MYSQL_CONTAINER_NAME}`" != "healthy" ]; do \
		sleep 3; \
	done
	@echo 'Database is now healthy state'
	@echo ''


install: --check-poetry ## Install all dependencies for app
	@echo ">>> Installing all packages required for application ..."
	@poetry install


show: --check-poetry --check-docker ## Show related components for app
	@echo ">>> Packages installed in virtualenv"
	@poetry show
	@echo ''
	@echo ">>> Containers running on machine"
	@docker container ls --all
	@echo ''
	@echo ">>> Application process"
	@ps -ef |grep uvicorn |grep -v 'grep' || true
	@echo ''


all: ## Start all componentes of portal-core app
	@make db
	@make install
	@poetry run uvicorn app.main:app --port=3000 --reload &


clean: ## Remove components
	@echo ">>> Removing MySQL containers ..."
	@docker stop ${MYSQL_CONTAINER_NAME} 2> /dev/null || true
	@docker rm ${MYSQL_CONTAINER_NAME} 2> /dev/null || true
	@echo ''
	@echo ">>> Stopping application process ..."
	@pkill -f uvicorn || true
	@echo ''
	@echo ">>> Cleaning up container network ..."
	@echo ''


help: ## Print this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
