# random-travelers
People who make thier decisions decided by Cloud Native

<!-- *** -->
## Prerequisites
Since random-travelers application would handle location information, the app requires us to **allow location service enabled** in client side.

<!-- *** -->
## Run locally
As random-travelers application requires relational database, we have to prepare database before starting application program. \
The most handy and easy way to start database is using container, and considering security we basically expect [`bitnami/mysql`](https://bitnami.com/stack/mysql/containers) container for local docker environment. \
For further information about `bitnami/mysql`, please refer [the sources in GitHub](https://github.com/bitnami/containers/tree/main/bitnami/mysql).

Since we have prepared Makefile to launch app easily with some subcommands, just run:

```bash
% export GOOGLE_MAPS_API_KEY="***"
% export JAWSDB_URL='mysql://root:root@0.0.0.0:3306/rt'

# This will invoke start up process both for application and databases
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

For ruuning Python application locally, we have to install dependencies packages onto local, but we prefer to use virutalenv for creating separate/isolated Python runtime. \
Code basis would be managed by poetry, so you can install deps simply like below:

```bash
# Install dependencies
% poetry install

# Starting application inside virtualenv with configurations
% export JAWSDB_URL='mysql://root:root@0.0.0.0:3306/rt'
% export GOOGLE_MAPS_API_KEY="***"
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

# Starting application with configurations
% export JAWSDB_URL='mysql://root:root@0.0.0.0:3306/rt'
% export GOOGLE_MAPS_API_KEY="***"
% uvicorn app.main:app --port=3000 --reload
```

Then you can confirm API for health check would be valid, so that application startup would have been successed

```bash
# validate with /healthz
% curl -X GET localhost:3000/healthz; echo
{"status":"ok"}
```

<!-- *** -->
## Builds and Deployments
### Image builds
In this project, FastAPI application wll be deployed onto [Heroku](https://www.heroku.com) as application platform.

The applications on Heroku is formed as contianers, and its container images will be sourced from GitHub Container Registry. \
On Heroku, it has great build system, [Buildpacks](https://devcenter.heroku.com/articles/buildpacks), which will create secure container image easily with its `Builders`, \
and we can also use this Builder local or CI environment.
You can download the actual images built by [Heroku Buildpacks](https://github.com/heroku/buildpacks) in CI (GitHub Actions) from [GitHub Packages](https://github.com/hwakabh/random-travelers/pkgs/container/random-travelers).

```shell
% docker pull ghcr.io/hwakabh/random-travelers:latest
```

For image builds, please refer more details with the following articles:
- [Buildpacks.io](https://buildpacks.io)
- [pack-cli](https://github.com/buildpacks/pack)

### Heroku Deployment
Heroku, where `random-travelers` app has been hosted, has features to connect Git repository and its deployment (app source) called Automatic Deploys as a part of [GitHub integrations](https://devcenter.heroku.com/articles/github-integration).

So once we will make changes on `main` branch on this repo, the changes has been immediately applied to production apps, and this will realize Continous Deliveries of app with lower operational costs.

### Kubernetes Deployment
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

<!-- *** -->
## Environmental Variables
### JAWSDB_URL
This value will be used for application to know what database should be connected. \
On Heroku, we can use JawsDB, MySQL as a Service, with free costs, and the URL of JawsDB will represent as the following format:

```shell
{db_protocol}://{db_username}:{db_password}@{db_hostname}:{db_port}/{db_database_name}
```

Currently we have only supported MySQL as application backend with using [`mysql-connector-python`](https://github.com/mysql/mysql-connector-python), but once you customized the parse logic of `JAWSDB_URL`, you will be able to use another database as backend database.

For running application locally, `bitnami/mysql` container will be expected as first choice, so the value would looks like:

```shell
mysql://root:root@0.0.0.0:3306/rt
```

### GOOGLE_MAPS_API_KEY
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
