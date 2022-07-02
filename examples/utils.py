#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 2 10:58:00 2022
Author: Gianluca Bianco
"""

#====================================================
#     MODULES
#====================================================
from arsenalgear import utils
  
#====================================================
#     Parallelization
#====================================================
def utils():
    
    # TimeToInt
    time_str = "2022-04-12 16:23:45"
    time_int = utils.TimeToInt( time_str )
    print( "Converting \"{}\" into an int: {}".format( time_str, time_int ) )
    
    # IntToTime
    time_int = 20220412162345
    time_str = utils.IntToTime( time_int )
    print( "Reconverting {} into a string: \"{}\"".format( time_int, time_str ) )

#====================================================
#     Main
#====================================================
def main():
    utils()
        
if __name__ == "__main__":
    main()