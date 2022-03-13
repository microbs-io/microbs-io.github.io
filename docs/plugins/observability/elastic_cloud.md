# elastic_cloud plugin


## Contents

* [Usage](#usage)
* [Prerequisites](#prerequisites)
* [Configuration](#configuration)


## [](usage)Usage

This section documents the behavior of the `elastic_cloud` plugin when using
the [`CLI`](/docs/usage/cli).

Before using the `elastic_cloud` plugin you must have its [prerequisites](#prerequisites).


### `setup`

|! Elastic will charge you for your use of Elastic Cloud after a 14-day free trial ([more info](https://www.elastic.co/elasticsearch/service)).


When running [`microbs setup [--obs]`](/docs/usage/cli/#setup), the
`elastic_cloud` plugin creates an Elastic Cloud deployment using the
[Elastic Cloud API](https://www.elastic.co/guide/en/cloud/current/Deployment_-_CRUD.html#create-deployment). Then it deploys `filebeat`, `metricbeat`, and `heartbeat` services to the Kubernetes cluster. These agents autodiscover logs
and metrics from the Kubernetes nodes and pods and ships that data to the
Elastic Cloud deployment.

### `rollout`

The `elastic_cloud` plugin is unaffected by [`microbs rollout`](/docs/usage/cli#rollout).

### `destroy`

When running [`microbs destroy [--obs]`](/docs/usage/cli/#destroy), the
`elastic_cloud` plugin destroys your Elastic Cloud deployment using the
[Elastic Cloud API](https://grafana.com/docs/grafana-cloud/reference/cloud-api/#delete-stack).
It also removes the services that were deployed to Kubernetes
during `setup`.


## [](prerequisites)Prerequisites


### Create Elastic Cloud resources

You must create an [Elastic Cloud account](https://cloud.elastic.co/registration)
and obtain an [Elastic Cloud API Key](https://www.elastic.co/guide/en/cloud/current/ec-api-authentication.html)
before using the `elastic_cloud` plugin.


## [](configuration)Configuration

This section documents the `elastic_cloud` plugin configurations for [config.yaml](/docs/usage/configuration).

### Required fields

#### [](plugins.elastic_cloud.api_key)`plugins.elastic_cloud.api_key`

The value of your [Elastic Cloud API Key](https://www.elastic.co/guide/en/cloud/current/ec-api-authentication.html).

Example: `VnVhQ2ZHY0JDZGJrUW0tZTVhT3g6dWkybHAyYXhUTm1zeWFrdzl0dk5udw==`

#### [](plugins.elastic_cloud.region)`plugins.elastic_cloud.region`

The name of the region in which to deploy your Elastic Cloud deployment.

See the
[available regions](https://www.elastic.co/guide/en/cloud/current/ec-reference-regions.html)
for a list of acceptable values.

Examples: `gcp-us-east1`, `ap-east1`, `westeurope`

#### [](plugins.elastic_cloud.version)`plugins.elastic_cloud.version`

The version of the Elastic Stack to deploy.

Examples: `8.0.0`
