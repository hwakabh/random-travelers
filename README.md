# random-travelers
People who make thier decisions decided by Cloud Native

## Prerequisites
Since random-travelers application would handle location information, the app requires us to allow location service enabled in client side.

## Run locally
As random-travelers application requires relational database, we have to prepare database before starting application program. \
The most handy and easy way to start database is using container, and considering security we basically expect [`bitnami/mysql`](https://bitnami.com/stack/mysql/containers) container for local docker environment. \
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

# provide database url with fallbacks
% export JAWSDB_URL='mysql://root:root@0.0.0.0:3306/rt'
```
The environmental variables required by apps and its default values in application builds are described in Makefile. \
Please check [`Makefile`](./Makefile) and you can customize them in yoru local environment.

For ruuning Python application locally, we have to install dependencies packages onto local, but we prefer to use virutalenv for creating separate/isolated Python runtime. \
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

## Builds and Deployments
In this project, FastAPI application wll be deployed to [Railway](https://railway.com) as application platform. \
As you can easily setup accounts with free trials, please visit [the official documents](https://docs.railway.com) for further references.

In Railway, the steps for application builds as container image will be done by [Nixpacks](https://nixpacks.com/docs), and you can see its configurations in [`nixpacks.toml`](./nixpacks.toml). \
As there is a lot of options for application builds, please also refer [the documents](https://nixpacks.com/docs/configuration/file) for more details.

The applications on Railway is formed as contianers, and its container images will be sourced from GitHub Container Registry. \
You can download the actual images built by Nixpacks in CI (GitHub Actions) from [GitHub Packages](https://github.com/hwakabh/random-travelers/pkgs/container/random-travelers).

```shell
% docker pull ghcr.io/hwakabh/random-travelers:latest
```

Also in case you would like to deploy application on Kubernetes clusters, you can have an options to deploy apps onto [KinD](https://kind.sigs.k8s.io) cluster in your local environment. \
You can create all Kubernetes resources from manifests in this repository, after [the installations](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) of `kind` commands:

```shell
% kind create cluster --config kind-cluster.yaml

# Install sealed-secret-controllers
% kubectl apply -f ./manifests/controllers/sealed-secret-controller.yaml

# Install application resources with Kustomization
% kubectl apply -k ./manifests

# Required for sealed-secret-controller to unseal SealedSecret resources
% cat << EOF |kubeseal - -o yaml |kubectl apply -f -
---
apiVersion: v1
kind: Secret
metadata:
  name: mysql-secret
  namespace: random-travelers
  labels:
    app: random-travelers
type: Opaque
data:
  MYSQL_ROOT_PASSWORD: $(echo -n root |base64)
  MYSQL_DATABASE: $(echo -n rt |base64)
EOF
```

## Environmental Variables of GOOGLE_MAPS_API_KEY

For local:
```shell
% export GOOGLE_MAPS_API_KEY='xxx'
```

In production env, where we expect to run app on Railway, they are mounted to app with Variables of Railway apps. \
But for security consideration, we will use [Sealed Secret](https://github.com/bitnami-labs/sealed-secrets) to hide confidential information from GitHub, so you have to install sealed-secret-controller first to the Kubernetes cluster that you will use need, if you use your BYO cluster.

For updating each environmental variables to be sealed, you need to install `kubeseal` commands to interact with sealed-secret-controller, then you need to create generic Secret resources:
```shell
% cat << EOF |kubeseal - -o yaml |kubectl apply -f -
---
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
  namespace: random-travelers
  labels:
    app: random-travelers
type: Opaque
data:
  MYSQL_HOST: $(echo -n mysql.random-travelers.svc.cluster.local |base64)
  MYSQL_USER: $(echo -n root |base64)
  MYSQL_PASSWORD: $(echo -n root |base64)
  MYSQL_DATABASE: $(echo -n rt |base64)
  GOOGLE_MAPS_API_KEY: $(echo -n $GOOGLE_MAPS_API_KEY |base64)
EOF
```

Once you can complete all required setup, you can see the following resources:

```shell
# main resources on kind-cluster
% kubectl -n random-travelers get pods,deploy,sts,pvc,secrets,sealedsecrets
NAME                           READY   STATUS    RESTARTS   AGE
pod/fastapi-6b9cd8d559-2gmsj   1/1     Running   0          22m
pod/mysql-0                    1/1     Running   0          26m
pod/mysql-1                    1/1     Running   0          25m
pod/mysql-2                    1/1     Running   0          23m

NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/fastapi   1/1     1            1           26m

NAME                     READY   AGE
statefulset.apps/mysql   3/3     26m

NAME              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/fastapi   ClusterIP   10.96.236.238   <none>        80/TCP     28m
service/mysql     ClusterIP   None            <none>        3306/TCP   28m

NAME                                       STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
persistentvolumeclaim/mysql-data-mysql-0   Bound    pvc-f12a317b-e0ad-4613-ada3-ed1314a55313   5Gi        RWO            standard       <unset>                 26m
persistentvolumeclaim/mysql-data-mysql-1   Bound    pvc-f0607751-c65a-44c3-a1d3-f5b79fe812b7   5Gi        RWO            standard       <unset>                 25m
persistentvolumeclaim/mysql-data-mysql-2   Bound    pvc-57e2cc12-6c5f-4c82-82a8-cc0acd3b4bcf   5Gi        RWO            standard       <unset>                 23m

NAME                  TYPE     DATA   AGE
secret/app-secret     Opaque   5      24m
secret/mysql-secret   Opaque   2      26m

NAME                                    AGE
sealedsecret.bitnami.com/app-secret     26m
sealedsecret.bitnami.com/mysql-secret   26m

# you can access to application UI with port-forwarding at localhost:8080,
# or of course you can install any of Ingress or LoadBalancer with your kind-cluster!
% kubectl -n random-travelers port-forward svc/fastapi 8080:80
# ...
```

## API directory layout
Application root for API: `app/*`
- `database.py` and `config.py`
  - The configuration parameters for application
  - Determine where/how to connect

API Specifics structures in `app/api/v1/*`
- `routers.py`: Application URL routings with CRUDs and Services
  - Routers itself is responsible on dispatching, so that it lies on top with CRUDs/Services

- `cruds.py`: Database operations using with models
  - `models.py`: Table definitions with ORM

- `services.py`: Operations with other services including external endpoints

- `schemas.py`: Contains Request/Response models

- `helpers.py`: Helper functions for CRUDs/Services
