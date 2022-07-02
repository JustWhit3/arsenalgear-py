#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:18:00 2022
Author: Gianluca Bianco
"""

#################################################
#     Libraries
#################################################
import parser
import doctest
from termcolor import colored
import numpy as np
import math

#################################################
#     Orthogonal polynomials functions
#################################################
def Hermite( x, n ):
    """
    Function used to compute the Hermite polynomials.
    
    Args:
        x (any): variable.
        n (int): polynomials order
    Returns:
    
        any: returns the value of the polynomials at a given order for a given variable value.
        
    Testing:
        Already tested in some functions of the "functions.py" library.
    """
    
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * Hermite( x, n-1 ) - 2 * ( n-1 ) * Hermite( x, n-2 )
    
def Chebyshev( x, n ):
    """
    Function used to compute the Chebyshev polynomials.
    
    Args:
        x (any): variable.
        n (int): polynomials order
        
    Returns:
        any: returns the value of the polynomials at a given order for a given variable value.
        
    Testing:
        Already tested in some functions of the "functions.py" library.
    """
    
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * Chebyshev( x, n-1 ) - Chebyshev( x, n-2 )
    
def Legendre( x, n ): 
    """
    Function used to compute the Legendre polynomials.
    
    Args:
        x (any): variable.
        n (int): polynomials order
        
    Returns:
        any: returns the value of the polynomials at a given order for a given variable value.
        
    Testing:
        Already tested in some functions of the "functions.py" library.
    """
    
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ( ( ( 2 * n ) - 1 ) * x * Legendre( n - 1, x ) - ( n - 1 ) * Legendre( n-2, x ) ) / float( n )
    
def Laguerre( x, n ): 
    """
    Function used to compute the Laguerre polynomials.
    Args:
        x (any): variable.
        n (int): polynomials order
    Returns:
        any: returns the value of the polynomials at a given order for a given variable value.
        
    Testing:
        Already tested in some functions of the "functions.py" library.
    """
    
    if n == 0:
        return 1
    elif n == 1:
        return 1 - x
    else:
        return ( ( ( 2 * n + 1 - x ) * Laguerre( x, n - 1 ) ) - x * Laguerre( x, n - 2 ) ) / ( n + 1 )
    
#################################################
#     "IsInBounds" function
#################################################
def IsInBounds( value, min_, max_ ):
    """
    Function to check if a value is in certain bounds.
    
    Args:
        value (any): the interested value.
        min (any): min value.
        max (any): max value.
        
    Returns:
        bool: return true if is in the bound, otherwise false.
        
    Testing:
        >>> IsInBounds( 3, 1, 5 )
        True
        >>> IsInBounds( 2.3, -2, 3 )
        True
        >>> IsInBounds( 1, 2, 3 )
        False
    """
    
    return min_ <= value <= max_

#################################################
#     "e_parser" function
#################################################
def e_parser( real_part, imaginary_part, n, x ):
    """
    Returns the complex value of a parsed expression.
    
    Args:
        real_part (string): mathematical real expression part.
        imaginary_part (string): mathematical imaginary expression part.
        n (int): wave function index.
        x (any): expression variable.
        
    Returns:
        complex: returns the value of a complex parsed expression for an index n and variable x.
        
    Testing:
        >>> e_parser( "pow( x, n )", "0", 2, 2 )
        (4+0j)
        >>> e_parser( "n*np.cos( x )", "3*n", 2, np.pi )
        (-2+6j)
        >>> e_parser( "n*np.cos( k )", "3*n", 2, np.pi )
        Traceback (most recent call last):
            ...
        NameError: name 'k' is not defined
        >>> e_parser( "n*np.cos( x )", "3*z", 2, np.pi )
        Traceback (most recent call last):
            ...
        NameError: name 'z' is not defined
        >>> e_parser( "os.system", "0", 0, 1 )
        Traceback (most recent call last):
            ...
        RuntimeError: \033[31mDon't parse os.system strings! It is dangerous!\033[0m
    """
    
    if "os.system" in real_part or "os.system" in imaginary_part:
        raise RuntimeError( colored( "Don't parse os.system strings! It is dangerous!", "red" ) )
    
    real_p = parser.expr( real_part ).compile()
    imag_p = parser.expr( imaginary_part ).compile()
    
    return eval( real_p ) + eval( imag_p ) * 1j

#################################################
#     "kronecker" function
#################################################
def kronecker( i, j ):
    """
    Definition of the Kronecker delta function for two numbers i and j.
    
    Args:
        i (int): index i
        j (int): index j
        
    Returns:
        int: return the Kronecker delta value.
        
    Testing:
        >>> kronecker( 2, 2 )
        1
        >>> kronecker( 1, 2 )
        0
    """
    
    if i == j:
        return 1
    else:
        return 0
    
#############################################################
#    OrderOfMagnitude
#############################################################
def OrderOfMagnitude( number ):
    """
    Function used to find the order of magnitude of a number.

    Args:
        number (any): the input number.

    Returns:
        int: the order of magnitude of the number.
        
    Testing:
        >>> OrderOfMagnitude( 1E+10 )
        10
        >>> OrderOfMagnitude( 1E-10 )
        -10
        >>> OrderOfMagnitude( 145 )
        2
    """
    
    return math.floor( math.log( number, 10 ) )

    
#################################################
#     Doing tests
#################################################
if __name__ == "__main__":
    doctest.testmod()