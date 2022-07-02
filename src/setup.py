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
    version = "1.2.2",
    description = "A library containing general purpose Python utils",
    author = "Gianluca Bianco",
    author_email = 'biancogianluca9@gmail.com',
    url = 'https://justwhit3.github.io/', 
    download_url = 'https://github.com/JustWhit3/arsenalgear/archive/refs/tags/v1.2.2.zip',
    license = "MIT",
    install_requires = [ 
                        "matplotlib>=3.1.2", 
                        "numpy>=1.17.4", 
                        "scipy==1.6.2",
                        "termcolor==1.1.0",
                        "tqdm>=4.64.0"
                       ],
    classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Software Development',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.8',
    ]
)