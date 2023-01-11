example netjsonconfig backend
==============================

This repository provides the example code behind the [create your backend](https://netjsonconfig.readthedocs.io/en/latest/backends/create_your_backend.html) page for netjsonconfig.

This example code shows how to write python classes derived from the one in netjsonconfig to add
a new configuration output format to netjsonconfig. This feature is important for the following use-cases.

1. You want a new configuration format and you don't want to contibute to netjsonconfig.
2. You are experimenting with a new configuration format and it's not ready to be merged in netjsonconfig.

This python package can be installed where netjsonconfig is present and it will add
a [backend](https://netjsonconfig.readthedocs.io/en/latest/general/basics.html#backend) called `ExampleBackend` to the available one.
