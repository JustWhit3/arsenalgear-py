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
from arsenalgear import plotter as pt

#====================================================
#     Plotter
#====================================================
def plotter():
    print( "Plotting cos(x) + i + sin(x): " )
    pt.plotter_complex( "np.cos(x)", "np.sin(x)", 0, np.pi, 0, 1 )

#====================================================
#     Main
#====================================================
def main():
    plotter()
        
if __name__ == "__main__":
    main()