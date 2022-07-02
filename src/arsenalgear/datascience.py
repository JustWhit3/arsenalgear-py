#!/bin/python3
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
import doctest
from tqdm import tqdm

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
    
#############################################################
#    RemoveOutliers
#############################################################
def RemoveOutliers( array, max_deviations ):
    """
    Function used to remove outliers from an array.

    Args:
        array (numpy.array): the interested array.
        max_deviations (int): the maximum number of std.

    Returns:
        numpy.array: the array without outliers.
        
    Testing:
        >>> RemoveOutliers( np.array([1, 1, 1, 1, 1, 1, 42, 1, 1]), 2 )
        array([1, 1, 1, 1, 1, 1, 1, 1])
        >>> RemoveOutliers( np.array([20220314062656, 20220314092546, 20220314092736, 20220314092928, 20220314093120, 20220314092407, 20220314092642, 20220314092831, 20220314093026, 20220314094935]), 2 )
        array([20220314092546, 20220314092736, 20220314092928, 20220314093120,
               20220314092407, 20220314092642, 20220314092831, 20220314093026,
               20220314094935])
        >>> RemoveOutliers( np.array([20220314085233, 20220314092407, 20220314092547, 20220314092643, 20220314092738, 20220314092832, 20220314092930, 20220314093026, 20220314093121, 20220314094315]), 2 )
        array([20220314092407, 20220314092547, 20220314092643, 20220314092738,
               20220314092832, 20220314092930, 20220314093026, 20220314093121,
               20220314094315])
        >>> RemoveOutliers( np.array([20220314063832, 20220314092412, 20220314092551, 20220314092647, 20220314092741, 20220314092836, 20220314092933, 20220314093031, 20220314093125, 20220314102110]), 1 )
        array([20220314092412, 20220314092551, 20220314092647, 20220314092741,
               20220314092836, 20220314092933, 20220314093031, 20220314093125])
    """
    
    mean = np.mean( array )
    std_dev = np.std( array )
    zero_based = abs( array - mean ) # Normalize array around 0
    
    return array[ zero_based < max_deviations * std_dev ]

#############################################################
#    RemoveOutliersDF
#############################################################
def RemoveOutliersDF( dataframe, max_deviations, show_progressb = True ):
    """
    Function used to remove outliers from a particular dataframe.

    Args:
        dataframe (pandas.DataFrame): the pandas dataframe.
        max_deviations (int): the maximum number of std.
        show_progressb (boolean): set progressbar visualization to True / False.

    Returns:
        pandas.DataFrame: the modified dataframe.
        
    Testing:
        >>> df = pd.DataFrame()
        >>> df = df.append( { "Channel": 0, "20220314063832": 0, "20220314092412": 0, "20220314092551": 0, "20220314092647": 0, "20220314092741": 0, "20220314092836": 0, "20220314092933": 0, "20220314093031": 0, "20220314093125": 0, "20220314102110": 0 }, ignore_index = True )
        >>> df = RemoveOutliersDF( df, 1, show_progressb = False )
        >>> df.columns
        Index(['20220314092412', '20220314092551', '20220314092647', '20220314092741',
               '20220314092836', '20220314092933', '20220314093031', '20220314093125',
               'Channel'],
              dtype='object')
    """
    
    new_dataframe = dataframe.loc[ :, dataframe.columns != "Channel" ]
        
    for column in tqdm( new_dataframe.columns, disable = not show_progressb ):
        if int( column ) not in RemoveOutliers( new_dataframe.columns.astype( int ) , 1 ):
            dataframe = dataframe.drop( labels = column, axis = 1 )

    return dataframe


#################################################
#     Doing tests
#################################################
if __name__ == "__main__":
    doctest.testmod()