# slack plugin

|! The `slack` plugin is not yet fully implemented. Currently none of the applications that come with microbs use the `slack` plugin.


## Contents

* [Usage](#usage)
* [Prerequisites](#prerequisites)
* [Configuration](#configuration)


## [](usage)Usage

This section documents the behavior of the `slack` plugin when using
the [`CLI`](/docs/usage/cli).

Before using the `slack` plugin you must have its [prerequisites](#prerequisites).


### `setup`

When running [`microbs setup [-o]`](/docs/usage/cli/#setup), the
`slack` plugin creates a channel in your Slack Workspace.

### `rollout`

The `slack` plugin is unaffected by [`microbs rollout`](/docs/usage/cli#rollout).

### `destroy`

The `slack` plugin does not yet implement [`microbs destroy [-k]`](/docs/usage/cli/#destroy).
You can delete your channel through the standard Slack interfaces such as the
Slack UI.


## [](prerequisites)Prerequisites


### Create Slack resources

You must create a [Slack workspace](https://slack.com/get-started#/create)
and obtain a [bot access token](https://api.slack.com/authentication/token-types#bot)
before using the `slack` plugin.


## [](configuration)Configuration

This section documents the `slack` plugin configurations for [config.yaml](/docs/usage/configuration).

### Required fields

#### [](plugins.slack.bot_user_oauth_access_token)`plugins.slack.api_key`

The value of your [bot access token](https://api.slack.com/authentication/token-types#bot).

Example: `xoxb-999999999999-999999999999-gxnpd45mZZh76FzLfkpLP7Tj`
