# [](configuration)Configuration

## Contents

* [Config file](#config-file)
* [Syntax](#syntax)
* [Reference](#reference)


## [](config-file)Config file

microbs is driven by a config file, named `config.yaml` by default. The repo
includes a sample config file called `config.reference.yaml`. You should copy
this file, rename it to `config.yaml`, and save it to the same directory. This
is the default file name and location that microbs uses.

### [](alternative-files)Alternative files

By default, microbs expects to use a config file named `config.yaml` in the same
directory as the `microbs` executable file, which is located in the root
directory of the [repo](https://github.com/microbs-io/microbs) that you cloned
during [installation](/docs/overview/getting-started). You can specify the path
to a different config file when running commands in the [CLI](/docs/usage/cli)
by using the `-c` or `--config` flag.

Example:

`microbs help -c /path/to/your/config.yaml`

### [](validation)Validation

You can (and should) validate the syntax and correctness of your config file by
running [`microbs validate`](/docs/usage/cli#validate). The validation script
can't provide 100% guidance, but it does a good job.


## [](syntax)Syntax

The microbs config file uses [yaml](https://yaml.org/spec/1.2.2/) syntax.

When you run a command with microbs, every field and value in `config.yaml` is
converted to an environment variable and shared with all microbs application
services on Kubernetes. Those values are stored in a Kubernetes
[Secret](https://kubernetes.io/docs/concepts/configuration/secret/) object named
`microbs-secrets`. The field names are flattened and uppercased, and dots are
replaced with underscores.

For example, the following configuration in config.yaml...

```yaml:nocopy
foo:
  bar_baz.abc: xyz
```

...would be shared with the application as the following environment variable:

```js:nocopy
FOO_BAR_BAZ_XYZ=xyz
```


## [](reference)Reference


### Required fields

#### [](deployment.name)`deployment.name`

A name for the deployment. The [plugins](/docs/plugins) that come with microbs
prefix this value with `microbs-` and use it as the name of the Kubernetes
cluster or observability solution stack. For example, if the value of
`deployment.name` is `changeme`, then the Kubernetes plugin would name the
cluster `microbs-changeme`.

#### [](deployment.app)`deployment.app`

The name of an [application](/docs/apps) to deploy
(i.e. the name of a directory in `./apps`).

#### [](deployment.plugins.k8s)`deployment.plugins.k8s`

The name of a [Kubernetes plugin](/docs/plugins/observability) to use
(i.e. the name of a directory in `./cli/src/plugins/k8s`).

#### [](deployment.plugins.obs)`deployment.plugins.obs`

The name of an [observability plugin](/docs/plugins/observability) to use
(i.e. the name of a directory in `./cli/src/plugins/obs`).

#### [](otlp.receiver.host)`otlp.receiver.host`

The OTLP gRPC destination host for the deployed application services. The
[apps](/docs/apps) and [observability](/docs/plugins/observability) plugins that
come with microbs expect this value to be `otel-collector`.

#### [](otlp.receiver.port)`otlp.receiver.port`

The OTLP gRPC destination port for the deployed application services. The
[apps](/docs/apps) and [observability](/docs/plugins/observability) plugins that
come with microbs expect this value to be `4317`.


### Optional fields

#### [](deployment.environment)`deployment.environment`

A description of the environment (e.g. `dev`, `test`, `prod`).

#### [](deployment.plugins.alerts)`deployment.plugins.alerts`

The name of an [alerts plugin](/docs/plugins/observability) to use
(i.e. the name of a directory in `./cli/src/plugins/alerts`).

#### [](docker.registry)`docker.registry`

A container image registry for the application services. This is used by the
[setup](/docs/usage/cli#setup) and [rollout](/docs/usage/cli#rollout) commands,
which passes the value to `skaffold run --default-repo=${docker.registry}`. Read the [skaffold docs](https://skaffold.dev/docs/environment/image-registries/) for more details on the behavior of this config.


### Plugin configs

Each [plugin](/docs/plugins) has its own set of configurations that are
specified in the same config file. Refer to the documentation for each plugin
that you wish to use to ensure that the plugin is properly configured.
