# [](cli)CLI

## Commands

* [`setup`](#setup)
* [`rollout`](#rollout)
* [`stabilize`](#stabilize)
* [`destroy`](#destroy)
* [`validate`](#validate)
* [`apps`](#apps)
* [`plugins`](#plugins)
* [`help`](#help)

See also: [Global options](#global-options)


### [](setup)`setup`

Usage: `microbs setup [OPTIONS]`

Creates all or part of the microbs environment as configured in the
`deployment.app` and `deployment.plugins*` configuration fields.

If you specify the `--app`, `--k8s`, `--obs`, or `--alerts` command flags, then
microbs will only attempt to setup those specified components. Otherwise,
microbs will attempt to setup all components. If microbs finds that a component
has already been setup, then microbs will avoid duplicating its setup.

microbs attempts to setup components in a specific order to account for their
dependencies, regardless of the order you specify in the command. That order is:

1. [Alerts plugin](/docs/plugins/alerts) (configured in [`deployment.plugins.alerts`](/docs/usage/configuration#deployment.plugins.alerts))
2. [Kubernetes plugin](/docs/plugins/kubernetes) (configured in [`deployment.plugins.k8s`](/docs/usage/configuration#deployment.plugins.k8s))
3. [Observability plugin](/docs/plugins/observability) (configured in [`deployment.plugins.obs`](/docs/usage/configuration#deployment.plugins.obs))
4. [Application](/docs/apps) (configured in [`deployment.app`](/docs/usage/configuration#deployment.app))

#### Optional command flags

|Short|Long|Description|
|-----|----|-----------|
|`-a`|`--app`|Rollout the application to Kubernetes|
|`-k`|`--k8s`|Run the `setup()` command of the Kubernetes plugin|
|`-o`|`--obs`|Run the `setup()` command of the observability plugin|
|`-l`|`--alerts`|Run the `setup()` command of the alerts plugin|


### [](rollout)`rollout`

Usage: `microbs rollout [VARIANT_NAME] [OPTIONS]`

Rolls out a [variant](/docs/overview/concepts/#variants) (`VARIANT_NAME`) of the
application deployed to Kubernetes. If no variant name is given, then the
default `main` profile of the application is rolled out to Kubernetes, which is
the same thing as deploying the application via [`setup`](#setup).


### [](stabilize)`stabilize`

Usage: `microbs stabilize [OPTIONS]`

An alias for [`microbs rollout main [OPTIONS]`](#rollout). Returns a deployed
application to its `main` profile.


### [](destroy)`destroy`

Usage: `microbs destroy [OPTIONS]`

Destroys all or part of the microbs environment as configured in the
`deployment.app` and `deployment.plugins*` configuration fields.

If you specify the `--app`, `--k8s`, `--obs`, or `--alerts` command flags, then
microbs will only attempt to destroy those specified components. Otherwise,
microbs will attempt to destroy all components.

microbs attempts to destroy components in a specific order to account for their
dependencies, regardless of the order you specify in the command. That order is:

1. [Application](/docs/apps) (configured in [`deployment.app`](/docs/usage/configuration#deployment.app))
2. [Alerts plugin](/docs/plugins/alerts) (configured in [`deployment.plugins.alerts`](/docs/usage/configuration#deployment.plugins.alerts))
3. [Observability plugin](/docs/plugins/observability) (configured in [`deployment.plugins.obs`](/docs/usage/configuration#deployment.plugins.obs))
4. [Kubernetes plugin](/docs/plugins/kubernetes) (configured in [`deployment.plugins.k8s`](/docs/usage/configuration#deployment.plugins.k8s))

#### Optional command flags

|Short|Long|Description|
|-----|----|-----------|
|`-a`|`--app`|Remove the application from Kubernetes|
|`-k`|`--k8s`|Run the `destroy()` command of the Kubernetes plugin|
|`-o`|`--obs`|Run the `destroy()` command of the observability plugin|
|`-l`|`--alerts`|Run the `destroy()` command of the alerts plugin|


### [](validate)`validate`

Usage: `microbs validate [OPTIONS]`

Validates the installation and configuration of microbs, and reports the status
of each validation check. Offers guidance where possible.

The scope of the `validate` command includes:

* Software dependency installation
* Software dependency versions
* Config file existence
* Config file syntax
* Config file values


### [](apps)`apps`

Usage: `microbs apps [OPTIONS]`

Displays a list of [apps](/docs/apps) available to microbs.


### [](plugins)`plugins`

Usage: `microbs plugins [OPTIONS]`

Displays a list of [plugins](/docs/plugins) available to microbs.


### [](help)`help`

Usage: `microbs help [OPTIONS]`

Displays a concise explanation of commands and options available to the CLI.


## [](global-options)Global options

These options can be used for all commands.

|Short|Long|Description|
|-----|----|-----------|
|`-c`|`--config`|Path to [config file](/docs/usage/configuration) (default: `./config.yaml`)|
|`-L`|`--log-level`|Filter logs by: `debug`, `info`, `warn`, `error` (default: `info`)|
||`--no-color`|Disable colors in log messages|
|`-v`|`--verbose`|Include timestamps and log levels in logs|
