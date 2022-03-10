#!/bin/bash

#====================================================
#     CHECK IF OS IS WINDOWS OR NOT
#====================================================
UNAME=$(uname)
main="examples"
if [[ "$UNAME" == CYGWIN* || "$UNAME" == MINGW* ]] ; then
	main="${main}.exe"
fi

#====================================================
#     INSTALLING PREREQUISITES
#====================================================
sudo apt install build-essential g++ libboost-all-dev wget unzip
echo ""
echo "Installing ExprTk library..."
exprtk_sha1=ca5c577917646ddba3f71ce6d5dd7d01f351ee80
wget https://github.com/ArashPartow/exprtk/archive/$exprtk_sha1.zip
mv $exprtk_sha1.zip exprtk-$exprtk_sha1.zip
unzip exprtk-$exprtk_sha1.zip
sudo cp exprtk-$exprtk_sha1/exprtk.hpp /usr/include/
rm -rf exprtk-*
echo ""
read -p "Do you want to install optional arsenalgear prerequisites (y/n)? " word_o
if [ $word_o == "y" ] || [ $word_o == "Y" ] ; then
    sudo apt install doctest-dev subversion valgrind cppcheck clang-format
fi
echo ""

#====================================================
#     COMPILATION OF THE SOURCE CODE
#     (check if doctest is installed)
#====================================================
cd cpp || exit
if [ -f "/usr/include/doctest.h" ] ; then
    echo "Compiling the whole arsenalgear code..."
    if ! make ; then
        echo "Compilation failed!"
        exit
    fi
elif [ -f "/usr/include/doctest/doctest.h" ] ; then
    echo "Doctest is installed in /usr/include/doctest folder, move it in /usr/include in order to correctly use it for the library tests!"
    echo "Compiling only the main code of arsenalgear (this is not a problem for the installation)..."
    if ! make $main ; then
        echo "Compilation failed!"
        exit
    fi
else
    echo "Doctest is not installed, cannot compile the test codes!"
    echo "Compiling only the main code of arsenalgear (this is not a problem for the installation)..."
    if ! make $main ; then
        echo "Compilation failed!"
        exit
    fi
fi
echo ""

#====================================================
#     SAVING FILES INTO THE SYSTEM
#====================================================
include_var=$(stat -c%s "include")
lib_var=$(stat -c%s "lib")
var=$(expr $include_var + $lib_var)
read -p "Installation of arsenalgear will take up $var bytes of disk space. Would you like to continue (y/n)? " word
if [ $word == "y" ] || [ $word == "Y" ] ; then
    sudo echo "Installing arsenalgear header files into /usr/local/include folder..."
    sudo mkdir -p /usr/local/include/arsenalgear
    if ! ( sudo cp -r include/* /usr/local/include/arsenalgear ) ; then
        echo "Cannot install the header file into /usr/local/include position of the system!"
    fi
    echo "Installing arsenalgear lib into /usr/local/lib folder..."
    if ! ( sudo cp lib/* /usr/local/lib ) ; then
        echo "Cannot install the library into /usr/local/lib position of the system!"
    fi
else
    echo "Installation has been canceled!"
    exit
fi
echo ""

#====================================================
#     INSTALLATION COMPLETED
#====================================================
echo "Arsenalgear has been succesfully installed!"
echo ""
echo "To compile any C++ program with this library, use:"
echo ""
echo "           g++ program.cpp -larsenalgear"
echo ""
echo "If you use a library component which uses threads:"
echo ""
echo "           g++ program.cpp -larsenalgear -pthread"
echo ""
echo "Enjoy! :)"
echo ""