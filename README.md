# random-travelers
People who make thier decisions decided by Cloud Native

## Prerequisites
Since random-travelers application would handle location information, the app requires us to allow location service enabled in client side.

## Run application locally
As random-travelers application requires relational database, we have to prepare database before starting application program.
The most handy and easy way to start database is using container, and considering security we basically expect [`bitnami/mysql`](https://bitnami.com/stack/mysql/containers) container for local docker environment.
For further information about `bitnami/mysql`, please refer [the sources in GitHub](https://github.com/bitnami/containers/tree/main/bitnami/mysql).

Since we have prepared Makefile to launch app easily with some subcommands, just run:
```bash
% make all
```

If you would like to run containers with docker command directly:
```bash
# Start MySQL container with setting root password & creating database
% docker run -d --name rt -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=rt bitnami/mysql:latest
% docker container ls
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS          PORTS                                       NAMES
c0abdba6a3e6   bitnami/mysql:latest   "/opt/bitnami/script…"   30 seconds ago   Up 30 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp   rt
```

For ruuning Python application locally, we have to install dependencies packages onto local, but we prefer to use virutalenv for creating separate/isolated Python runtime.
Code basis would be managed by poetry, so you can install deps simply like below:

```bash
# Install dependencies
% poetry install

# Start app within virtualenv
% poetry run uvicorn app.main:app --port=3000 --reload
```

In case you would not use poetry:
```bash
# Name of virtualenv `.venv` is just an example so you can use what you like
% python -m venv .venv
% source .venv/bin/activate

# Install dependencies
% pip install -r requirements.txt
% pip list

# Starting application
% uvicorn app.main:app --port=3000 --reload
```

Then you can confirm API for health check would be valid, so that application startup would have been successed
```bash
# validate with /healthz
% curl -X GET localhost:3000/healthz; echo
{"status":"ok"}
```
