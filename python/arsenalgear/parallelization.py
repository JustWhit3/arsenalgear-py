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
      
#################################################
#     Doing tests
#################################################
if __name__ == "__main__":
    doctest.testmod()