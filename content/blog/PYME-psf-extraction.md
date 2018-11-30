Title: Extracting PSFs with PYME
Date: 2018-11-30 09:14
Status: published
Slug: blog/Extracting_PSFs_with_PYME
Tags: super-resolution, software, python

<img width="700" src="{filename}/images/software/PYME-psf-viewer.png" alt="PYME PSF viewer">

## A brief tutorial

[PYME]({filename}/pages/software/PYME.md) is a very powerful framework but for that reason also can be complex to use. In addition, the documentation often does not keep pace with the introduction of exciting new features. In a loose series of blogs we will illustrate a few procedures that one often needs to use which hopefully will be useful for other PYME users.

### Installing PYME

The following assumes you have a running copy of PYME. The quickest way to install is probably following steps 1-3 on David's main [PYME installation page](http://python-microscopy.org/doc/Installation/InstallationWithAnaconda.html).

### Open your PSF stack

The first step is to open the PSF stack in dh5view, this is a step that may require you to provide some info about your data if it was not recorded with PYME itself.

David provides some instructions [how to import your data](http://python-microscopy.org/doc/AnalysingForeignData.html#analysingforeigndata). Basically, you need to provide some essential metadata in a `.md` file. Once that is done you can open your file by typing in a terminal

	dh5view <filename>.tif

Alternatively, just start `dh5view` using the GUI and then use the `File>Open` dialog to read your file. Finally, there are pretty straightforward ways to set things up, in both macos and windows, so that the opening can be done just using GUI commands, e.g. `Open with...` in the windows FileManager etc. Perhaps material for another blog entry.

### Loading the PSF Extraction module

Once you have opened your psf stack, you should load the `psfExctraction` module, as shown in the screenshot below.

<img width="700" src="{filename}/images/software/PYME-psf-extract-selectmodule.png" alt="load PSF extraction module">


### Tag PSF candidates using the crosshair tool

The next step is to tag psf candidates with the crosshair selection tool (selectable atthe top right, it is selected by default). You only need to click near the center of a PSF image and then press the `Tag` button.

<img width="700" src="{filename}/images/software/PYME-psf-extract-crosshair.png" alt="tag PSFs">

### Repeat for all candidates and then extract

At this stage all you need to do is repeat this for all candidates. Each successfully tagged psf image gets a green box around it. Once done press `Extract`.

<img width="700" src="{filename}/images/software/PYME-psf-extract-doextract.png" alt="extract PSFs">

At this stage I will point out David's [PSF Extraction Documentation](http://python-microscopy.org/doc/PSFExtraction.html). it has most of the points given here and also explains a few other aspects, i.e. the other parameters you can edit (e.g. the size of the volume to extract around each bead) and the other modes of PSF extraction, e.g. for multi-channel data, etc.

I will complete this blog entry soonish, while also explaining how to save the resulting PSF and other aspects that may not be so obvious for a first time user.
