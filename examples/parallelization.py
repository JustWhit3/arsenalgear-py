#!/bin/python3

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