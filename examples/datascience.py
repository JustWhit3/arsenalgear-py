#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Ape 15 12:28:00 2022
Author: Gianluca Bianco
"""

#====================================================
#     MODULES
#====================================================

# Standard libraries
import numpy as np

# Arsenalgear libraries
from arsenalgear import datascience as ds

#====================================================
#     Data Science
#====================================================
def datascience():
    print( "Not easy to produce AMS score or plots, see repository JustWhit3/higgs-decay-classification for an example." )
    print()
    array = np.array([1, 1, 1, 1, 1, 1, 42, 1, 1])
    print( "Removing outliers from array {}: {}".format( array, ds.RemoveOutliers( array, 2 ) ) )

#====================================================
#     Main
#====================================================
def main():
    datascience()
        
if __name__ == "__main__":
    main()