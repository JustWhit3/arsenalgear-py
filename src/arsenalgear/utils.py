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
#     Doing tests
#################################################
if __name__ == "__main__":
    doctest.testmod()