# [](plugin-development)Plugin Development

* [Introduction](#intro)
  * [What is a microbs plugin?](#intro.what-is-a-microbs-plugin)
* [Plugin types](#plugin-types)
  * [`kubernetes`](#plugin-types.kubernetes)
  * [`observability`](#plugin-types.observability)
  * [`alerts`](#plugin-types.alerts)
* [Configuration](#configuration)
* [Requirements](#requirements)
  * [package.json](#requirements.package.json)
  * [Versioning](#requirements.versioning)
* [Functions](#functions)
  * [Overview](#functions.overview)
  * [Commands](#functions.commands)
    * [`setup`](#functions.commands.setup)
    * [`rollout`](#functions.commands.rollout)
    * [`destroy`](#functions.commands.destroy)
    * [`validate`](#functions.commands.validate)
  * [Hooks](#functions.hooks)
* [Tests](#tests)


## [](intro)Introduction

### [](intro.what-is-a-microbs-plugin)What is a microbs plugin?

A microbs plugin manages either the Kubernetes cluster, the observability
solution, or the alerts destination of the microbs deployment. microbs users can
install their choice of plugins and use them to run their microbs deployment
that serves their purposes.

More specifically, a microbs plugin is a Node.js package that implements the
functionality of microbs [commands](#functions.commands) and [lifecycle hooks](#functions.hooks).
The microbs CLI manages these Node.js packages using `npm`, which is simplified
by the use of the `microbs plugins` command.


## [](plugin-types)Plugin types

A microbs plugin belongs to one of the following plugin types:

### [](plugin-types.kubernetes)`kubernetes`

A `kubernetes` plugin creates and manages the Kubernetes cluster that the
microbs application will run in.

Users declare their choice of a `kubernetes` plugin in `config.yaml` here:

```yaml
deployment.plugins.kubernetes: PLUGIN_NAME
```

### [](plugin-types.observability)`observability`

An `observability` plugin creates and manages the observability solution that
monitors both the Kubernetes cluster and the microbs application.

Users declare their choice of an `observability` plugin in `config.yaml` here:

```yaml
deployment.plugins.observability: PLUGIN_NAME
```

### [](plugin-types.alerts)`alerts`

An `alerts` plugin creates and manages the alerting destination to which the
observability solution publishes alerts.

Users declare their choice of an `alerts` plugin in `config.yaml` here:

```yaml
deployment.plugins.alerts: PLUGIN_NAME
```


## [](configuration)Configuration

Each plugin must be configured in `config.yaml` under the `deployment.plugins`
section as follows:

```yaml
deployment:
  plugins:
    PLUGIN_NAME:
      KEY: VALUE,
      ...
```

Example:

```yaml
deployment:
  plugins:
    grafana-cloud:
      api_key: my-api-key
      org_slug: test
      region: us
```

Plugins have read-only access to the entire config object that the microbs CLI
parses from `config.yaml`. Plugins can read from the config object using
`config.get()` from `@microbs.io/core`.


## [](requirements)Plugin requirements

A microbs plugin is a Node.js package and must be compatible with `npm`.

### [](requirements.package.json)package.json

Plugins must conform to these requirements in `package.json`:

* `"name"` must start with `plugin-` or `@microbs.io/plugin-`
* `"name"` must contain only lowercase letters, digits, or hyphens
* `"main"` must reference a module that exports the expected plugin functions
* `"version"` must adhere to semantic version syntax.
* `"keywords"` must contain `"microbs"` and `"plugin"`
* `"keywords"` must contain exactly one microbs plugin type: `"kubernetes"`, `"observability"`, or `"alerts"`
* `"peerDependencies"` must include `"@microbs.io/core"`

Plugins also should conform to these best practices in `package.json`, though they are not required:

* `"license"` should be provided
* `"repository"` should be provided
* `"description"` should be `"microbs plugin - PLUGIN_NAME"` 
* `"scripts"` should include `"test"` which invokes `"jest"`

Here is an example of a complete, well-formed `package.json` file used by the 
[`gke`](/plugins/kubernetes/gke) plugin:

```json
{
  "name": "@microbs.io/plugin-gke",
  "version": "0.1.7-alpha",
  "description": "microbs plugin - gke",
  "license": "Apache-2.0",
  "url": "https://microbs.io/docs/plugins/kubernetes/gke/",
  "main": "./src/index.js",
  "repository": {
    "type": "git",
    "url": "https://github.com/microbs-io/microbs-plugin-gke.git"
  },
  "keywords": [
    "microbs",
    "plugin",
    "kubernetes",
    "gke"
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
  "dependencies": {
    "command-exists": "^1.2.9",
    "semver": "^7.3.5",
    "shell-quote": "^1.7.3"
  },
  "peerDependencies": {
    "@microbs.io/core": "^0.1.8-alpha"
  },
  "devDependencies": {
    "jest": "^26.6.3"
  }
}
```

### [](requirements.versioning)Versioning

Plugins must conform with the microbs [version policy](/docs/development/versioning), 
which uses semantic version syntax.


## [](functions)Functions 

### [](functions.overview)Overview

A microbs plugin is expected to implement all applicable functions documents in
this guide and export them in the root module of the package.

Example of expected usage:

```js
const plugin = require('@microbs.io/plugin-example')
plugin.setup()
plugin.destroy()
plugin.hooks.after_setup_kubernetes()
plugin.hooks.before_setup_app()
```

### [](functions.commands)Commands

Whenever the microbs CLI runs the `setup` or `destroy` commands, it calls the
`setup()` or `destroy()` function of the plugins that the user has invoked in
the command. For example, `microbs setup -ko` will invoke the `setup()` function
of the `kubernetes` and `observability` plugins specified in the `deployment.plugins.*`
fields of `config.yaml`. Running `microbs setup` without any limitaton on
plugins will call the `setup()` function of all those plugins.

Plugins are called in a specific order depending on the command being run:

* `setup` calls the `setup()` function of `alerts`, then `kubernetes`, then `observability`
* `destroy` calls the `destroy()` function of `alerts`, then `observability`, then `kubernetes`

Examples:

* `microbs setup` calls the `setup()` function of the `alerts` plugin, then the
`kubernetes` plugin, and then the `observability` plugin. It also calls any
setup [hooks](`functions.hooks`) for all plugins.
* `microbs setup -ko` calls the `setup()` function of the `kubernetes` plugin and
then the `observability` plugin. It also calls any setup [hooks](`functions.hooks`)
for all plugins.
* `microbs destroy -a` destroys the deployed application on Kubernetes. It also
calls any destroy [hooks](`functions.hooks`) for all plugins.

### [](functions.hooks)Hooks

Whenever the microbs CLI runs the `setup`, `rollout`, or `destroy` commands,
it calls optional lifecycle hooks for any plugin that implements them. This
allows plugins to perform certain necessary actions regardless of whether the
user called them or not. For example, if an `observability` plugin needs to
perform some action whenever the user runs either `microbs setup --app` or
`microbs rollout`, then the plugin could implement the `after_setup_app` and
`after_rollout` hooks to always perform that action during those commands.

Plugins are called in a specific order depending on the command being run:

* `setup` calls the hooks of `alerts`, then `kubernetes`, then `observability`
* `rollout` calls the hooks of `alerts`, then `kubernetes`, then `observability`
* `destroy` calls the hooks of `alerts`, then `observability`, then `kubernetes`

Plugins can implement any (or none) of the following hooks:

* `after_destroy_alerts()` - Runs after `microbs destroy --alerts`
* `after_destroy_app()` - Runs after `microbs destroy --app`
* `after_destroy_kubernetes()` - Runs after `microbs destroy --kubernetes`
* `after_destroy_observability()` - Runs after `microbs destroy --observability`
* `after_setup_alerts()` - Runs after `microbs setup --alerts`
* `after_setup_app()` - Runs after `microbs setup --app`
* `after_setup_kubernetes()` - Runs after `microbs setup --kubernetes`
* `after_setup_observability()` - Runs after `microbs setup --observability`
* `after_rollout()` - Runs after `microbs rollout`
* `before_destroy_alerts()` - Runs before `microbs destroy --alerts`
* `before_destroy_app()` - Runs before `microbs destroy --app`
* `before_destroy_kubernetes()` - Runs before `microbs destroy --kubernetes`
* `before_destroy_observability()` - Runs before `microbs destroy --observability`
* `before_setup_alerts()` - Runs before `microbs setup --alerts`
* `before_setup_app()` - Runs before `microbs setup --app`
* `before_setup_kubernetes()` - Runs before `microbs setup --kubernetes`
* `before_setup_observability()` - Runs before `microbs setup --observability`
* `before_rollout()` - Runs before `microbs rollout`


## [](tests)Tests

Plugins are expected to run and pass automated tests prior to release. Tests
must cover the standard [plugin requirements](#requirements) and should cover
as much other functionality as possible.
