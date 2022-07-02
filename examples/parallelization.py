#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Ape 15 12:28:00 2022
Author: Gianluca Bianco
"""

#====================================================
#     MODULES
#====================================================
from arsenalgear import parallelization as paral
    
#====================================================
#     Parallelization
#====================================================
def process_1():
    print( "First process!" )
    
def process_2():
    print( "Second process" )
    
def parallelization():
    print( "Parallelizing two processes: " )
    paral.MultiProcesses( process_1, process_2 )

#====================================================
#     Main
#====================================================
def main():
    parallelization()
        
if __name__ == "__main__":
    main()