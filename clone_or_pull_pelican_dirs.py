#!/usr/bin/env python3
"""Setup up pelican directories (currently themes and plugins) in CI"""
from os import environ
from os.path import dirname

from sh import cd, git, mkdir, rm

from publishconf import THEME_NAME, THEME_REMOTE


ORIGINAL_DIR = dirname(__file__)
THEMES_PATH = environ["PELICAN_THEMES_PATH"]
PLUGINS_PATH = environ["PELICAN_PLUGINS_PATH"]


def clone_or_pull(repo_name, url, rm_on_clone=False):
    """Clone or pull a given repository and optionally delete folder contents when cloning.

    If the repository ``repo_name`` already exists locally, perform a normal git pull. If it
    doesn't exist, clone ``url`` and optionally delete files in the directory. This could be useful
    if the repository often changes (programmatically determined, selected, etc.) and previously
    cloned repositories are now obsolote.

    :param repo_name: Repository to be operated on
    :param url: URL to be used if cloning is needed
    :param rm_on_clone: whether to delete files in the current directory when cloning
    """
    print(f'Clone or pull {repo_name}')

    try:
        cd(repo_name)
    except FileNotFoundError:
        if rm_on_clone:
            rm('-rf', '*')
        git('clone', url, repo_name, _fg=True)
    else:
        git('pull', _fg=True)


if __name__ == '__main__':
    mkdir('-p', THEMES_PATH)
    cd(THEMES_PATH)
    clone_or_pull(THEME_NAME, THEME_REMOTE, rm_on_clone=True)
    cd(ORIGINAL_DIR)

    clone_or_pull(PLUGINS_PATH, 'https://github.com/getpelican/pelican-plugins/')
    cd(ORIGINAL_DIR)
