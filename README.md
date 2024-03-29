<p align="center"><img src="https://github.com/JustWhit3/arsenalgear-py/blob/main/img/logo.svg" height=220></p>

<h3 align="center">A library containing general purpose utils.</h3>
<p align="center">
    <img title="v1.3" alt="v1.3" src="https://img.shields.io/badge/version-v1.3-informational?style=flat-square"
    <a href="LICENSE">
        <img title="MIT License" alt="license" src="https://img.shields.io/badge/license-MIT-informational?style=flat-square">
    </a>
	<img title="Python 3.10.4" alt="Python 3.10.4" src="https://img.shields.io/badge/Python-3.10.4-informational?style=flat-square"><br>
	<img title="Code size" alt="code size" src="https://img.shields.io/github/languages/code-size/JustWhit3/arsenalgear-py?color=red">
	<img title="Repo size" alt="repo size" src="https://img.shields.io/github/repo-size/JustWhit3/arsenalgear-py?color=red">
	<img title="Lines of code" alt="total lines" src="https://img.shields.io/tokei/lines/github/JustWhit3/arsenalgear-py?color=red"><br/>
  <img title="codeq" alt="codeq" src="https://github.com/JustWhit3/arsenalgear-py/actions/workflows/codeql-analysis.yml/badge.svg">
  <img title="DocGenerator" alt="DocGenerator" src="https://github.com/JustWhit3/arsenalgear-py/actions/workflows/DocGenerator.yml/badge.svg">

***

## Table of contents

- [Introduction](#introduction)
- [Install and run](#install-and-run)
- [Extra documentation](#extra-documentation)
- [List of features](#list-of-features)
  - [Data science](#data-science)
  - [Mathematics](#mathematics)
  - [Parallelization](#parallelization)
  - [Plotter](#plotter)
- [Credits](#credits)
  - [Project leaders](#project-leaders)
- [Stargazers over time](#stargazers-over-time)

## Introduction

This library contains a set of generic utils I developed for other projects. There are several sub-headers / modules related to various topics (mathematics, threading etc...).

Existing tools are constantly updated and new ones are added once their development is required for other projects.

If you want to use this library please cite it following [this](https://github.com/JustWhit3/arsenalgear/blob/main/CITATION.cff) citation template.

The software is and will stay **free**, but if you want to support me with a donation it would be really appreciated!

<a href="https://www.buymeacoffee.com/JustWhit33" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Supported operating systems:

- Linux (Ubuntu and WSL tested)
- Windows 10.
- MaxOS.

## Install and run

Steps to be reproduced:

**1)** Install the library and prerequisites.

```bash
pip install arsenalgear
```

> To run examples:
>
>```python
>python examples.py
>```

**2)** Use in your device

Once you have installed the library you can freely use it in one of your Python projects by including one or more of the modules:

```python
from arsenalgear import module_name
```

for example:

```Python
from arsenalgear import mathematics
```

**3)** Run the tests (optional):

If you want to run the tests you have to type:

```shell
python src/arsenalgear/module_name
```

If anything is displayed it means that tests ran correctly.

Tests have been performed using the [Doctest](https://docs.python.org/3/library/doctest.html) framework.

If you want a detailed tests log printed on the screen, simply enter:

```shell
python src/arsenalgear/module_name -v
```

## Extra documentation

- [Contributing to the repository](https://github.com/JustWhit3/arsenalgear-py/blob/main/CONTRIBUTING.md): a generic file containing detailed info about how to open an issue or send a pull request to contribute.
- [Code documentation](https://justwhit3.github.io/arsenalgear-py/index.html): code documentation has been generated using Doxygen.

## List of features

### Data science

- [`AMS_score`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1datascience.html#a0763a5d9063ba2ad2f02afeb27dbebf1): function used to retrieve the AMS score.
- [`RemoveOutliers`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1datascience.html#a5e0b3384380b048873103f8b29f0af9c): function used to remove the outliers of an array.
- [`RemoveOutliers_DF`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1datascience.html#ad8091af135f0399eefd1cf9ff5cb4ff0): function used to remove the outliers of a dataframe.

### Mathematics

- [`Hermite`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1mathematics.html#a13b6c046844f01db40eba86d5bfc444a): function used to retrieve Hermite polynomials values.
- [`Chebyshev`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1mathematics.html#af8f1f1077fe6a2122d0e3966d018024d): function used to retrieve Chebyshev polynomials values.
- [`Legendre`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1mathematics.html#aecf04044cf0ab973d20fbb9dc987b5dc): function used to retrieve Legendre polynomials values.
- [`Laguerre`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1mathematics.html#a53074055544eedb8978dc3d769625552): function used to retrieve Laguerre polynomials values.
- [`IsInBounds`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1mathematics.html#a5e46216eda407e1b2f7d41174349fdfb): function used to check if a value is in a certain bound or not.
- [`e_parser`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1mathematics.html#afca1150afc0f3a661662e0e92ef9d0d3): function used to return the complex value of a parsed expression.
- [`kronecker`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1mathematics.html#a18ed877a011ff6caa380e11964b40dd5): function used to compute the Kronecker delta.
- [`OrderOfMagnitude`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1mathematics.html#a194458ac454c279b4f85b70ddb9141d2): function used to find the order og magnitude of a number.

### Parallelization

- [`MultiProcesses`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1parallelization.html#aaa6a5e0f47866f0584b64255518efcd8): function used to parallelize more functions.
- [`chunker`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1parallelization.html#a7995c580610863b92f988bb23aaa588e): function used send a bunch of processes in parallel.

### Plotter

- [`plot_AMS`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1plotter.html#ad6d1642cee8c1d9bdc9dbd733c5da6f3): function used to plot the AMS score.
- [`plotter_complex`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1plotter.html#af2555056142e267a7c9cc06467bf20e8): function used to plot a given function for an index n.
- [`plot_learning_curve`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1plotter.html#a8aac49421888ff46f8a7224b8e69937a): function used to plot a learning curves for train and tests sets of a dataset.

### Utils

- [`TimeToInt`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1utils.html#a1848f48fa5574beecead7c9397e7c26c): function used to convert a time-string into an integer.
- [`IntToTime`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1utils.html#a9f4c99effed79a774bf6ad5f74c3f0ae): function used to convert an integer into a time-string.
- [`save_img`](https://justwhit3.github.io/arsenalgear-py/namespacearsenalgear_1_1utils.html#a90e7c8346eb2f207ed45ac0527ffa9dd): function used to save an image in a certain position of the system.

## Credits

### Project leaders

<table>
  <tr>
    <td align="center"><a href="https://justwhit3.github.io/"><img src="https://avatars.githubusercontent.com/u/48323961?v=4" width="100px;" alt=""/><br /><sub><b>Gianluca Bianco</b></sub></a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## Stargazers over time

[![Stargazers over time](https://starchart.cc/JustWhit3/arsenalgear-py.svg)](https://starchart.cc/JustWhit3/arsenalgear-py)