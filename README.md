# Django Contributing Commons (CC)
**_Django CC_ is an open tool belt making maintaining an contributing to Django packages a breeze.**

It contains a standardized contributing guide as well as various tools to automate conform code contribution.

## Preamble
This project aims to provide confidence and convenience for both contributors and maintainers.

### Goals
- Early on feedback and a shorter feedback loop.
- High and highly sustainable code quality.

## Contribution Guide
The contribution guide is the central part of the projects. All tools and example configurations aim to support following the contribution guide as easy as possible.

**Contents**
1. [Code of Conduct](CONTRIBUTING.md# Code of Conduct)

## Tools
The tool belt consists of a set of tools and configuration files that ensure contributions to be aligned with the contribution guide.

### [EditorConfig]
EditorConfig helps developers define and maintain consistent coding styles between different editors and IDEs. [[1]][EditorConfig]

EditorConfig enables contributors to align their code with the guideline while writing it.

The example file includes all file types defined in the contribution including the [isort](#isort) config.

### [isort]
isort your python imports for you so you don't have to. [[2]][isort]

isort is configured in the [pre-commit], [setup.cfg] and [editorconfig].

### [flake8]
Flake8 is a wrapper around these tools: [[3]][flake8]
- [PyFlakes](https://launchpad.net/pyflakes)
- [pep8](https://github.com/jcrocholl/pep8)
- Ned Batchelder's [McCabe](http://nedbatchelder.com/blog/200803/python_code_complexity_microtool.html) script

Additionally the [setup.cfg] file make use of [pep8-naming](https://github.com/flintwork/pep8-naming), an flake8 extension, that checks for pep8 conform naming.

### [pep257]
pep257 checks doc strings with their compliance with [PEP 257](https://www.python.org/dev/peps/pep-0257/).

### [pre-commit]
A framework for managing and maintaining multi-language pre-commit hooks. [[4]][pre-commit]

[prec-commit]: (http://pre-commit.com/)
[editorconfig]: (examples/.editorconfig)
[isort]: (https://github.com/timothycrosley/isort)
[flake8]: (https://flake8.readthedocs.org/en/latest/)
[pep257]: (https://github.com/GreenSteam/pep257)
[setup.cfg]: (examples/setup.cfg)
[pre-commit]: (examples/.pre-commit-config.yml)
