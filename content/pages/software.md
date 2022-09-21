Title: Software
Slug: software
Date: 2017-11-19 11:54
Tags: software, stuff

The laboratory fully supports open source and sharable code
resources. Code and software play an important role in our work and we
are both active users of open software and are actively contributing
the code and algorithms that we develop back to the community.

## PYME - the Python Microscopy Environment

<img style="float:left; border-right:8px solid white" width="300"
src="{static}/images/software/PYMEacquire.png" alt="PYME Acquire GUI
Interface"/>
[PYME](http://python-microscopy.org/) is a microscopy
software environment designed and implemented by our colleague David
Baddeley. David worked with us for several years, a large part of
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

<img style="float:right; border-right:8px solid white" width="300"
src="{static}/images/software/PYMEvisgui.png" alt="PYME VisGUII Interface"/>
PYME also has a PALM/STORM data exploration and visualisation tool,
VisGUI. VisGUI offers a fast and flexible tool for exploring and
visualising the list of fluorophore locations that is produced by
PALM/STORM analysis algorithms. VisGUI renders localisations in various
different ways and can filter and process localisation events in
powerful and flexible ways. Recently, we have implemented extension
plugins to experiment with the qPAINT quantitative imaging paradigm
and the powerful Python based infrastructure enabled the
implementation of cluster based processing with relative ease.

PYME is not limited to super-resolution microscopy. It can also deal
with various types of confocal data - it provides powerful
deconvolution and 3D visualisation tools.

## PYME github repositories

We maintain several repositories on [github](https://github.com/)
that contain our acquisition, analysis and control codes for various
types of microscopy.

* <i class="fa fa-github fa-lg"></i>
  [python-microscopy](https://github.com/csoeller/python-microscopy) -
  a fork of David's python-microscopy with our pull requests etc
* <i class="fa fa-github fa-lg"></i>
  [pyme-extra](https://github.com/csoeller/PYME-extra) -
  extra plugins for PYME, including qPAINT, camera map tools, etc
* <i class="fa fa-github fa-lg"></i>
  [pyme-cs-siteconfig](https://github.com/csoeller/PYME-cs-siteconfig) -
  PYME site specific init files and custom protocols
  * <i class="fa fa-github fa-lg"></i>
  [pyme-extra-sample-data](https://github.com/csoeller/PYME-extra-sample-data) -
  PYME sample data for tests and illustrations plus some code examples
* <i class="fa fa-github fa-lg"></i>
  [pyme-apps](https://github.com/csoeller/PYME-apps) -
  macos lightweight app wrappers for PYME using the
  [platypus](http://www.sveinbjorn.org/platypus) app builder


## ImageJ/Fiji

<img style="float:right; border-right:8px solid white" width="150"
src="{static}/images/software/fiji.png" alt="Fiji"/> [Fiji](http://fiji.sc/)
is an image processing package—a "batteries-included" distribution of
ImageJ, bundling a lot of plugins which facilitate scientific image
analysis.

<img style="float:left; border-right:8px solid white" width="150"
src="{static}/images/software/Imagej2-icon.png" alt="ImageJ"/> Fiji comes in
handy all the time for various smaller and larger jobs on image
processing. Its GUI interface makes it very suitable for beginners,
students and all those who are not yet experts in writing their own
code with Python, IDL or similar languages.

We do not contribute ourselves to Fiji/ImageJ but promote its use and
support as a great example of an open software tool that has become
very useful and allows access to high quality image processing for
those who are not programmers at heart.

We recommend using Fiji over standalone imageJ as the updating
mechanism and plugin handling is vastly superior in Fiji which
essentially wraps a package manager type application around ImageJ and
therefore makes maintenance a breeze.

## PDL

<img style="float:left; border-right:8px solid white" width="150"
src="{static}/images/software/PerlDL-logopic.png" alt="PDL Logo"/>Now of
mostly historical interest, CS is one of the original core developers
of [PDL](http://pdl.perl.org/), an array language like matlab, IDL, or
numpy, which is based on the [Perl](http://www.perl.org/) scripting
language.

PDL ("Perl Data Language") gives standard Perl the ability to
compactly store and speedily manipulate the large N-dimensional data
arrays which are the bread and butter of scientific computing.

PDL turns Perl into a free, array-oriented, numerical language similar
to (but, we believe, better than) such commercial packages as IDL and
MatLab. One can write simple Perl expressions to manipulate entire
numerical arrays all at once. Simple interactive shells are provided
for use from the command line along with the PDL module for use in
Perl scripts.

PDL was the first larger open software project that CS had become
involved with. One of the nicest side effects was getting to know two
fellow academics and programmers,
[Karl Glazebrook](http://astronomy.swin.edu.au/~karl) who is now a
professor of astronomy at Swinburne and
[Tuomas Lukka](http://www.linkedin.com/in/tuomas-j-lukka-013abb3/) who
is now chief scientist at [Zen Robotics](http://zenrobotics.com/).

