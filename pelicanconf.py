#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#pylint: disable=missing-docstring
from __future__ import unicode_literals
from platform import system
from os import environ
from os.path import expanduser, join, dirname

SYSTEM = system()

AUTHOR = 'Ali Ghahraei'
SITENAME = 'Ali Ghahraei Figueroa'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Monterrey'

DEFAULT_LANG = 'en'

USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
IGNORE_FILES = ['.#*', '__pycache__']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/AliGhahraei'),
    ('GitLab', 'https://gitlab.com/AliGhahraei'),
    ('LinkedIn', 'https://www.linkedin.com/in/ali-ghahraei-figueroa-89836091/'),
)


#Theme
USER_THEME_PATH = expanduser(environ['PELICAN_THEMES_PATH'])
THEME_NAME = 'nest'
THEME = join(USER_THEME_PATH, THEME_NAME)

NEST_CSS_MINIFY = True
NEST_INDEX_HEAD_TITLE = 'Homepage'
NEST_INDEX_HEADER_TITLE = 'Me + programming'
NEST_INDEX_HEADER_SUBTITLE = 'My small corner of the internet'
NEST_INDEX_CONTENT_TITLE = 'Recent Posts'


# Plugins
PLUGIN_PATHS = [expanduser(environ['PELICAN_PLUGINS_PATH'])]
PLUGINS = ['org_reader']

ORG_READER_EMACS_LOCATION = ('/Applications/Emacs.app/Contents/MacOS/Emacs' if SYSTEM == 'Darwin'
                             else '/usr/bin/emacs')
ORG_READER_EMACS_SETTINGS = join(dirname(__file__), 'export-settings.el')
