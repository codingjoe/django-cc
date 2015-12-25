#!/usr/bin/env python
from distutils.spawn import find_executable

from setuptools import find_packages, setup

import dcc

if not find_executable('hub'):
    raise RuntimeError(
        '"hub" was not found.\n'
        'Please download hup at https://hub.github.com/'
    )

setup(
    name='dcc',
    version=dcc.__version__,
    description=dcc.__doc__.strip(),
    url='https://github.com/codingjoe/django-cc',
    download_url='https://github.com/codingjoe/django-cc',
    bugtrack_url='https://github.com/codingjoe/django-cc/issues',
    author=dcc.__author__,
    author_email='info@johanneshoppe.com',
    license=dcc.__licence__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dcc = dcc.__main__:main',
            'django-cc = dcc.__main__:main',
        ],
    },
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Topic :: Software Development',
        'Topic :: Software Development :: Version Control',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
)
