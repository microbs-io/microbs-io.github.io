# [](cli)CLI

## Commands

* [`setup`](#setup)
* [`rollout`](#rollout)
* [`stabilize`](#stabilize)
* [`destroy`](#destroy)
* [`validate`](#validate)
* [`plugins`](#plugins)
* [`apps`](#apps)
* [`version`](#version)
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
2. [Kubernetes plugin](/docs/plugins/kubernetes) (configured in [`deployment.plugins.kubernetes`](/docs/usage/configuration#deployment.plugins.kubernetes))
3. [Observability plugin](/docs/plugins/observability) (configured in [`deployment.plugins.observability`](/docs/usage/configuration#deployment.plugins.observability))
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
3. [Observability plugin](/docs/plugins/observability) (configured in [`deployment.plugins.observability`](/docs/usage/configuration#deployment.plugins.observability))
4. [Kubernetes plugin](/docs/plugins/kubernetes) (configured in [`deployment.plugins.kubernetes`](/docs/usage/configuration#deployment.plugins.kubernetes))

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


### [](plugins)`plugins`

Manages microbs [plugins](/docs/plugins)

Usages:

* `microbs plugins list`
* `microbs plugins search`
* `microbs plugins install PLUGIN_NAME [...]`
* `microbs plugins update PLUGIN_NAME [...]`
* `microbs plugins uninstall PLUGIN_NAME [...]`

#### [](plugins.list)`plugins.list`

`microbs plugins list` displays the plugins installed on the same machine as the
microbs CLI.

#### [](plugins.list)`plugins.search`

`microbs plugins search` searches for official microbs plugins on the npm
registry. The names of official plugins packages are prefixed with
`@microbs.io/plugin-`.

#### [](plugins.install)`plugins.install`

`microbs plugins install PLUGIN_NAME [...]` installs one or more plugins by name
from the npm registry. microbs automatically prefixes the plugin package name
with `@microbs.io/plugin-`, thus if you wanted to install the `gke` plugin, you
would only need to run `microbs plugin install gke` and not `@microbs.io/plugin-gke`. Plugins are installed under the `node_modules` directory of the microbs
CLI.

#### [](plugins.update)`plugins.update`

`microbs plugins update PLUGIN_NAME [...]` updates one or more installed plugins
by name.

#### [](plugins.uninstall)`plugins.uninstall`

`microbs plugins uninstall PLUGIN_NAME [...]` removes one or more installed
plugins by name.


### [](apps)`apps`

Usage: `microbs apps [OPTIONS]`

Displays a list of [apps](/docs/apps) available to microbs.


### [](apps)`version`

Usage: `microbs version`

Displays the version of microbs.


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
