# How to migrate to Django-CC

We put together a little guide to help you including Django-CC
into your own projects.

## Contribution Guide

To stay up to date we advice to link your contributing guide to our
latest version, because the project is very young. We will add version
tags later, that will allow you to link your contributing guide to a
fixed version.

Just add the following lines to your `CONTRIBUTING.md` file in your git root:

    # Contributing Guide [![badge](https://img.shields.io/badge/Django-CC-ee66dd.svg)][django-cc]
    This project follows the **[Django Contributing Commons][django-cc]**.

    ## Getting started
    Getting started is simple, just do:
    ```bash
    pip install dcc
    dcc {PYPI_PACKAGE}
    hub checkout -b patch-1
    ```
    
    To test locally simply run:
    ```bash
    tox
    ```

    After that just write your code. Once you are done, just follow this easy flow:
    ```bash
    hub commit
    hub pull-request -b {OWNER}
    ```

    [django-cc]: https://github.com/codingjoe/django-cc/blob/master/CONTRIBUTING.md

This will look somewhat similar to this:

> # Contributing Guide [![django-cc](https://img.shields.io/badge/Django-CC-ee66dd.svg)](django-cc)

> This project follows the **[Django Contributing Commons][django-cc]**.

> ## Getting started

> Getting started is simple, just do:
>
>     pip install dcc
>     dcc django-stdimage
>     hub checkout -b patch-1
> 
> To test locally simply run:
>
>     tox
>
> After that just write your code. Once you are done, just follow this easy flow:
>
>     hub commit
>     hub pull-request -b codingjoe
> 

## Requirements

To ensure that [`dcc`][dcc] can setup a virtualenv you will need to provide a
`requirements-dev.txt` file. This file should contain all dependencies
required to develop and test your package.

It should look similar to this:

    -e .  # install the package itself
    pytest==2.8.0
    ...

You can find an example requirements file including all tools in our
examples folder.

## Tox

To encourage contributors to test as often an early as possible, we
recommend setting up tox. We have an 
[example configuration](examples/tox.ini)
in the examples folder.
Please make sure to also provide a tox test environment
for both quality assurance and documentation tests.

[dcc]: DCC.md
[django-cc]: https://github.com/codingjoe/django-cc/blob/master/CONTRIBUTING.md
