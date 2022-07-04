#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 2 10:58:00 2022
Author: Gianluca Bianco
"""

#====================================================
#     MODULES
#====================================================
from arsenalgear.utils import TimeToInt, IntToTime
  
#====================================================
#     Parallelization
#====================================================
def utils():
    
    # TimeToInt
    time_str_1 = "2022.03.14 09:20:00"
    time_int_1 = TimeToInt( time_str_1 )
    print( "Converting \"{}\" into an int: {}".format( time_str_1, time_int_1 ) )
    
    # IntToTime
    time_int_2 = 20220314092000
    time_str_2 = IntToTime( time_int_2 )
    print( "Reconverting {} into a string: \"{}\"".format( time_int_2, time_str_2 ) )

#====================================================
#     Main
#====================================================
def main():
    utils()
        
if __name__ == "__main__":
    main()