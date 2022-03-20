# kind plugin


## Contents

* [Usage](#usage)
* [Prerequisites](#prerequisites)
* [Configuration](#configuration)


## [](usage)Usage

This section documents the behavior of the `kind` plugin when using the [`CLI`](/docs/usage/cli).

Before using the `kind` plugin you must have its [prerequisites](#prerequisites).

### `setup`

When running [`microbs setup [--k8s]`](/docs/usage/cli/#setup), the `kind`
plugin runs `kind create cluster`. Currently, the `kind` plugin does not
configure the size of the cluster it deploys.

### `rollout`

The `kind` plugin is unaffected by [`microbs rollout`](/docs/usage/cli#rollout).

### `kind`

When running [`microbs setup [--k8s]`](/docs/usage/cli/#destroy), the `kind`
plugin runs `kind delete cluster`.


## [](prerequisites)Prerequisites


### Install dependencies

The `kind` plugin requires the following software dependencies on the same machine as microbs:

|Software|Version|
|------|-----|
|[kind](https://kind.sigs.k8s.io/docs/user/quick-start/)|0.12.0|


## [](configuration)Configuration

Currently, the `kind` plugin does not have any configurable settings.
