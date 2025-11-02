# Changelog

## [0.7.1](https://github.com/hwakabh/random-travelers/compare/v0.7.0...v0.7.1) (2025-11-02)


### Bug Fixes

* migrated from bitnami/mysql to bitnamilegacy/mysql images. ([67f53bc](https://github.com/hwakabh/random-travelers/commit/67f53bc9fd7abe32fa204cbb5b69aa99429a7e38))

## [0.7.0](https://github.com/hwakabh/random-travelers/compare/v0.6.3...v0.7.0) (2025-05-25)


### Features

* added error-handling of translate API. ([d895d86](https://github.com/hwakabh/random-travelers/commit/d895d868bbc6637531224d7b992307921542bc05))
* added prechecks before loading fixtures. ([b69cb96](https://github.com/hwakabh/random-travelers/commit/b69cb96bf9c39ee193debd1ba3feec3d10fd7e1f))
* enabled to fetch fixture data dynamically. ([dc2275c](https://github.com/hwakabh/random-travelers/commit/dc2275cdab179bb18b972b78eb3e35d32626e383))

## [0.6.3](https://github.com/hwakabh/random-travelers/compare/v0.6.2...v0.6.3) (2025-05-25)


### Bug Fixes

* **ci:** syntax error on stale-issue. ([9e353c4](https://github.com/hwakabh/random-travelers/commit/9e353c44a4bb291705f9f150b7acda0552d2900b))

## [0.6.2](https://github.com/hwakabh/random-travelers/compare/v0.6.1...v0.6.2) (2025-05-25)


### Bug Fixes

* **build:** added fallback URL of MySQL credentials for Uvicorn app. ([39b2a92](https://github.com/hwakabh/random-travelers/commit/39b2a92d027082f5577efef4d42dcc4f5963304b))
* **database:** error on sesison closing in get_db(). ([0f2ba2b](https://github.com/hwakabh/random-travelers/commit/0f2ba2b29b3db2728d899effa5be204014c4c716))
* **db:** current query filters with escape chars. ([1c17126](https://github.com/hwakabh/random-travelers/commit/1c1712688e72f703b9a998bad40826bae96b376d))


### Documentation

* fixed descriptions with removing Railway and Nixpack stuffs. ([43eac89](https://github.com/hwakabh/random-travelers/commit/43eac8989c556f98c872a4aa9b3fbf8939762e59))

## [0.6.1](https://github.com/hwakabh/random-travelers/compare/v0.6.0...v0.6.1) (2025-04-10)


### Documentation

* added commnads for database fallbacks in local env. ([354f16f](https://github.com/hwakabh/random-travelers/commit/354f16f6952799a47669b26bb1fa317a9998e88b))

## [0.6.0](https://github.com/hwakabh/random-travelers/compare/v0.5.0...v0.6.0) (2025-01-19)


### Features

* **database:** added functions for loading initial data to MySQL. ([fc22087](https://github.com/hwakabh/random-travelers/commit/fc220879a8b6d402048e0781d0fa63aa8a19f6cb))
* **deploy:** added commands with railway-cli to Publish CI. ([8b21b71](https://github.com/hwakabh/random-travelers/commit/8b21b71a31c6f3c9dcc9a88a6f4db082447bb4de))
* enabled initialization logic with asynccontextmanager and FastAPI lifespan. ([1c84ee5](https://github.com/hwakabh/random-travelers/commit/1c84ee5144b8c5abf38236e4ae0109ca894c6344))


### Bug Fixes

* **deployment:** explicitly configured replicas and regions. ([f27e306](https://github.com/hwakabh/random-travelers/commit/f27e3063fadd05e4f56c991f3083440587792bb8))

## [0.5.0](https://github.com/hwakabh/random-travelers/compare/v0.4.1...v0.5.0) (2024-12-25)


### Features

* **build:** added configs of railway. ([1efb526](https://github.com/hwakabh/random-travelers/commit/1efb526679b063b9b7da195eff0718fc06d8a05f))
* **build:** added Nixpacks configurations. ([e810f8f](https://github.com/hwakabh/random-travelers/commit/e810f8fa86ec8e870a5095abc5f114da02ca3b6a))
* **build:** enabled to configure MySQL TCP proxy ports of Railway. ([7e5e851](https://github.com/hwakabh/random-travelers/commit/7e5e851757433fd50b31401accb0a21ceafa1ea4))
* **ci:** enabled pushing image to GHCR. ([7180018](https://github.com/hwakabh/random-travelers/commit/7180018f1d4d6e1cb4d61bfdbe92fb0715249acb))
* **ci:** implemented actions of nixpacks. ([51c2021](https://github.com/hwakabh/random-travelers/commit/51c20214ffaf27ebb355907c8cf0c9eff1cabde5))
* enabled to create database for first migration. ([33aec3d](https://github.com/hwakabh/random-travelers/commit/33aec3da0a6be164bd63be4ee617553e306641cf))


### Bug Fixes

* **build:** default parameters in Makefile. ([0582a19](https://github.com/hwakabh/random-travelers/commit/0582a193240128be6d59c01e78f400c7d434c9fb))


### Dependencies

* locked minimal Python version with 3.13.0. ([64e4fab](https://github.com/hwakabh/random-travelers/commit/64e4fab7c152ee11536b10da011106412352ee11))


### Documentation

* added information about builds/deployment. ([d16a200](https://github.com/hwakabh/random-travelers/commit/d16a200a6b7046aad2d3e976c5074ecb5604cfd2))
* added instructions of sealed-secrets. ([1220a02](https://github.com/hwakabh/random-travelers/commit/1220a020739af11c60147edc4c424cc61d78a383))
* added kind-cluster setup and Kustomization. ([560e4e2](https://github.com/hwakabh/random-travelers/commit/560e4e243561449c373eb707421b01ed1e9c7eb4))

## [0.4.1](https://github.com/hwakabh/random-travelers/compare/v0.4.0...v0.4.1) (2024-07-08)


### Dependencies

* **certifi:** bumped to 2024.07.04 for fixing Trivy CVE scan. ([5ef9f9f](https://github.com/hwakabh/random-travelers/commit/5ef9f9fcb03d8702251cd3f8b2e78d3b75717967))

## [0.4.0](https://github.com/hwakabh/random-travelers/compare/v0.3.0...v0.4.0) (2024-02-19)


### Features

* **ci:** added cleanup workflow for staled images. ([892adc6](https://github.com/hwakabh/random-travelers/commit/892adc65bb50eeb6fc120d36bdab5dbac9014901))
* **ci:** added semantic PR. ([b8f73c9](https://github.com/hwakabh/random-travelers/commit/b8f73c9734897e205c76233e2f145082b529085a))

## [0.3.0](https://github.com/hwakabh/random-travelers/compare/v0.2.1...v0.3.0) (2024-01-23)


### Features

* added model/schema/crud for base for Airport instances. ([2530485](https://github.com/hwakabh/random-travelers/commit/2530485438624c46ff9594bca38e50ba65d612d0))
* added schemas for v0 API: [#66](https://github.com/hwakabh/random-travelers/issues/66). ([fefedc3](https://github.com/hwakabh/random-travelers/commit/fefedc3a423a4cbb090500ed0f0a613319bfe811))
* enabled to fetch URL path dynamically for v0 API. ([1e10540](https://github.com/hwakabh/random-travelers/commit/1e10540be102a0c2b42867ab473e6ecb76f9a80c))


### Bug Fixes

* **seeds:** updated SQL for generic uses. ([ae8a3d6](https://github.com/hwakabh/random-travelers/commit/ae8a3d63f5768f2bdf869943271188dce48b69ac))


### Documentation

* updated notes for directory structures. ([4c65538](https://github.com/hwakabh/random-travelers/commit/4c655384f9a2509bd7949a1776fe3b2f0384b509))

## [0.2.1](https://github.com/hwakabh/random-travelers/compare/v0.2.0...v0.2.1) (2024-01-19)


### Bug Fixes

* Query strings for restcounties.com and key to access response. ([0d6fec8](https://github.com/hwakabh/random-travelers/commit/0d6fec8f3530fac4400a47e3ac725561e00a3053))


### Documentation

* added descriptions of API key. ([8f06800](https://github.com/hwakabh/random-travelers/commit/8f06800b64597d7d7b326e251addbdcd091b8902))

## [0.2.0](https://github.com/hwakabh/random-travelers/compare/v0.1.1...v0.2.0) (2024-01-18)


### Features

* enabled to fetch JavaScript contexts via backend for security: [#40](https://github.com/hwakabh/random-travelers/issues/40). ([12d6d2f](https://github.com/hwakabh/random-travelers/commit/12d6d2f762431ad73736138f6034a75364f3627c))


### Bug Fixes

* Go templates syntax with docker command. ([73ad8ec](https://github.com/hwakabh/random-travelers/commit/73ad8eca4d1390ac958cfda8ffd4e05d6f23cfd5))
* minor changes ([6580da1](https://github.com/hwakabh/random-travelers/commit/6580da1a9f0c07344612e4651e8e30f323934291))
* minor changes. ([92108ef](https://github.com/hwakabh/random-travelers/commit/92108ef78a5b295852ca12546caea3bc63ee9e54))
* modified config file path for jobs. ([1bf5a24](https://github.com/hwakabh/random-travelers/commit/1bf5a24d6f080c5fb01b5278588fa9bef8cd64c9))
* updated logics of readiness probes. ([9e619a1](https://github.com/hwakabh/random-travelers/commit/9e619a19ca09382710586af1a495d91e55dff1d3))


### Documentation

* added make command to README.md ([e7c0ec1](https://github.com/hwakabh/random-travelers/commit/e7c0ec1486e865c6c8a3ca68cda5482be47e7bb5))

## [0.1.1](https://github.com/hwakabh/random-travelers/compare/v0.1.0...v0.1.1) (2024-01-09)


### Bug Fixes

* removed unexpected inputs. ([b442b2c](https://github.com/hwakabh/random-travelers/commit/b442b2c86c8c68ca82718063d4003bfe46ab4c05))
* Update labeler.yml ([7734d16](https://github.com/hwakabh/random-travelers/commit/7734d16e689b4f4eff50aaecd78a238f9dec6b4b))
* used proper URL path for API call. ([4ee955b](https://github.com/hwakabh/random-travelers/commit/4ee955b3e1c43f59154917386103badde36ca3f7))


### Documentation

* added descriptions of prerequisites. ([c2f75e1](https://github.com/hwakabh/random-travelers/commit/c2f75e1a67fd7d1340c10b1a0722b217295f842f))

## 0.1.0 (2024-01-08)


### Features

* **ui:** implemented mako templates and enabled render as HTML. ([13e7455](https://github.com/hwakabh/random-travelers/commit/13e745538a789bc3aed39458c173f0365ae55271))


### Bug Fixes

* **ci:** renamed labeler config file name with .yml. ([d632a47](https://github.com/hwakabh/random-travelers/commit/d632a47fe2badf675d5e19fc577623caf65824b0))
* removed jsonify() since Flask have not imported any more. ([dfaacbc](https://github.com/hwakabh/random-travelers/commit/dfaacbc28ae4a0c844ecf73247a79cf4e701411c))
* updated configs with v5 syntax. ([456c1bc](https://github.com/hwakabh/random-travelers/commit/456c1bcdd43c5f6e6980f10fcb64c22feca6de6c))
* updated configs with v5 syntax. ([a53275b](https://github.com/hwakabh/random-travelers/commit/a53275b829b077f77a058f140da74a81fad5e1a1))
* updated external links, local port, DB default credentials. ([0d61bf0](https://github.com/hwakabh/random-travelers/commit/0d61bf0df951363d33f617dddbd8b4462cddd319))


### Documentation

* added GitHub links of bitnami/mysql. ([3c4017e](https://github.com/hwakabh/random-travelers/commit/3c4017e30723028454081dcdc3816f273c87a9f9))
* updated procedures to run local. ([7a08127](https://github.com/hwakabh/random-travelers/commit/7a0812750537b772206b2fd9a5962ed6b9ab2ef3))
