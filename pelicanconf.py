#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Christian Soeller'
SITENAME = u'The Soeller Lab'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SHOW_DATE_MODIFIED = False
SHOW_ARTICLE_AUTHOR = False
USE_OPEN_GRAPH = False
PYGMENTS_STYLE = 'perldoc'

##################################
# Theme and plugins
##################################

THEME = 'themes/pelican-bootstrap3'

PLUGIN_PATHS = ['/Users/csoe002/Documents/src/pelican-plugins', 'plugins' ]
PLUGINS = ['i18n_subsites']#, 'feed_summary']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

##################################
# Static Paths and Favicons
##################################

# so we can supply our google file
READERS = {'html': None}

STATIC_PATHS = ['images', 'pdfs', 'extra/robots.txt', 'extra/google98210508b6f74207.html']
# below we pick up the various favicons that we generated using the site https://realfavicongenerator.net
# and have placed into images/favicons
EXTRA_PATH_METADATA = {}
for directory in ('extra', 'images/favicons'):
    for filename in os.listdir(os.path.join(PATH, directory)):
        EXTRA_PATH_METADATA['{}/{}'.format(directory, filename)] = {'path': filename}

# the FAVICON config variable is now only checked for True or False, not string value!
FAVICON = True

# the below way is the old way of using favicons - not functional in the modified theme
# FAVICON = 'images/faviconCS.ico'

##################################
# pages/menu setup
##################################

USE_FOLDER_AS_CATEGORY = True

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Research','/pages/research.html'),
    ('Publications','/pages/publications.html'),
    ('People','/pages/people.html'),
    ('Software', '/pages/software.html'),
    ('Openings', '/pages/openings.html'),
)

##################################
# Banner
##################################


BANNER = "images/mybanner.png"
BANNER_SUBTITLE = u"Cardiac Calcium Regulation and Nanosignalling @<a HREF=\"http://physiologie.unibe.ch/\">Physiology Bern</a>."
BANNER_ALL_PAGES = True


# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

##################################
# Sidebar settings
##################################

DISPLAY_RECENT_POSTS_ON_SIDEBAR = False

SOCIAL = (('Academic Webpage', 'https://physiologie.unibe.ch/~soeller/', 'academia'),
          ('Twitter', 'http://twitter.com/SoellerLab'),
          ('LinkedIn', 'http://www.linkedin.com/in/christian-soeller-98167676/'),
          ('ResearchGate', 'https://www.researchgate.net/profile/Christian_Soeller'),
          ('Google Scholar', 'http://scholar.google.co.uk/citations?hl=en&user=ByDRW44AAAAJ'),
          ('BitBucket', 'http://bitbucket.org/christian_soeller/'),)

#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)


CONTACT = (('Email', 'pages/contact.html#email', 'envelope'),
           ('Address', 'pages/contact.html#address', 'address-card'),
           ('Phone', 'pages/contact.html#phone', 'phone'),
           ('Directions', 'pages/contact.html#directions', 'map-marker'),)

TWITTER_WIDGET_ID = True
TWITTER_USERNAME = 'soellerlab'

#################################
# END Sidebar settings
#################################


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
