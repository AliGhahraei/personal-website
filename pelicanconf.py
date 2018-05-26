#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#pylint: disable=missing-docstring
from __future__ import unicode_literals
from platform import system
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
    ('GitHub', 'https://github.com/'),
    ('LinkedIn', 'https://www.linkedin.com/in/ali-ghahraei-figueroa-89836091/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
IGNORE_FILES = ['.#*', '__pycache__']
PLUGINS = ['org_reader']


#Theme
USER_THEME_PATH = expanduser(join('~', 'g', 'pelican-themes'))
THEME_NAME = 'nest'
THEME = join(USER_THEME_PATH, THEME_NAME)

NEST_CSS_MINIFY = True
NEST_INDEX_HEAD_TITLE = 'Homepage'
NEST_INDEX_HEADER_TITLE = 'Me + programming'
NEST_INDEX_HEADER_SUBTITLE = 'My small corner of the internet'
NEST_INDEX_CONTENT_TITLE = 'Recent Posts'


# Plugins
PLUGIN_PATHS = [expanduser(join('~', 'g', 'pelican-plugins'))]
ORG_READER_EMACS_LOCATION = ('/Applications/Emacs.app/Contents/MacOS/Emacs' if SYSTEM == 'Darwin'
                             else '/usr/bin/emacs')
ORG_READER_EMACS_SETTINGS = join(dirname(__file__), 'export-settings.el')
