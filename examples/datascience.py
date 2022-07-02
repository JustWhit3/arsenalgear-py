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
import pandas as pd

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
    print()
    df = pd.DataFrame()
    df = df.append( { "Channel": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "4": 0, "5": 0, "6": 0, "1": 0, "123412": 0 }, ignore_index = True )
    print( "Removing outliers from {}".format( df ) )
    print( "Removed: {}".format( ds.RemoveOutliersDF( df, 1, show_progressb = False ) ) )

#====================================================
#     Main
#====================================================
def main():
    datascience()
        
if __name__ == "__main__":
    main()