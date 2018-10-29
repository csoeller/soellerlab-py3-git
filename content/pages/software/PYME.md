Title: Python software for super-resolution microscopy
Slug: PYME
Date: 2018-12-29 11:54
Tags: software, stuff

<img style="float:left; border-right:8px solid white" width="300"
src="{filename}/images/software/PYMEacquire.png" alt="PYME Acquire GUI
Interface"/>
The [Python Microscopy Environment](http://python-microscopy.org/) (or PYME for short) is a microscopy
software environment originally designed and implemented by our colleague and collaborator [David
Baddeley](https://unidirectory.auckland.ac.nz/profile/d-baddeley). 

David worked with us for several years, a large part of
the SMLM functionality was tested and implemented while working
together at the University of Auckland. David has continued to develop
this package and we regularly contribute code and extensions. PYME
offers a data acquisition module which performs the microscope and
camera control functionality similar to that offered by
e.g. micro-manager, but optimised for PALM/STORM type imaging. The
PYMEAcquire GUI interface is highly configurable and has backends for
a range of different hardware in terms of cameras, microscopes,
etc. We run it on a range of custom built microscopes. A major
strength is the flexible extensibility resulting from being built
within the powerful Python framework.

PYME is not limited to super-resolution microscopy. It can also deal
with various types of confocal data - it provides powerful
deconvolution and 3D visualisation tools. David has also integrated
functionally for STED data and the framework is extensible so that
just about any modality could be usefully interfaced to PYME.

## Installation instructions

For installation details go to the
[python-microscopy site](http://python-microscopy.org/). These days there are fairly simple 2-line installation
options that use the very flexible [Python Ananconda](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution))
environment. David's page provides detailed instructions
[how to get PYME](http://python-microscopy.org/doc/Installation/InstallationWithAnaconda.html)
running on your computer.

## Our PYME extensions

### PYME Site Configuration

We are maintaining several packages to configure and extend PYME functionality. Our
[Site Configuration Files](http://bitbucket.org/christian_soeller/pyme-exeter-siteconfig) provide initialisation files
and custom protocols for our acqusition systems.

### PYME plugins

PYME has a config system that allows adding plugins for the GUI applications quite easily. We have used
this recent ability of PYME in our [PYME-extra](http://bitbucket.org/christian_soeller/pyme-extra) suite of tools
where we implement both experimental and tested new functionality for PYME.

### Extending and configuring PYME for your site

The extension functionalty is provided by the PYME.config infrastructure. Read the
[PYME.config documentation](http://www.python-microscopy.org/doc/api/PYME.config.html)
and look at our usage in [PYME-extra](http://bitbucket.org/christian_soeller/pyme-extra) to get an
idea.

## PYME bitbucket repositories

We maintain several repositories on [bitbucket](http://bitbucket.org)
that contain our acquisition, analysis and control codes for various
types of microscopy.

* <i class="fa fa-bitbucket fa-lg"></i>
  [python-microscopy-exeter](http://bitbucket.org/christian_soeller/python-microscopy-exeter) -
  a fork of David's python-microscopy with our changes
* <i class="fa fa-bitbucket fa-lg"></i>
  [pyme-extra](http://bitbucket.org/christian_soeller/pyme-extra) -
  extra plugins for PYME, including qPAINT, camera map tools, etc
* <i class="fa fa-bitbucket fa-lg"></i>
  [pyme-exeter-siteconfig](http://bitbucket.org/christian_soeller/pyme-exeter-siteconfig) -
  PYME site specific init files and custom protocols
* <i class="fa fa-bitbucket fa-lg"></i>
  [python-microscopy-osxapps](https://bitbucket.org/christian_soeller/python-microscopy-osxapps) -
  an alternative mac app interface for PYME using the
  [platypus](http://www.sveinbjorn.org/platypus) app builder
