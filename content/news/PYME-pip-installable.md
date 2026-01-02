Title: Easier PYME install available
Date: 2025-12-18 13:00
Status: published
Slug: news/pypme-pip-installable
Tags: nano, super-resolution, software, python-microscopy

<img width="200" src="{static}/images/research/pymeLogo.png" alt="PYME"/>

### PYME and PYME-extra now fully pip installable

For users mainly interested in the stable releases of `python-microscopy` and `PYME-extra` for usage as is we now recommend a pip based install.

We highly recommend installing into a fresh virtual environment as can be generated with `conda` and related tools:

1. if you don't yet have it, download and install [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda) or [miniforge](https://github.com/conda-forge/miniforge).

2. create and activate a new conda environment with python 3.10 to 3.13 (3.10 and 3.11 are probably the most well tested at present)

```
    conda create -n pyme-pip python=3.10
    conda activate pyme-pip
```

Now you are ready to use `pip` to install `python-microscopy` and `PYME-extra` (`#` is the comment sign on macOS/posix shells, just leave out that text when pasting to windows command prompts):

```
	# possibly install python-microscopy first and check that the install succeeds
	pip install python-microscopy
	pip install PYME-extra # installation from PyPi
	pymex_install_plugins # important final step: register the plugins systemwide
```

This should be all, at this stage you can launch the main applications, i.e. `visgui` (AKA `PymeVis` or `PYMEVisualize`) and `dh5view` (AKA `PYMEImage`) to open and process microscopy data. See also [Verify Installation](https://www.python-microscopy.org/doc/Installation/Installation.html#verify-installation) in the [PYME docs](https://www.python-microscopy.org/doc).

Further details on installing are available on the [PYME-extra github pages](https://github.com/csoeller/PYME-extra).
