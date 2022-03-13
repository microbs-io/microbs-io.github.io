# [](getting-started)Getting Started

|? 👋 Hello! microbs is a new project with an amibtious scope. Its configurations and interfaces might change until its GA release. Be sure to check these docs for changes whenever you pull the latest version of microbs. And if you like the project, consider [contributing](http://github.com/microbs-io/microbs) on GitHub!


## [](quick-start)Quick start

You can install microbs in three basic steps:

1. [Prepare your environment](#step-1)
2. [Clone the repo](#step-2)
3. [Install microbs](#step-3)

Once installed, you can proceed to the [configuration](/docs/usage/configuration) and [CLI](/docs/usage/cli).


## [](step-1)Step 1. Prepare your environment

### Operating system

microbs has been tested on **MacOS 12.1**. Your mileage may vary on other operating systems.

### Software dependencies

|! [Plugins](/docs/plugins) may require additional dependencies. Be sure to read the docs for the plugins you wish to use.

You will need to install [node](https://nodejs.org/en/download/), [nvm](https://github.com/nvm-sh/nvm), [kubectl](https://kubernetes.io/docs/tasks/tools/), and [skaffold](https://skaffold.dev/docs/install/) before installing microbs.

microbs has been tested with the following software versions:

|Software|Version|
|------|-----|
|[kubectl](https://kubernetes.io/docs/tasks/tools/)|1.23.4|
|[node](https://nodejs.org/en/download/)|17.5.0|
|[nvm](https://github.com/nvm-sh/nvm)|17.5.0|
|[skaffold](https://skaffold.dev/docs/install/)|1.36.0|


## [](step-2)Step 2. Clone the repo

```sh
git clone https://github.com/microbs-io/microbs.git
```


## [](step-3)Step 3. Install microbs

```python
# Navigate into the cloned microbs repo
cd microbs

# Use the correct version of node
nvm use

# Install the node modules for microbs
npm install

# Add the current directory to your PATH
export PATH="$(pwd):$PATH"

# Create a config file
cp ./config.reference.yaml config.yaml

# Verify installation
microbs help
```
