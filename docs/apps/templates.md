# [](templates)templates

The `templates` app is a set of basic microservices implemented in various
languages and software frameworks. You can think of each service as a simple
"hello world" program.

The purpose of the `templates` app is to test or demonstrate the essentials of
observability instrumentation for various languages and software frameworks.
Each service exhibits the same HTTP routes and behaviors, writes the same logs,
and emits the same traces with OpenTelemetry, regardless of the language or
framework of the service.

You can also copy these templates and use them as the foundation for developing
your own [custom microbs apps](/docs/development/apps). For example, you will
notice that the [`ecommerce`](/docs/apps/ecommerce) app borrows many of the
conventions from the [`python-flask`](https://github.com/microbs-io/microbs/tree/main/apps/templates/services/python-flask)
service of the `templates` app.


## Implementations

* [`nginx`](https://github.com/microbs-io/microbs/tree/main/apps/templates/services/nginx) - An [Nginx](https://www.nginx.com/) service instrumented with the [OpenTelemetry C++ nginx module](https://github.com/open-telemetry/opentelemetry-cpp-contrib/tree/main/instrumentation/nginx).
* [`python-flask`](https://github.com/microbs-io/microbs/tree/main/apps/templates/services/python-flask) - A [Python](https://www.python.org/) service using the [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework.

## Planned implementations

* `dotnet-framework`
* `go-echo`
* `java-spring`
* `nodejs-express`
