# random-travelers
People who make thier decisions decided by Cloud Native

## Run application locally
As random-travelers application requires relational database, we have to prepare database before starting application program.
The most handy and easy way to start database is using container, and considering security we basically expect [`bitnami/mysql`](https://bitnami.com/stack/mysql/containers) container for local docker environment.
For further information about `bitnami/mysql`, please refer [the sources in GitHub](https://github.com/bitnami/containers/tree/main/bitnami/mysql).

```bash
# Start MySQL container with setting root password & creating database
% docker run -d --name rt -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=rt bitnami/mysql:latest
% docker container ls
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS          PORTS                                       NAMES
c0abdba6a3e6   bitnami/mysql:latest   "/opt/bitnami/script…"   30 seconds ago   Up 30 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp   rt
```

For ruuning Python application locally, we have to install dependencies packages onto local, but we prefer to use virutalenv for creating separate/isolated Python runtime.

```bash
# Name of virtualenv `.venv` is just an example so you can use what you like
% python -m venv .venv
% source .venv/bin/activate

# Install dependencies
% pip install -r requirements.txt
% pip list

# Starting application
% python main.py
```
