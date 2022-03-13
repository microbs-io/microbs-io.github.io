# grafana_cloud plugin


## Contents

* [Usage](#usage)
* [Prerequisites](#prerequisites)
* [Configuration](#configuration)


## [](usage)Usage

This section documents the behavior of the `grafana_cloud` plugin when using
the [`CLI`](/docs/usage/cli).

Before using the `grafana_cloud` plugin you must have its [prerequisites](#prerequisites).


### `setup`

|! Grafana Cloud has a free tier that works for most usage of microbs ([more info](https://grafana.com/pricing/)).


When running [`microbs setup [--obs]`](/docs/usage/cli/#setup), the
`grafana_cloud` plugin creates a Grafana Cloud stack using the
[Grafana Cloud API](https://grafana.com/docs/grafana-cloud/reference/cloud-api/#create-stack).
Then it deploys a `grafana-agent` service to the Kubernetes cluster. This agent
autodiscovers logs and metrics from the Kubernetes nodes and pods, and collects
OpenTelemetry traces and metrics from the application running on Kubernetes, and
ships that data to the Grafana Cloud stack.

### `rollout`

The `grafana_cloud` plugin is unaffected by [`microbs rollout`](/docs/usage/cli#rollout).

### `destroy`

When running [`microbs destroy [--obs]`](/docs/usage/cli/#destroy), the
`grafana_cloud` plugin destroys your Grafana Cloud stack using the
[Grafana Cloud API](https://grafana.com/docs/grafana-cloud/reference/cloud-api/#delete-stack).


## [](prerequisites)Prerequisites


### Create Grafana Cloud resources

You must create a [Grafana Cloud account](https://grafana.com/auth/sign-up/create-user)
and obtain a [Grafana Cloud API Key](https://grafana.com/docs/grafana-cloud/reference/create-api-key/)
before using the `grafana_cloud` plugin.


## [](configuration)Configuration

This section documents the `grafana_cloud` plugin configurations for [config.yaml](/docs/usage/configuration).

### Required fields

#### [](plugins.grafana_cloud.api_key)`plugins.grafana_cloud.api_key`

The value of your [Grafana Cloud API Key](https://grafana.com/docs/grafana-cloud/reference/create-api-key/).

Example: `eyJrIjoiZTlkNmY5MDdjYTlmZTMxNDYxZDZmZGUwMTdhYzJhZGE5ZDE1MGI2NCIsIm4iOiJjaGFuZ2VtZSIsImlkIjo5OTk5OTl9`

#### [](plugins.grafana_cloud.org_slug)`plugins.grafana_cloud.org_slug`

The slug of your organization name as it exists on Grafana Cloud.

If you're unsure what this is, [sign in](https://grafana.com/auth/sign-in) to
Grafana Cloud and look at the value of URL after `/orgs/`:

`https://grafana.com/orgs/acmecorp`

Example: `acmecorp`

#### [](plugins.grafana_cloud.region)`plugins.grafana_cloud.region`

The slug of the region in which to deploy your Grafana Cloud stack.

See the
[available regions](https://grafana.com/api/stack-regions) and refer to the
`slug` fields for a list of acceptable values.

Examples: `us`, `eu`, `au`
