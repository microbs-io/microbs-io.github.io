# [](getting-started)Getting Started

## [](quick-start)Quick start

You can get started with microbs in three basic steps:

1. [Prepare your environment](#step-1)
2. [Install microbs](#step-2)
2. [Configure microbs](#step-3)

Once installed and configured, you can use the [CLI](/docs/usage/cli) to run
commands with microbs.


## [](step-1)Step 1. Prepare your environment

### Operating system

microbs has been tested on **MacOS 12.1+**. Your mileage may vary on other
operating systems. Linux may work, but Windows is expected *not* to work.

### Software dependencies

|! [Plugins](/docs/plugins) may require additional dependencies. Be sure to read
the docs for the plugins you wish to use.

You will need to install [node](https://nodejs.org/en/download/),
[docker](https://docs.docker.com/engine/install/),
[kubectl](https://kubernetes.io/docs/tasks/tools/), and
[skaffold](https://skaffold.dev/docs/install/) before installing microbs.

microbs has been tested with the following software versions:

|Software|Version|
|------|-----|
|[node](https://nodejs.org/en/download/)|16.14.0|
|[docker](https://docs.docker.com/engine/install/)|20.10.12|
|[kubectl](https://kubernetes.io/docs/tasks/tools/)|1.23.4|
|[skaffold](https://skaffold.dev/docs/install/)|1.36.0|


## [](step-2)Step 2. Install microbs

Run the following command:

```sh
curl -Ls https://microbs.io/install.js | node
```

This will do a few things:

* `microbs` will be available as an executable file in your `$PATH`
* `$HOME/.microbs` will be created to store deployment information
* `$HOME/.microbs/config.yaml` will be created to configure microbs
* All [official apps and plugins](https://www.npmjs.com/~microbs.io) will be installed


## [](step-3)Step 3. Configure microbs

Open `$HOME/.microbs/config.yaml` in a text editor and complete the
[configuration](/docs/usage/configuration). Don't forget to install any
dependencies for the [plugins](/docs/plugins) you wish to use. You can run
[`microbs validate`](/docs/usage/cli#validate) to check if you have correctly
prepared the environment for your plugins.

## [](whats-next)What's next?

Once installed and [configured](/docs/usage/configuration), refer to the [CLI](/docs/usage/cli)
for an explanation of how to run microbs commands.
