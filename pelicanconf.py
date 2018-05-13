#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#pylint: disable=missing-docstring
from __future__ import unicode_literals
from platform import system
from os.path import expanduser, join

SYSTEM = system()

AUTHOR = 'Ali Ghahraei Figueroa'
SITENAME = 'Ali Ghahraei Figueroa'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Monterrey'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/ali-ghahraei-figueroa-89836091/'),
          ('GitHub', 'https://github.com/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
IGNORE_FILES = ['.#*', '__pycache__']
PLUGINS = ['org_reader']


USER_THEME_PATH = expanduser(join('~', 'g'))
THEME_NAME = 'attila'
THEME = join(USER_THEME_PATH, THEME_NAME)

PLUGIN_PATHS = [expanduser(join('~', 'g', 'pelican-plugins'))]
ORG_READER_EMACS_LOCATION = ('/Applications/Emacs.app/Contents/MacOS/Emacs' if SYSTEM == 'Darwin'
                             else '/usr/bin/emacs')
