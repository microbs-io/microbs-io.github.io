# gke plugin


## Contents

* [Usage](#usage)
* [Prerequisites](#prerequisites)
* [Configuration](#configuration)


## [](usage)Usage

This section documents the behavior of the `gke` plugin when using the [`CLI`](/docs/usage/cli).

Before using the `gke` plugin you must have its [prerequisites](#prerequisites).

### `setup`

|! Google will charge you for your use of GKE ([more info](https://cloud.google.com/kubernetes-engine/pricing)).

When running [`microbs setup [--k8s]`](/docs/usage/cli/#setup), the `gke` plugin
runs `gcloud beta container clusters create`.

Currently, the `gke` plugin deploys a fixed-sized cluster in "Standard" mode
(i.e. not "Autopilot") with the following configuration:

* Machine type: `e2-highcpu-4`
* Number of nodes: 1 node for each zone in the given `region_name` (usually 3 nodes total).
* Disks: 32GB SSD Persistent Disks

### `rollout`

The `gke` plugin is unaffected by [`microbs rollout`](/docs/usage/cli#rollout).

### `destroy`

The `gke` plugin does not yet implement [`microbs destroy [--k8s]`](/docs/usage/cli/#destroy).
You can delete your GKE cluster through the standard GCP interfaces such as the
GCP UI or `gcloud`.


## [](prerequisites)Prerequisites


### Create GCP resources

You must create the following GCP resources before using the `gke` plugin:

* [Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
* [VPC network](https://cloud.google.com/vpc/docs/create-modify-vpc-networks)
* [VPC subnetwork](https://cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules)
* [Service account](https://cloud.google.com/iam/docs/service-accounts)
* [Service account key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)


### Install dependencies

The `gke` plugin requires the following software dependencies on the same
machine as microbs:

|Software|Version|
|------|-----|
|[gcloud](https://cloud.google.com/sdk/docs/install)|372.0.0|


## [](configuration)Configuration

This section documents the `gke` plugin configurations for [config.yaml](/docs/usage/configuration).

### Required fields

#### [](plugins.gke.project_name)`plugins.gke.project_name`

Name of the [project](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
in which your GKE cluster will be deployed.

Example: `acmecorp`

#### [](plugins.gke.region_name)`plugins.gke.region_name`

Name of the [region](https://cloud.google.com/compute/docs/regions-zones)
in which your GKE cluster will be deployed.
Your [VPC network](https://cloud.google.com/vpc/docs/create-modify-vpc-networks)
must support your chosen region.

See the
[available regions](https://cloud.google.com/compute/docs/regions-zones) for
acceptable values. Do NOT include the zone suffix (e.g. `-a`, `-b`, `-c`, `-d`).

Examples: `us-central1`, `asia-east1`

#### [](plugins.gke.network_name)`plugins.gke.network_name`

Name of the [VPC network](https://cloud.google.com/vpc/docs/create-modify-vpc-networks)
in which your GKE cluster will be deployed.

Example: `microbs`

#### [](plugins.gke.subnetwork_name)`plugins.gke.subnetwork_name`

Name of the [VPC subnetwork](https://cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules)
in which your GKE cluster will be deployed.

Example: `microbs-us-east1`

#### [](plugins.gke.service_account_name)`plugins.gke.service_account_name`

Name of the [service account](https://cloud.google.com/iam/docs/service-accounts)
that microbs will use to authenticate interactions with GCP.

Example: `username@acmecorp.iam.gserviceaccount.com`

#### [](plugins.gke.service_account_key_path)`plugins.gke.service_account_key_path`

Path to the [service account key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)
JSON file that microbs will use to authenticate interactions with GCP.

Example: `/path/to/my/secret/key/acmecorp-999999-49d9ba2b8b6d.json`
