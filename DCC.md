# DCC

## Contributing made easy

Wo make things even easier we cooked up a little tool for you called `dcc`.
It will set you up with just one simple command, so you can focus on implementing
that feature you've been thinking about.

To get started just install `dcc` globally.

```bash
pip install dcc
```

If you want to get started to contribute to any package supporting Django Contributing Commons:

```shell
usage: dcc [-h] [-v] PACKAGE

positional arguments:
  PACKAGE     name of the pypi package

optional arguments:
  -h, --help  show this help message and exit
  -v          verbose mode (default: off)
```

So if you want to write a feature for `django-select2`, just type:

```bash
dcc django-select2
```

## DCC for maintainers

Supporting DCC is easy, all you need to do is set the `download_url` to you GitHub repository in your `setup.py` file.

e.g.

```python
setup(
    name='dcc',
    
    download_url='https://github.com/codingjoe/django-cc',
    
    packages=find_packages(),
)
```

Make sure to put all your development requirements in the `requirements-dev.txt` file.
