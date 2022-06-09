#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:18:00 2022
Author: Gianluca Bianco
"""

#################################################
#     Libraries
#################################################
from termcolor import colored
from mathematics import e_parser
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sci

#################################################
#     "plotter_complex" function
#################################################
def plotter_complex( real_part, imaginary_part, a, b, n, coefficient ):
    """
    Function used to plot a given wave-function for an index n.
    Args:
        real_part (string): mathematical real expression part.
        imaginary_part (string): mathematical imaginary expression part.
        a (any): lower integration extreme.
        b (any): higher integration extreme.
        n (int): wave function index.
        coefficient (any): value of the normalization coefficient.
    Returns:
        plot: the wave-function plot for the index n is returned.
    """
    
    if coefficient != colored( "Error, division by 0!", "red" ):
        
        if a == -np.inf and b != np.inf:
            x = np.arange( -10, b, ( ( b+10 ) / 10 ) )
        elif a != -np.inf and b == np.inf:
            x = np.arange( a, 10, ( ( 10-a ) / 10 ) )
        elif a == -np.inf and b == np.inf:
            x = np.arange( -10, 10, ( ( 20 ) / 10 ) )
        else:
            x = np.arange( 10*a, 10*b, ( ( 10*( b-a ) ) / 10 ) )

        def func( x ):
            return coefficient * e_parser( real_part, imaginary_part, n, x )
        
        my_label = "Normalized wave-function f(x) for n = " + str( n )
        plt.figure( figsize = ( 8, 6 ), dpi = 80 )
        plt.xlabel( "Re: f(x)" )
        plt.ylabel( "Im: f(x)" )
        plt.title( my_label )

        if real_part == "0" and imaginary_part != "0":
            X_Y_Spline = sci.make_interp_spline( x, np.imag( func( x ) ) )
            X = np.linspace( x.min(), x.max(), 500 )
            Y = X_Y_Spline( X )
        
            plt.xlabel( "x" )
            plt.ylabel( "Im: f(x)" )
            plt.plot( X, Y, color = "green" )
        elif real_part != "0" and imaginary_part == "0":
            X_Y_Spline = sci.make_interp_spline( x, np.real( func( x ) ) )
            X = np.linspace( x.min(), x.max(), 500 )
            Y = X_Y_Spline( X )
        
            plt.xlabel( "x" )
            plt.ylabel( "Re: f(x)" )
            plt.plot( X, Y, color = "green" )
        else:
            X = np.real( func( x ) )
            Y = np.imag( func( x ) )
            tck, u = sci.splprep( [ X, Y ], s = 0 )
            unew = np.arange( 0, 1.01, 0.01 )
            out = sci.splev( unew, tck )
            
            plt.plot( X, Y, 'x', out[0], out[1], color = "green" )

        plt.show()