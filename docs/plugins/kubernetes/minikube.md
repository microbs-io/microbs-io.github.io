# minikube plugin


## Contents

* [Usage](#usage)
* [Prerequisites](#prerequisites)
* [Configuration](#configuration)


## [](usage)Usage

This section documents the behavior of the `minikube` plugin when using the [`CLI`](/docs/usage/cli).

Before using the `minikube` plugin you must have its [prerequisites](#prerequisites).

### `setup`

When running [`microbs setup [--k8s]`](/docs/usage/cli/#setup), the `minikube`
plugin runs `minikube start`.

Currently, the `minikube` plugin does not configure the size of the cluster it
deploys. If you find that you need more capacity, [destroy](#/docs/usage/cli#destroy)
your current cluster and run:

```text
minikube config set memory NUM_MB && \
minikube config set cpus NUM_CPUS
```

### `rollout`

The `minikube` plugin is unaffected by [`microbs rollout`](/docs/usage/cli#rollout).

### `destroy`

When running [`microbs setup [--k8s]`](/docs/usage/cli/#destroy), the `minikube`
plugin runs `minikube delete`.


## [](prerequisites)Prerequisites


### Install dependencies

The `minikube` plugin requires the following software dependencies on the same machine as microbs:

|Software|Version|
|------|-----|
|[minikube](https://kubernetes.io/docs/tasks/tools/#minikube)|1.25.2|


## [](configuration)Configuration

Currently, the `minikube` plugin does not have any configurable settings.
