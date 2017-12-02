Title: New Website
Date: 2017-11-26 12:12
Modified: 2017-11-29 09:09
Status: published
Slug: news/new-site
Tags: website, python, pelican
Authors: Christian Soeller

### A new website with Pelican

We have just published our website using pelican and the bootstrap3 theme. [Pelican](http://docs.getpelican.com) is a static site generator, written in [Python](http://www.python.org/).

Going with a static site generator, rather than a database based one such as wordpress, seemed a good idea, for a few reasons:

- smaller attack surface (e.g. wordpress is regularly hacked)
- easier backup and maintenance - we keep everything in a [mercurial](https://www.mercurial-scm.org/wiki/Mercurial) repository
- it uses Python - we [use Python a lot in the lab](/pages/software.html)
- you can work on the site at any time and anywhere - you don't need to be online

There are lots of [Pelican](http://docs.getpelican.com) based academic sites which I looked
at for guidance and ideas. Most useful are those that publish their source code on
sites like github, e.g.
 [Peter Wittek's site](http://github.com/peterwittek/peterwittek.com),
 Kyle Cranmer's
 [Theory and Practice](http://github.com/cranmer/TheoryAndPractice/)
 and many more.
At some stage we might put our site on a public repository...
