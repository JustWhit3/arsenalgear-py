# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:18:00 2022
Author: Gianluca Bianco
"""

#################################################
#     Libraries
#################################################
import numpy as np
import matplotlib.pyplot as plt

#################################################
#     "AMS_score" function
#################################################
def AMS_score( x_cut, predictions, label_vectors, weights ):
    """
    Function used to compute the AMS score.

    Args:
        x_cut ( double ): s the cut parameter of the AMS. It ranges from 0.5 to 1 in steps of 0.1.
        predictions ( numpy array ): is a binary array, defined from the set of data that we're considering.
        label_vectors ( numpy array ): is a binary array constructed from the dataset, used for each model, that distinguishes an event between signal and background.
        weights ( numpy array ): it takes the weights associated to each data of my dataset.

    Returns:
        double: returns the AMS score.
    """
    
    b_reg = 10
    
    s = sum( weights[ ( predictions[ :, 1 ] > x_cut )  & ( label_vectors[ :, 1 ] == 1 ) ] )
    b = sum( weights[ ( predictions[ :, 1 ] > x_cut )  & ( label_vectors[ :, 1 ] == 0 ) ] )

    AMS = np.sqrt( 2 *( ( s + b + b_reg ) * np.log( 1 + s / ( b + b_reg ) ) -s ) )
    
    return AMS

#################################################
#     "plot_AMS" function
#################################################
def plot_AMS( predictions, label_vectors, weights ):
    """
    Function used to plot the AMS function.

    Args:
        predictions ( numpy array ): is a binary array, defined from the set of data that we're considering.
        label_vectors ( numpy array ): is a binary array constructed from the dataset, used for each model, that distinguishes an event between signal and background.
        weights ( numpy array ): it takes the weights associated to each data of my dataset.
    """
    
    x = np.arange( 0.5, 1, 1e-2 )
    y = np.array( [ AMS_score( x_values, predictions, label_vectors, weights ) for x_values in x ] )
    
    plt.plot( x, y )
    plt.xlabel( "Cut Parameter" )
    plt.ylabel( "AMS Score" )
    plt.grid()
    
    print( "The best AMS Score is {:.3f} at a Cut Parameter of {:.2f}".format( max( y ), x[ np.argmax( y ) ] ) )