#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:36:00 2022
Author: Gianluca Bianco
"""

#################################################
#     Libraries
#################################################
import multiprocessing as multi
import numpy as np
import doctest
import itertools

#################################################
#     MultiProcesses
#################################################
def MultiProcesses( *functions ):
    """
    Function used to parallelize more functions.
    
    Args:
        *functions (function): the n processes to be sent in parallel.
    """
    
    # Variables
    processes = np.array( [] )
    
    # Sending processes in parallel
    for function in functions:
      process = multi.Process( target = function )
      process.start()
      processes = np.append( processes, process )
      
    # Joining processes
    for process in processes:
      process.join()

#############################################################
#    chunker
#############################################################
def chunker( it, size ):
    """
    Function uses to allow the selection of a bunch of jobs to be executed in parallel.

    Args:
        it (any): a list of objects through which iterate.
        size (int): the amount of jobs to be executed in parallel.

    Yields:
        tuple: a tuple used for iteration.
    """
    
    # Variables
    it = iter( it )
    
    # Selecting a bunch of jobs
    while True:
        p = tuple( itertools.islice( it, size ) )
        if not p:
            break
        yield p

      
#################################################
#     Doing tests
#################################################
if __name__ == "__main__":
    doctest.testmod()