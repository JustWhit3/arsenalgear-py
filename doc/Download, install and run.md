# Download and install

## Table of contents

- [Download](#download)
  - [Download the whole repository](#download-the-whole-repository)
  - [Download the latest release](#download-the-latest-release)
- [Prerequisites](#prerequisites)
  - [Mandatory](#mandatory)
  - [Optional](#optional)
- [Install](#install)
- [Use in your device](#use-in-your-device)
- [Run tests](#run-tests)

## Download

To download the library you can proceed in two independent ways.

### Download the whole repository

First of all, you need to download the code: go to the [main page](https://github.com/JustWhit3/arsenalgear-py) of the repository and click on the upper right green button called `Code`. Than click on `Download ZIP` and wait the download to be completed.

Then open a fresh shell and move the downloaded zipped file to your home directory (or to any other place you prefer):

```shell
mv Downloads/arsenalgear-py-main.zip $HOME
```

Where ``Downloads`` have to be replaced with the right name (and maybe the right path) of your downloads directory.

Now you have to enter your home folder (unless you were already in it, in this case skip this passage), extract the folder from the zipped file and renaming itself with its right repository name. Therefore lets type this commands one after the other:

```shell
cd $HOME
unzip arsenalgear-py-main.zip
mv arsenalgear-py-main arsenalgear-py
```

And that's all. You can enter the folder by simply typing:

```shell
cd arsenalgear-py
```

### Download the latest release

Alternatively you can download the latest version of the repository from the ``Releases`` button on the right of the repository main page by clicking on the source code link. In this case the procedure is similar:

Open a fresh shell and move the downloaded zipped file to your home directory (or to any other place you prefer):

```shell
mv Downloads/arsenalgear-py-x.y.z.zip $HOME
```

Where `x.y.z` is the release tag and ``Downloads`` have to be replaced with the right name (and maybe the right path) of your downloads directory.

Now you have to enter your home folder (unless you were already in it, in this case skip this passage), extract the folder from the zipped file and renaming itself with its right repository name. Therefore lets type this commands one after the other:

```shell
cd $HOME
unzip arsenalgear-py-x.y.z.zip
mv arsenalgear-py-x.y.z arsenalgear-py
```

> If you prefer to download the tar.gz format of the release you have to run the `gunzip` command followed by the `tar -xvf` command on the zipped release folder and than proceed with `mv`.

And that's all. You can enter the folder by simply typing:

```shell
cd arsenalgear-py
```

## Prerequisites

All the mandatory prerequisites can be automatically obtained during the installation via `pip`.

### Mandatory

Tools:

- Python 3.8.10.

Libraries and frameworks:

- `matplotlib >= 3.1.2`.
- `numpy >= 1.17.4`.
- `scipy == 1.6.2`.
- `termcolor == 1.1.0`.

### Optional

- [unzip](https://www.mysoftkey.com/linux/how-to-do-zip-and-unzip-file-in-ubuntu-linux/) to unzip zipped directories during update with the `update.sh` script.

## Install

To install the module you can simply do it through `pip`, since it is present in the official Python package manager ([here](https://pypi.org/project/arsenalgear-py/)):

```bash
pip install arsenalgear
```

To run examples:

```python
python examples.py
```

## Use in your device

Once you have installed the library you can freely use it in one of your Python projects by including one or more of the modules:

```python
from arsenalgear import module_name
```

for example:

```Python
from arsenalgear import mathematics
```

Now you are able to access al the functions and classes of the module.

## Run tests

Tests have been performed using [`doctest`](https://docs.python.org/3/library/doctest.html) which is integrated in Python 8.

To run tests you can simply run one of the module codes:

```Python
python module_name
```

for example:

```Python
python mathematics.py
```

and if the tests run correctly anything is output, otherwise and error message is displayed.

If you want a detailed tests log printed on the screen, simply enter:

```Python
python src/utils.py -v
python src/functions.py -v
```
