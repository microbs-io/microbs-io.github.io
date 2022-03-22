# [](concepts)Concepts

Here are the definitions of common terms that you will find in microbs.


## [](cli)CLI

microbs provides a [command-line interface (CLI)](/docs/usage/cli) to
[setup](/docs/usage/cli#setup), [rollout](/docs/usage/cli#rollout), and
[destroy](/docs/usage/cli#destroy) your microbs environment. That environment
includes your choice of a [Kubernetes](#kubernetes) cluster, an
[application](#applications) that runs in the cluster, an
[observability](#observability) solution that monitors both the application and
the cluster, and an [alerting](#alerting) destination.


## [](applications)Applications

Applications ("apps") are bundled [microservices](#microservices) that microbs
deploys to [Kubernetes](#kubernetes) and instruments for [observability](#observability).
See the [ecommerce](/docs/apps/ecommerce) application as one example.


## [](variants)Variants

Variants are simulated issues that you can rollout to your [applications](#applications).
Examples might include code syntax errors, traffic spikes, networking
misconfigurations, or anything else that changes the behavior of the application
in an undesired way. Variants allow you to test the efficacy of the
[observability](#observability) solution. You can ask yourself, "Do I see my
expected alerts when this variant runs? Can I use my observability solution
to identify the root cause of the variant?"


## [](kubernetes)Kubernetes

microbs deploys applications to [Kubernetes](https://kubernetes.io/) ("k8s"),
the industry standard for container orchestration and microservices. You can
configure microbs to deploy to a Kubernetes cluster using one of the
[Kubernetes plugins](/docs/plugins/kubernetes).


## [](observability)Observability

Observability solutions capture information about the state of an application
and its supporting infrastructure over time. That information can include logs,
metrics, traces, probes, and synthetics checks. microbs instruments your chosen
[application](#applications) and [Kubernetes](#kubernetes) cluster with your
choice of an observability solution using one of the
[observability plugins](/docs/plugins/observability).

## [](microservices)Microservices

Microservices (or "services") are processes that run on [Kubernetes](#kubernetes)
and constitute part of an [application](#applications). microbs treats an
application as a set of services, each of which is implemented as a Kubernetes
[pod](https://kubernetes.io/docs/concepts/workloads/pods/).


## [](synthetics)Synthetics

Synthetics are human-like traffic sent to your [applications](#applications).
An application may or may not implement a synthetics service. For example, the
[ecommerce](/docs/apps/ecommerce) application generates virtual user traffic
that runs the steps needed to order a product.


## [](alerts)Alerts

Alerts are notifications of undesired or unusual behaviors of [applications](#applications)
or their supporting infrastructure. microbs will implement alerts to allow
realistic troubleshooting of [variants](#variants).

|! microbs has not fully implemented any alerts plugins yet.
