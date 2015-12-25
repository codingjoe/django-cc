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

1. [Quick Start Guide](CONTRIBUTING.md#Quick Start Guide)
2. [Code of Conduct](CONTRIBUTING.md#Code of Conduct)
3. [Code Style](CONTRIBUTING.md#Code Style)
4. [Documentation](CONTRIBUTING.md#Documentation)
5. [Git](CONTRIBUTING.md#Git)
6. [Releases](CONTRIBUTING.md#Releases)

## Tools
The tool belt consists of a set of tools and configuration files that ensure contributions to be aligned with the contribution guide.

### DCC
Wo make things even easier we cooked up a little tool for you called `dcc`.
It will set you up with just one simple command, so you can focus on implementing
that feature you've been thining about.

To get started just install `dcc` globally.

```bash
pip install dcc
```

If you want to get started to contribute to any package supporting Django Contributing Commons:

```
usage: dcc [-h] [-v] PACKAGE

positional arguments:
  PACKAGE     name of the pypi package

optional arguments:
  -h, --help  show this help message and exit
  -v          verbose mode (default: off)
```

So if you want to write a feature for django-select2, just type:
```bash
$ dcc django-select2
```

#### DCC for maintainers
Supporting DCC is easy, all you need to do is set the `download_url` to you Github repository in your `setup.py` file.

e.g.
```python
setup(
    name='dcc',
    
    download_url='https://github.com/codingjoe/django-cc',
    
    packages=find_packages(),
)
```

Make sure to put all your development requirements in the `requirements-dev.txt` file.

### [EditorConfig]
EditorConfig helps developers define and maintain consistent coding styles between different editors and IDEs. [[1]][EditorConfig]

EditorConfig enables contributors to align their code with the guideline while writing it.

The example file includes all file types defined in the contribution including the [isort](#isort) config.

### [isort][isort]
isort your python imports for you so you don't have to. [[2]][isort]

isort is configured in the [pre-commit][pre-commit-config.yaml], [setup.cfg] and [editorconfig].

### [flake8][flake8]
Flake8 is a wrapper around these tools: [[3]][flake8]
- [PyFlakes](https://launchpad.net/pyflakes)
- [pep8](https://github.com/jcrocholl/pep8)
- Ned Batchelder's [McCabe](http://nedbatchelder.com/blog/200803/python_code_complexity_microtool.html) script

Additionally the [setup.cfg] file make use of [pep8-naming](https://github.com/flintwork/pep8-naming), an flake8 extension, that checks for pep8 conform naming.

### [pep257][pep257]
pep257 checks doc strings with their compliance with [PEP 257](https://www.python.org/dev/peps/pep-0257/).

### [pre-commit][pre-commit]
A framework for managing and maintaining multi-language pre-commit hooks. [[4]][pre-commit]

[pre-commit]: (http://pre-commit.com/)
[editorconfig]: examples/.editorconfig
[isort]: (https://github.com/timothycrosley/isort)
[flake8]: (https://flake8.readthedocs.org/en/latest/)
[pep257]: (https://github.com/GreenSteam/pep257)
[setup.cfg]: examples/setup.cfg
[pre-commit-config.yaml]: examples/.pre-commit-config.yaml
