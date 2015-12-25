"""``dcc`` utils."""
import json
import logging
import os
import subprocess
import sys

from . import BASE_DIR, HUB, PIP, VIRTUALENV, DjangoCCError

PY3 = sys.version_info[0] == 3
if PY3:
    from urllib.request import urlopen
else:
    from urllib import urlopen


logger = logging.getLogger('dcc')


PYPI_JSON_URL = "https://pypi.python.org/pypi/{package_name}/json"
GITHUB_URL = "https://github.com/{username}/{repo_name}.git"


def get_github_url(package_name):
    """Return Github url based on PYPI package information."""
    url = PYPI_JSON_URL.format(package_name=package_name)
    response = urlopen(url)
    if response.code == 404:
        raise DjangoCCError('The package "%s" does not exist.' % package_name)
    if PY3:
        body = response.read().decode('utf-8')
    else:
        body = response.read()
    data = json.loads(body)
    github_url = data['info']['download_url']
    if not github_url.startswith('https://github.com/'):
        raise DjangoCCError('The package "%s" does not support Django-CC.' % package_name)
    return github_url


def parse_github_url(url):
    """Return username and repository name base on Github url."""
    return [x for x in url.rsplit('/') if x][-2:]


def setup_git(package_name, github_url):
    """Clone git repository and setup own Github fork and remote."""
    owner_name, repo_name = parse_github_url(github_url)
    git_clone(owner_name, repo_name)
    username = get_github_username()
    try:
        logger.info("Forking...")
        logger.debug(
                subprocess.check_output([HUB, 'fork'], stderr=subprocess.STDOUT, cwd=repo_name)
        )
    except subprocess.CalledProcessError:
        logger.info("Fork already exists. Adding remote...")
        if username != owner_name:
            add_git_remote(username, repo_name)
        else:
            logger.info("%s is your own package. No remote added." % package_name)
    set_git_commit_msg(repo_name)
    return repo_name, username, owner_name


def git_clone(owner_name, repo_name):
    github_url = GITHUB_URL.format(username=owner_name, repo_name=repo_name)
    logger.info("Cloning %s" % github_url)
    output = subprocess.check_output(
            [HUB, 'clone', '-p', '-o', owner_name,
             '{}/{}'.format(owner_name, repo_name), repo_name],
            stderr=subprocess.STDOUT,
    )
    logger.debug(output)


def add_git_remote(username, repo_name):
    """Add git remote based on username."""
    logger.debug(subprocess.check_output([HUB, 'remote', 'add', '-p', username], cwd=repo_name))


def get_github_username():
    """Return Github user name."""
    output = subprocess.check_output([HUB, 'config', '--get', 'github.user'])
    username = output.strip().decode('utf-8')
    if not username:
        raise DjangoCCError(
                'You have not setup your Github username in your git config.\n'
                'You may do so by executing:\n'
                'git config --global github.user [YOUR_USERNAME]'
        )
    return username


def set_git_commit_msg(repo_name):
    """Set custom git commit message for given repository."""
    template = os.path.join(BASE_DIR, 'git_commit_msg.txt')
    output = subprocess.check_output(
                    [HUB, 'config', 'commit.template', template],
                    cwd=repo_name
            )
    logger.debug(output)


def setup_env(repo_name):
    """Set up virtual environment and install dependencies."""
    print("Setting up virtualenv...")
    logger.debug(subprocess.check_output([VIRTUALENV, 'env'], cwd=repo_name))
    print("Installing requirements...")
    logger.debug(subprocess.check_output(
            ['env/bin/python', PIP, 'install', '-r', 'requirements-dev.txt'],
            cwd=repo_name
    ))


TARGET_EXISTS_MSG = "Seems like you had one too many.\n{package_name} already exists."


def target_path_exists(package_name):
    """Test if target path is already existing."""
    target_path = os.path.join(os.getcwd(), package_name)
    if os.path.exists(target_path):
        print(TARGET_EXISTS_MSG.format(package_name=package_name))
        return True
    else:
        return False
