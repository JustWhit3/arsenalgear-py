<p align="center"><img src="https://github.com/JustWhit3/arsenalgear/blob/main/img/logo.svg" height=220></p>

<h3 align="center">A library containing general purpose utils I developed for other projects, using different languages</h3>
<p align="center">
    <img title="v1.0" alt="v1.0" src="https://img.shields.io/badge/version-v1.0-informational?style=flat-square"
    <a href="LICENSE">
        <img title="MIT License" alt="license" src="https://img.shields.io/badge/license-MIT-informational?style=flat-square">
    </a>
	<img title="C++17" alt="C++17" src="https://img.shields.io/badge/c++-17-informational?style=flat-square">
	<img title="Python 3.8.10" alt="Python 3.8.10" src="https://img.shields.io/badge/Python-3.8.10-informational?style=flat-square"><br>
	<img title="Code size" alt="code size" src="https://img.shields.io/github/languages/code-size/JustWhit3/arsenalgear?color=red">
	<img title="Repo size" alt="repo size" src="https://img.shields.io/github/repo-size/JustWhit3/arsenalgear?color=red">
	<img title="Lines of code" alt="total lines" src="https://img.shields.io/tokei/lines/github/JustWhit3/arsenalgear?color=red">

***

## Table of contents

- [Introduction](#introduction)
- [Documentation](#documentation)
- [News from the last release](#news-from-the-last-release)
- [List of features](#list-of-features)
- [Credits](#credits)
  - [Project leaders](#project-leaders)

## Introduction

This library contains a set of generic utils (functions and classes), for different languages, I developed for other projects. There are several sub-headers / modules related to the various topics (math, iostream and others). There are folders related to each programming languages I developed tools for. You can simply enter one of the folder with a language name and explore the various tools. You can also easily install the libraries using one of the installation scripts of the [scripts](https://github.com/JustWhit3/arsenalgear/tree/main/scripts) folder and run an example code for each programming language or following the guides.
> **NOTE**: the various libraries for different languages don't necessary contain the same functions / classes written in different languages. The contents are usually different.

Existing tools are constantly updated and new ones are added once their development is required for other projects.

Some projects in which I am using this library are, for example: [osmanip](https://github.com/JustWhit3/osmanip) and [SAFD-algorithm](https://github.com/JustWhit3/SAFD-algorithm).

If you want to use this library please cite it following [this](https://github.com/JustWhit3/arsenalgear/blob/main/CITATION.cff) citation template.

The software is and will stay **free**, but if you want to support me with a donation it would be really appreciated!

<a href="https://www.buymeacoffee.com/JustWhit33" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Supported and tested operating systems:

- Ubuntu (and the other Linux OSs).
- Windows Subsystem for Linux (WSL).

## Documentation

Repository diagram structure:

```txt
arsenalgear/
├── cpp/
│   ├── doc/
│   │   ├── Code structure.md
│   │   ├── Download, install and run.md
│   ├── include/
│   │   ├── constants.hpp
│   │   ├── math.hpp
│   │   ├── operators.hpp
│   │   ├── stream.hpp
│   │   ├── utils.hpp
│   ├── src/
│   │   ├── examples.cpp
│   │   ├── operators.cpp
│   │   ├── stream.cpp
│   ├── test/
│   │   ├── tests_math.cpp
│   │   ├── tests_operators.cpp
│   │   ├── tests_stream.cpp
│   │   ├── tests_utils.cpp
│   ├── Makefile
│   ├── .clang-format
│   ├── .valgrindrc
├── python/
│   ├── arsenalgear/
│   │   ├── __init__.py
│   │   ├── mathematics.py
│   │   ├── plotter.py
│   │   ├── machinelearning.py
│   ├── doc/
│   │   ├── Code structure.md
│   │   ├── Download, install and run.md
│   ├── examples.py
│   ├── setup.py
├── scripts/
│   ├── install_cpp.sh
│   ├── uninstall_cpp.sh
│   ├── debug.sh
│   ├── update.sh
│   ├── size_of_dir.py
├── img/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CITATION.cff
├── .gitignore
├── .all-contributorsrc
```

General documentation:

- [Contributing to the repository](https://github.com/JustWhit3/arsenalgear/blob/main/CONTRIBUTING.md): a generic file containing detailed info about how to open an issue or send a pull request to contribute.

Documentation for the [cpp](https://github.com/JustWhit3/arsenalgear/tree/main/cpp) folder:

- [Code structure](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/doc/Code%20structure.md): contains a detailed list of the `cpp` objects of the repository and how to use them.
- [Download, install and run](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/doc/Download%2C%20install%20and%20run.md): contains instructions about how to install, download and run the repository code and extra information about the scripts of the [scripts](https://github.com/JustWhit3/arsenalgear/tree/main/scripts) folder.

Documentation for the [python](https://github.com/JustWhit3/arsenalgear/tree/main/python) folder:

- [Code structure](https://github.com/JustWhit3/arsenalgear/blob/main/python/doc/Code%20structure.md): contains a detailed list of the `python` objects of the repository and how to use them.
- [Download, install and run](https://github.com/JustWhit3/arsenalgear/blob/main/python/doc/Download%2C%20install%20and%20run.md): contains instructions about how to install, download and run the repository code and extra information about the scripts of the [scripts](https://github.com/JustWhit3/arsenalgear/tree/main/scripts) folder for the python utils.

## News from the last release

- Python package version has been added to PyPi.
- Module datascience has been provided.
- Module utils has been provided.
- Module parallelization has been provided.

## List of features

Here you can find the list of features implemented in the current version of the library:

- **cpp** headers:
  - [Constants](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/constants.hpp): contains a list of constants developed for utility.
  - [Math](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/math.hpp): contains a list of mathematical tools.
  - [Operators](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/operators.hpp): contains a list of operators redefinition.
  - [Stream](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/stream.hpp): contains a list of input / output stream tools.
  - [Utils](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/utils.hpp): contains a list of generic utils which don't fit any of the other categories.

- **python** modules:
  - [Math](https://github.com/JustWhit3/arsenalgear/blob/main/python/arsenalgear/mathematics.hpp): contains a list of mathematical tools.
  - [Machine learning](https://github.com/JustWhit3/arsenalgear/blob/main/python/arsenalgear/machinelearning.hpp): contains a list of machine learning tools.
  - [Plotting tools](https://github.com/JustWhit3/arsenalgear/blob/main/python/arsenalgear/plotter.hpp): contains a list of plotting tools.

## Credits

### Project leaders

<table>
  <tr>
    <td align="center"><a href="https://justwhit3.github.io/"><img src="https://avatars.githubusercontent.com/u/48323961?v=4" width="100px;" alt=""/><br /><sub><b>Gianluca Bianco</b></sub></a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
