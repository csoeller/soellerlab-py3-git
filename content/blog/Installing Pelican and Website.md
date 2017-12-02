Title: Installing Pelican
Date: 2017-11-19 11:57
Status: draft
Slug: blog/Installing Pelican and Website
Tags: python, pelican


First I needed to add, see <https://github.com/getpelican/pelican-themes/issues/507>,

	PLUGIN_PATHS = ['path/to/plugins', ]
	PLUGINS = ['i18n_subsites', ]
	JINJA_ENVIRONMENT = {
    	'extensions': ['jinja2.ext.i18n'],
	}

to `pelicanconf.py` and install `python-gettext` using pip.

Then I also needed a patch from <https://github.com/getpelican/pelican-themes/issues/460>:

In my quick testing in local, adding this to `generators.py` fixed the problem, but I don't have enough context on the i18n use cases to know if this covers everything:

	# On line 71 in generators.py
	import gettext
	self.env.install_gettext_translations(gettext)


Note that `generators.py` is in the pelican distribution.

### Proper Fix

The proper fix though seems to be

Point the THEME variable in your pelicanconf.py to /path/to/pelican-bootstrap3 and add

	JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
	
to your Pelican configuration, as this template can be translated (see Translations below). You also need to activate a plugin that initializes the i18n jinja extension. One possibility is an up to date version of the i18n_subsites plugin:

	PLUGIN_PATHS = ['/path/to/git/pelican-plugins'] PLUGINS = ['i18n_subsites']
	
i.e. **we need to install the plugin**!
