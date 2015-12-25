#!/usr/bin/env python
"""The main entry point. Invoke as ``dcc`` or ``python -m dcc``."""
import argparse
import logging
import os
import sys

from . import HUB, __doc__ as description
from .utils import get_github_url, setup_env, setup_git, target_path_exists

logger = logging.getLogger('dcc')


def check_binaries():
    """Test if ``hub`` is installed."""
    if not HUB:
        raise RuntimeError(
                '"hub" was not found.\n'
                'Please download hup at https://hub.github.com/'
        )

PROGRESS_MSG = "One {package_name}, coming right up!\n..."


SUCCESS_MSG = """
{package_name} has been forked and copied to:
{target_path}

To get started create a new feature branch using:
hub branch -d my_feature

Once you're done commit and push...
hub push --set-upstream {username} my_feature

...and create a pull-request:
hub pull-request -b {owner_name}
"""


def get_args():
    """Setup argument parser and return parsed arguments."""
    parser = argparse.ArgumentParser(
            description=description.strip()
    )
    parser.add_argument('package_name', metavar='PACKAGE', type=str,
                        help='Name of the PyPI package.')
    parser.add_argument('-v', dest='verbose', action='store_const',
                        const=logging.DEBUG, default=logging.WARNING,
                        help='verbose mode (default: off)')
    return parser.parse_args()


def main():
    """Main method that is invoked by ``dcc``."""
    args = get_args()
    package_name = args.package_name
    if target_path_exists(package_name):
        return
    print(PROGRESS_MSG.format(package_name=package_name))

    handler = logging.StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(args.verbose)

    check_binaries()
    github_url = get_github_url(package_name)
    repo_name, username, owner_name = setup_git(args.package_name, github_url)
    setup_env(repo_name)
    msg = SUCCESS_MSG.format(
        package_name=package_name,
        target_path=os.path.join(os.getcwd(), package_name),
        username=username,
        owner_name=owner_name,
    )
    print(msg)


if __name__ == '__main__':
    sys.exit(main())
