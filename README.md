<p align="center"><img src="https://github.com/JustWhit3/arsenalgear-py/blob/main/img/logo.svg" height=220></p>

<h3 align="center">A library containing general purpose utils I developed for other projects</h3>
<p align="center">
    <img title="v1.1" alt="v1.1" src="https://img.shields.io/badge/version-v1.1-informational?style=flat-square"
    <a href="LICENSE">
        <img title="MIT License" alt="license" src="https://img.shields.io/badge/license-MIT-informational?style=flat-square">
    </a>
	<img title="Python 3.8.10" alt="Python 3.8.10" src="https://img.shields.io/badge/Python-3.8.10-informational?style=flat-square"><br>
	<img title="Code size" alt="code size" src="https://img.shields.io/github/languages/code-size/JustWhit3/arsenalgear-py?color=red">
	<img title="Repo size" alt="repo size" src="https://img.shields.io/github/repo-size/JustWhit3/arsenalgear-py?color=red">
	<img title="Lines of code" alt="total lines" src="https://img.shields.io/tokei/lines/github/JustWhit3/arsenalgear-py?color=red">

***

## Table of contents

- [Introduction](#introduction)
- [Documentation](#documentation)
- [News from the last release](#news-from-the-last-release)
- [List of features](#list-of-features)
  - [Data science](#data-science)
  - [Mathematics](#mathematics)
  - [Parallelization](#parallelization)
  - [Plotter](#plotter)
- [Credits](#credits)
  - [Project leaders](#project-leaders)

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

## Documentation

Repository diagram structure:

```txt
arsenalgear/
├── .github/
│   ├── workflows/
│   │   ├── codeql-analysis.yml
├── examples/
│   ├── datascience.py
│   ├── mathematics.py
│   ├── parallelization.py
│   ├── plotter.py
│   ├── utils.py
├── src/
│   ├── arsenalgear/
│   │   ├── __init__.py
│   │   ├── mathematics.py
│   │   ├── plotter.py
│   │   ├── datascience.py
│   │   ├── parallelization.py
│   │   ├── utils.py
│   ├── setup.py
│   ├── setup.cfg
├── doc/
│   ├── Code structure.md
│   ├── Contributing.md
│   ├── Download, install and run.md
├── img/
├── README.md
├── LICENSE
├── CITATION.cff
├── .gitignore
├── .all-contributorsrc
```

General documentation:

- [Contributing to the repository](https://github.com/JustWhit3/arsenalgear-py/blob/main/doc/Contributing.md): a generic file containing detailed info about how to open an issue or send a pull request to contribute.
- [Code structure](https://github.com/JustWhit3/arsenalgear-py/blob/main/doc/Code%20structure.md): contains a detailed list of the `python` objects of the repository and how to use them.
- [Download, install and run](https://github.com/JustWhit3/arsenalgear-py/blob/main/doc/Download%2C%20install%20and%20run.md): contains instructions about how to install, download and run the repository code.

## News from the last release

- Python package version has been added to PyPi.
- Module datascience has been provided.
- Module utils has been provided.
- Module parallelization has been provided.

## List of features

Here you can find the list of features implemented in the current version of the library:

### Data science

- [AMS_score](): function used to retrieve the AMS score.
- [RemoveOutliers](): function used to remove the outliers of an array.

### Mathematics

- [Hermite](): function used to retrieve Hermite polynomials values.
- [Chebyshev](): function used to retrieve Chebyshev polynomials values.
- [Legendre](): function used to retrieve Legendre polynomials values.
- [Laguerre](): function used to retrieve Laguerre polynomials values.
- [IsInBounds](): function used to check if a value is in a certain bound or not.
- [e_parser](): function used to return the complex value of a parsed expression.
- [kronecker](): function used to compute the Kronecker delta.

### Parallelization

- [MultiProcesses](): function used to parallelize more functions.

### Plotter

- [plot_AMS](): function used to plot the AMS score.
- [plotter_complex](): function used to plot a given function for an index n.

### Utils

- [TimeToInt](): function used to convert a time-string into an integer.
- [IntToTime](): function used to convert an integer into a time-string.

## Credits

### Project leaders

<table>
  <tr>
    <td align="center"><a href="https://justwhit3.github.io/"><img src="https://avatars.githubusercontent.com/u/48323961?v=4" width="100px;" alt=""/><br /><sub><b>Gianluca Bianco</b></sub></a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
