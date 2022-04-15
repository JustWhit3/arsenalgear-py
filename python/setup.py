# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:21:00 2022
Author: Gianluca Bianco
"""

#################################################
#     Libraries
#################################################
from setuptools import find_packages, setup

#################################################
#     Setup settings
#################################################
setup(
    name = "arsenalgear",
    packages = find_packages( include = [ "arsenalgear" ] ),
    version = "1.0.1",
    description = "A library containing general purpose utils I developed for other projects, using different languages",
    author = "Gianluca Bianco",
    license = "MIT",
    install_requires = [ 
                        "matplotlib>=3.1.2", 
                        "numpy>=1.17.4", 
                        "scipy==1.6.2",
                        "termcolor==1.1.0"
                       ],
)