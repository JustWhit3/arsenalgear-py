#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Ape 15 12:28:00 2022
Author: Gianluca Bianco
"""

#################################################
#     Libraries
#################################################
import numpy as np
import doctest
import os
import matplotlib.pyplot as plt

#############################################################
#    TimeToInt
#############################################################
def TimeToInt( time_string ):
    """
    Function used to convert a time-string into an integer.

    Args:
        time_string ( string ): the time-string.

    Returns:
        int: the converted time-string into int.
    
    Testing:
        >>> TimeToInt( "2022.03.14 09:20:00.000" )
        20220314092000000
        >>> TimeToInt( "2022.03.14 09:20:00" )
        20220314092000
        >>> TimeToInt( "2022.03.14 09:20:00" ) + 3
        20220314092003
    """
    
    time_string = time_string.replace( ":", "" )
    time_string = time_string.replace( ".", "" )
    time_string = time_string.replace( " ", "" )
    
    return int( time_string )

#############################################################
#    IntToTime
#############################################################
def IntToTime( time_int ):
    """
    Function used to convert an integer into a time-string.

    Args:
        time_int ( int ): the integer.

    Returns:
        string: the converted time-string.
        
    Testing:
        >>> IntToTime( 20220314092000 )
        '2022.03.14 09:20:00'
        >>> IntToTime( 20220314094000 )
        '2022.03.14 09:40:00'
    """
    
    time_string = str( time_int )
    time_string = time_string[ :4 ] + "." + time_string[ 4: ]
    time_string = time_string[ :7 ] + "." + time_string[ 7: ]
    time_string = time_string[ :10 ] + " " + time_string[ 10: ]
    time_string = time_string[ :13 ] + ":" + time_string[ 13: ]
    time_string = time_string[ :16 ] + ":" + time_string[ 16: ]
    
    return time_string

#################################################
#     save_img
#################################################
def save_img( img_name, save_path, tight = False ):
    """
    Function used to save a specific plot "img_name" into a specific directory "save_path".
    Args:
        img_name (str): The name of the plot to be saved. No file extension needed.
        save_path (str): The path in which the plot should be saved.
        tight (bool, optional): Set "tight" option for plot into True or False. Default to False.
    
    Testing:
        >>> a = [ 1, 2, 3, 4 ]
        >>> _ = plt.plot( a )
        >>> save_img( "save_img_test", "../../img/tests" )
        >>> os.path.exists( "../img/tests/save_img_test.png" )
        True
    """
    
    # Create the path if it doesn't exist yet
    if not os.path.exists( save_path ):
        os.makedirs( save_path )

    # Save the plot
    if tight == True:
        plt.savefig( "{}/{}.png".format( save_path, img_name ), bbox_inches = "tight", dpi = 100 )
    elif tight == False:
        plt.savefig( "{}/{}.png".format( save_path, img_name ), dpi = 100 )

#################################################
#     Doing tests
#################################################
if __name__ == "__main__":
    doctest.testmod()