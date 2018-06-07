#!/usr/bin/env python3
from os import environ
from os.path import dirname

from sh import cd, git, mkdir, rm

from .publishconf import THEME_NAME, THEME_REMOTE


ORIGINAL_DIR = dirname(__file__)
THEMES_PATH = environ["PELICAN_THEMES_PATH"]
PLUGINS_PATH = environ["PELICAN_PLUGINS_PATH"]


mkdir('-p', THEMES_PATH)
cd(THEMES_PATH)
clone_or_pull(THEME_NAME, THEME_REMOTE, rm_on_clone=True)
cd(ORIGINAL_DIR)

clone_or_pull(PLUGINS_PATH, 'https://github.com/getpelican/pelican-plugins/')
cd(ORIGINAL_DIR)


def clone_or_pull(repo_name, url, rm_on_clone=False):
    try:
        cd(repo_name)
    except FileNotFoundError:
        if rm_on_clone:
            rm('-rf', '*')
        git('clone', url, repo_name)
    else:
        git('pull')
