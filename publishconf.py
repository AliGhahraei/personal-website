#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#pylint: disable=missing-docstring,wildcard-import,unused-wildcard-import,wrong-import-position
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://alighahraei.gitlab.io'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Following items are often useful when publishing

DISQUS_SITENAME = "alighahraei"
#GOOGLE_ANALYTICS = ""
