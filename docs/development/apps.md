# [](app-development)App Development

* [Introduction](#intro)
  * [What is a microbs app?](#intro.what-is-a-microbs-app)
* [Project structure](#project-structure)
* [Requirements](#requirements)
  * [package.json](#requirements.package.json)
  * [Versioning](#requirements.versioning)
* [Observability](#observability)
  * [Logging](#observability.logging)
  * [Tracing](#observability.tracing)
  * [Liveness & Readiness](#observability.liveness-readiness)


## [](intro)Introduction

### [](intro.what-is-a-microbs-app)What is a microbs app?

A microbs app is a set of microservices that run in a Kubernetes cluster and are
monitored with an observability solution. microbs users can install their choice
of apps and use them to run their microbs deployment that serves their purposes.

More specifically, a microbs app is a Node.js package that contains the source
code and metadata for the application, which also includes Dockerfiles,
Kubernetes manifests, and a skaffold file. The application services can be
written in any programming language because they will be deployed as containers.
Node.js is required simply to publish the project and install it to microbs.
The microbs CLI manages these Node.js packages using `npm`, which is simplified
by the use of the `microbs apps` command.

## [](project-structure)Project structure

### [](project-structure.overview)Overview

```sh
./plugins
./plugins/PLUGIN_NAME
./src
./src/common
./src/services
./src/services/SERVICE_NAME
./src/services/SERVICE_NAME/k8s
./src/services/SERVICE_NAME/k8s/*.yaml
./src/services/SERVICE_NAME/src
./src/services/SERVICE_NAME/Dockerfile
./src/variants
./src/variants/VARIANT_NAME
./src/variants/VARIANT_NAME/k8s
./src/variants/VARIANT_NAME/k8s/*.yaml
./src/variants/VARIANT_NAME/src
./src/variants/VARIANT_NAME/Dockerfile
./src/skaffold.yaml
package.json
```

### [](src)`./src`

Contains the source code for the entire application.

### [](src/services)`./src/services`

Contains the source code for each service of the application.

### [](src/services/SERVICE_NAME)`./src/services/SERVICE_NAME`

Contains the source code for a single service.

### [](src/services/SERVICE_NAME/k8s)`./src/services/SERVICE_NAME/k8s`

Contains the Kubernetes manifests for a service. The [`setup`](/docs/usage/cli#setup), [`rollout`](/docs/usage/cli#rollout), and [`destroy`](/docs/usage/cli#destroy) commands invoke `skaffold run` or `skaffold delete` to apply or remove these configurations on Kubernetes. The manifests must be declared in [`./src/skaffold.yaml`](src/skaffold.yaml) under the `main` profile for the commands to apply them.

### [](src/services/SERVICE_NAME/k8s/*.yaml)`./src/services/SERVICE_NAME/k8s/*.yaml`

Contains the configuration for one or more Kubernetes resources of the service. Usually this includes a `Deployment` and a `Service`.

### [](src/services/SERVICE_NAME/src)`./src/services/SERVICE_NAME/src`

Contains the source code for a single service.

### [](src/services/SERVICE_NAME/src/Dockerfile)`./src/services/SERVICE_NAME/src/Dockerfile`

Contains the instructions to build a Docker image for the service. The [`setup`](/docs/usage/cli#setup) and [`rollout`](/docs/usage/cli#rollout) commands invoke `skaffold run` to build these images and deploy them to Kubernetes. The Dockerfiles must be declared in [`./src/skaffold.yaml`](src/skaffold.yaml) under the `main` profile for the commands to build them.

### [](src/variants)`./src/variants`

Contains the source code for each variant of the application. (Functionally equivalent to [`./src/services`](#src/services))

### [](src/variants/VARIANT_NAME)`./src/variants/VARIANT_NAME`

Contains the source code for a single variant. (Functionally equivalent to [`./src/services/SERVICE_NAME`](#src/services/SERVICE_NAME))

### [](src/variants/VARIANT_NAME/k8s)`./src/variants/VARIANT_NAME/k8s`

Contains the Kubernetes manifests for a variant. The [`rollout`](/docs/usage/cli#rollout) command invokes `skaffold run` to apply or remove these configurations on Kubernetes. The manifests must be declared in [`./src/skaffold.yaml`](src/skaffold.yaml) under a profile that is not `main` for the commands to apply them. (Functionally equivalent to [`./src/services/SERVICE_NAME/k8s`](#src/services/SERVICE_NAME/k8s))

### [](src/variants/VARIANT_NAME/k8s/*.yaml)`./src/variants/VARIANT_NAME/k8s/*.yaml`

Contains the configuration for one or more Kubernetes resources of the variant. (Functionally equivalent to [`./src/services/SERVICE_NAME/k8s/*.yaml`](#src/services/SERVICE_NAME/k8s/*.yaml))

### [](src/variants/VARIANT_NAME/src)`./src/variants/VARIANT_NAME/src`

Contains the source code for a single variant. (Functionally equivalent to [`./src/services/SERVICE_NAME/src`](#src/services/SERVICE_NAME/src))

### [](src/variants/VARIANT_NAME/src/Dockerfile)`./src/variants/VARIANT_NAME/src/Dockerfile`

Contains the instructions to build a Docker image for the variant. The [`rollout`](/docs/usage/cli#rollout) command invoke `skaffold run` to build these images and deploy them to Kubernetes. The Dockerfiles must be declared in [`./src/skaffold.yaml`](src/skaffold.yaml) under a profile that is not `main` for the commands to build them. (Functionally equivalent to [`./src/services/SERVICE_NAME/src/Dockerfile`](#src/services/SERVICE_NAME/src/Dockerfile))

### [](src/skaffold.yaml)`./src/skaffold.yaml`

Contains the configuration that `skaffold` needs to build the Docker images for the services or variants and then deploy them to Kubernetes.

### [](package.json)`package.json`

Contains metadata about the application that is required to be installed to microbs.


## [](requirements)App requirements

A microbs app is a Node.js package and must be compatible with `npm`.

### [](requirements.package.json)package.json

Apps must conform to these requirements in `package.json`:

* `"name"` must start with `app-` or `@microbs.io/app-`
* `"name"` must contain only lowercase letters, digits, or hyphens
* `"version"` must adhere to semantic version syntax.
* `"keywords"` must contain `"microbs"` and `"app"`

Plugins also should conform to these best practices in `package.json`, though they are not required:

* `"license"` should be provided
* `"repository"` should be provided
* `"description"` should be `"microbs app - APP_NAME"` 
* `"scripts"` should include `"test"` which invokes `"jest"`

Here is an example of a complete, well-formed `package.json` file used by the 
[`ecommerce`](/apps/ecommerce) app:

```json
{
  "name": "@microbs.io/app-ecommerce",
  "version": "0.1.1-alpha",
  "description": "microbs app - ecommerce",
  "license": "Apache-2.0",
  "url": "https://microbs.io/docs/apps/ecommerce/",
  "repository": {
    "type": "git",
    "url": "https://github.com/microbs-io/microbs-app-ecommerce.git"
  },
  "keywords": [
    "microbs",
    "app",
    "ecommerce"
  ],
  "scripts": {
    "test": "jest"
  },
  "jest": {
    "silent": false,
    "verbose": true
  },
  "engines": {
    "node": ">=14.16.1"
  },
  "devDependencies": {
    "@microbs.io/core": "^0.1.7-alpha",
    "jest": "^26.6.3"
  }
}
```

### [](requirements.versioning)Versioning

Apps must conform with the microbs [version policy](/docs/development/versioning), 
which uses semantic version syntax.


## [](observability)Observability

The following implementation details for logging and tracing will be compatible
with the current [observability plugins](/docs/plugins/observability).

### [](observability.logging)Logging

* Services should serialize logs using logfmt
* Services should write to `stdout`

### [](observability.tracing)Tracing

* Services should instrument with OpenTelemetry
* Services should send spans to the `otel-collector` service on Kubernetes

### [](observability.liveness-readines)Liveness & Readiness

* Services should handle `GET /healthz` and return `200 OK` with the payload `{"health":true}` and the header `Content-Type: application/json`
