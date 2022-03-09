# Download and install

## Table of contents
- [Download](#download)
  * [Download the whole repository](#download-the-whole-repository)
  * [Download the latest release](#download-the-latest-release)
- [Prerequisites](#prerequisites)
  * [Mandatory](#mandatory)
  * [Optional](#optional)
- [Install](#install)
- [Update](#update)
- [Uninstall](#uninstall)
- [Compile and run](#compile-and-run)
  * [Use in your device](#use-in-your-device)
  * [Compile the source code example and testing](#compile-the-source-code-example-and-testing)
- [Other scripts](#other-scripts)
  * [debug.sh](#debugsh)

## Download 

To download the library you can proceed in two independent ways.

### Download the whole repository

First of all, you need to download the code: go to the [main page](https://github.com/JustWhit3/arsenalgear) of the repository and click on the upper right green button called `Code`. Than click on `Download ZIP` and wait the download to be completed.

Then open a fresh shell and move the downloaded zipped file to your home directory (or to any other place you prefer):
```shell
mv Downloads/arsenalgear-main.zip $HOME
```
Where ``Downloads`` have to be replaced with the right name (and maybe the right path) of your downloads directory.

Now you have to enter your home folder (unless you were already in it, in this case skip this passage), extract the folder from the zipped file and renaming itself with its right repository name. Therefore lets type this commands one after the other:
```shell
cd $HOME
unzip arsenalgear-main.zip
mv arsenalgear-main arsenalgear
```
And that's all. You can enter the folder by simply typing:
```shell
cd arsenalgear
```

### Download the latest release

Alternatively you can download the latest version of the repository from the ``Releases`` button on the right of the repository main page by clicking on the source code link. In this case the procedure is similar:

Open a fresh shell and move the downloaded zipped file to your home directory (or to any other place you prefer):
```shell
mv Downloads/arsenalgear-x.y.z.zip $HOME
```
Where `x.y.z` is the release tag and ``Downloads`` have to be replaced with the right name (and maybe the right path) of your downloads directory.

Now you have to enter your home folder (unless you were already in it, in this case skip this passage), extract the folder from the zipped file and renaming itself with its right repository name. Therefore lets type this commands one after the other:
```shell
cd $HOME
unzip arsenalgear-x.y.z.zip
mv arsenalgear-x.y.z arsenalgear
```

> If you prefer to download the tar.gz format of the release you have to run the `gunzip` command followed by the `tar -xvf` command on the zipped release folder and than proceed with `mv`. 

And that's all. You can enter the folder by simply typing:
```shell
cd arsenalgear
```

## Prerequisites

All the prerequisites can be installed during the first step of the automatic installation with the installer [script](https://github.com/JustWhit3/arsenalgear/blob/main/scripts/install_cpp.sh).

### Mandatory

- C++17 standard.
- g++ compiler (g++ 9.3.0 has been tested so far) for compilation.
- [Boost](https://www.boost.org/) library.
- [GNU make](https://www.opensourceforu.com/2012/06/gnu-make-in-detail-for-beginners/#:~:text=Installing%20GNU%20Make,install%20build%2Dessential.) for compilation.
- [ExprTK](http://www.partow.net/programming/exprtk/) library for functions parsing.


### Optional

- [doctest](https://github.com/onqtam/doctest) for testing compilation.
- [subversion](https://linuxtechlab.com/simple-guide-to-install-svn-on-linux-apache-subversion/) to correctly run the [update.sh](#update) script.
- [Valgrind](https://valgrind.org/) to run the [debug.sh](#debugsh) script.
- [Cppcheck](https://github.com/danmar/cppcheck) to run the [debug.sh](#debugsh) script.
- [Clang formatter](https://stackoverflow.com/questions/20756924/how-can-i-install-clang-format-in-ubuntu#:~:text=16.04%2C%20simply%20do%3A-,sudo%20apt%20install%20clang%2Dformat,-Share) to format the code for pull requests.

## Install

An installer script, called [install_cpp.sh](https://github.com/JustWhit3/arsenalgear/blob/main/scripts/install_cpp.sh), has been introduced. This script can be used to properly install the library into your computer, in order to easily use it in your programs.

Once the source code has been downloaded you can simply run this script. Enter the arsenalgear folder and type this command on the shell:
```shell
./scripts/install_cpp.sh
```
> **NOTE**: scripts have to be run directly from the repository home directory.

A new library *libarsenalgear* will be created into the `/usr/local/lib` folder of your computer and the [*header*](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include) files will be installed into `/usr/local/include`.

## Update

In case you want to update the source code from the latest improvements of the repository, you can use the updater script, called [update.sh](https://github.com/JustWhit3/osmanip/blob/main/cpp/update.sh).

From the repository folder type this command on the shell:
```shell
./scripts/update.sh
```
Then, you can reinstall the repository:
```shell
./scripts/install_cpp.sh
```

## Uninstall

In case you want to uninstall the software from your computer, you can use the uninstaller script, called [uninstall.sh](https://github.com/JustWhit3/arsenalgear/blob/main/uninstall.sh).

From the repository folder type this command on the shell:
```shell
./scripts/uninstall.sh
```

## Compile and run

### Use in your device

Once you have installed the library you can freely use it in one of your C++ projects by including one or more of the modules:
```c++
#include <arsenalgear/module_name.hpp>
```
for example:
```c++
#include <arsenalgear/math.hpp>
```
Now you are able to access al the functions and classes of the manipulator.

You can additionally add also a namespace directive if you want:
```c++
using namespace agr;
```

Supposing you are using the library in a program called *program.cpp*, to compile it you have simply to enter this command in the shell:
```shell
g++ program.cpp -larsenalgear
```
and then you can run the code with:
```shell
./a.out
```
> **NOTE**: at least c++17 standard is required to successfully access al the library features.

### Compile the source code example and testing

The source code contains also an example code [*cpp/src/examples.cpp*](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/src/examples.cpp) to show the user a simple usage of all the features supported by the library and test codes in the [**test**](https://github.com/JustWhit3/osmanip/blob/main/cpp/test) folder to test the correct functionality of the library functions and methods.

To compile them I prepared a [Makefile](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/Makefile). The source code is already compiled when you install the library, but in case you don't want to install the package and explore only the library features through this examples, you can run this command on the shell:
```shell
make
```
This will compile both main and test codes. An extra **obj** folder with object files and a **bin** folder with two executables, *main* and *tests*, are now created.
>**NOTE**: compilation may be slow due to the expensive operation of the `parsed_f` function, which uses the ExprTK library.

You have simply to run the former in order to run the entire example code:
```shell
./bin/examples
```
or the latter in order to test the correct functionalities of the library classes methods and functions:
```shell
./bin/tests
```
If you want to compile only the main code you can simply enter:
```shell
make examples
```
if instead you want to compile only the tests code you can use the following command:
```shell
make tests
```
There is also an option to go back to the pre-compilation state of the code, to do this simply type this command:
```shell
make clean
```
## Other scripts

Other scripts have been provided into the [**scripts**](https://github.com/JustWhit3/arsenalgear/blob/main/scripts) folder. After compiling the source code, they can be run from the repository home directory.

### debug.sh

This script is used to run [Valgrind](https://valgrind.org/) and [Cppcheck](https://github.com/danmar/cppcheck) debugging tools on the whole code.

You can run Valgrind debugging tools with a specific executable:
```shell
./scripts/debug.sh [valgrind-tool-name] [executable-name]
```