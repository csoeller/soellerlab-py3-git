#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# eventual target URL
SITEURL = 'http://soellerlab.ex.ac.uk'

# for testing via empslocal
#SITEURL = 'http://empslocal.ex.ac.uk/people/staff/soellerlab'

# for testing on my local linux box
#SITEURL = 'http://phy-lmsrv2.ex.ac.uk:8080'

# we have this for the moment so we can experiment with the blog
# in the development version without accidentally publishing it
# Note: remove once we want to publish blog entries
# ARTICLE_EXCLUDES = ['blog']

# we must prepend the siteurl to our menu links
MENUITEMS = [(entry[0], SITEURL + entry[1]) for entry in MENUITEMS] 

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
