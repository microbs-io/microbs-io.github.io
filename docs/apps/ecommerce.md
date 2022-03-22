# [](ecommerce)ecommerce

The `ecommerce` app simulates an ecommerce website.

## Services

Unless otherwise noted, these services are implementations of the
[`python-flask`](/docs/apps/templates) template service.

### [api-gateway](https://github.com/microbs-io/microbs/tree/main/apps/ecommerce/services/api-gateway)

The `api-gateway` service is an [Nginx](https://www.nginx.com/) proxy instrumented
with the [OpenTelemetry C++ nginx module](https://github.com/open-telemetry/opentelemetry-cpp-contrib/tree/main/instrumentation/nginx).
This is an implementation of the [`nginx`](/docs/apps/templates) template service.

Most services in the `ecommerce` app communicate with each other through the
`api-gateway` service. This simplifies the microservices topology by requiring
the services to be aware of only one service (in most cases). It also creates a
predictable flow of communications among services, and in theory, a single
place to manage access among services.

There are exceptions in which communications don't flow through the `api-gateway`
service:

* The `web-gateway` server communicates directly with the `session-data` service in addition to the `api-gateway` service.
* The `web-gateway` client communicates directly with the `web-gateway` server.
* The `content` service communicates with a public-internet GCP storage bucket to fetch images.
* The `synthetics` service communicates directly with the `web-gateway` client.

### [cart-data](https://github.com/microbs-io/microbs/tree/main/apps/ecommerce/services/cart-data)

The `cart-data` service stores the products and quantities of carts for each
session. The service is a [redis](https://redis.io/) server configured with a
replica service (`cart-data-replica`) for high availability.

### [cart](https://github.com/microbs-io/microbs/tree/main/apps/ecommerce/services/cart)

The `cart` service creates, reads, updates, and deletes carts and products in
the `cart-data` service via the `api-gateway` service.

### [checkout](https://github.com/microbs-io/microbs/tree/main/apps/ecommerce/services/checkout)

The `checkout` service processes payments and, if successful, clears the cart.
It communicates with the `payment` and `cart` services via the `api-gateway`
service.

### [content](https://github.com/microbs-io/microbs/tree/main/apps/ecommerce/services/content)

The `content` service fetches product images from a public-internet GCP bucket
that hosts images for the `ecommerce` microbs app.

### [payment](https://github.com/microbs-io/microbs/tree/main/apps/ecommerce/services/payment)

The `payment` service simulates the processing of a payment. Currently it does
this by waiting for a random period of time before returning an acknowledgement.

### [product-data](https://github.com/microbs-io/microbs/tree/main/apps/ecommerce/services/product-data)

The `product-data` service is a product catalog that stores data about each
product. The service is a [PostgreSQL](https://www.postgresql.org/) database.

### [product](https://github.com/microbs-io/microbs/tree/main/apps/ecommerce/services/product)

The `product` service queries product data from the `product-data` service.

### [session-data](https://github.com/microbs-io/microbs/tree/main/apps/ecommerce/services/session-data)

The `session-data` service stores session cookie identifiers that the
`web-gateway` service uses to establish and persist session state. The service
is a [redis](https://redis.io/) server configured with a replica service
(`session-data-replica`) for high availability.

### [synthetics](https://github.com/microbs-io/microbs/tree/main/apps/ecommerce/services/synthetics)

The `synthetics` service generates traffic to the `web-gateway` client.
Currently all traffic simulates the process of adding a product to a cart and
then placing an order. The service uses [k6](https://k6.io/) to simulate virtual
user traffic.

### [web-gateway](https://github.com/microbs-io/microbs/tree/main/apps/ecommerce/services/web-gateway)

The `web-gateway` service is a web server that serves a React application and
brokers requests between the React application and the `api-gateway` service.
The `synthetics` service interacts directly with the React application.

The `web-gateway` is given an external service on port `80` on Kubernetes so
that human users can interact with the application.
