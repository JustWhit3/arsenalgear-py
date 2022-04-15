
#====================================================
#     MODULES
#====================================================

# Standard libraries
import sys
import numpy as np

# Arsenalgear libraries
sys.path.append("arsenalgear/")
from arsenalgear import mathematics as mt
from arsenalgear import datascience as ds
from arsenalgear import plotter as pt
from arsenalgear import parallelization as paral

#====================================================
#     Mathematics
#====================================================
def mathematics():
    print( "#################################################" )
    print( "#     Mathematics                                " )
    print( "#################################################" )
    print()
    print( "Hermite polynomial in x = 3 and n = 2: ", mt.Hermite( 3, 2 ) )
    print( "Chebyshev polynomial in x = 3 and n = 2: ", mt.Chebyshev( 3, 2 ) )
    print( "Legendre polynomial in x = 3 and n = 2: ", mt.Legendre( 3, 2 ) )
    print( "Laguerre polynomial in x = 3 and n = 2: ", mt.Laguerre( 3, 2 ) )
    print()
    print( "Check if 3 is between 1 and 4: ", mt.IsInBounds( 3, 1, 4 ) )
    print()
    print( "Parsing ( 3*n*x + i * x ) in x = 1 and n = 2:", mt.e_parser( "3*n*x", "x", 1, 2 ) )
    print()
    print( "kronecker delta for i = 1 and j = 0: ", mt.kronecker( 1, 0 ) )
    print()

#====================================================
#     Data Science
#====================================================
def datascience():
    print( "#################################################" )
    print( "#     Data Science                               " )
    print( "#################################################" )
    print()
    print( "Not easy to produce AMS score or plots, see repository JustWhit3/higgs-decay-classification for an example." )
    print()
    array = np.array([1, 1, 1, 1, 1, 1, 42, 1, 1])
    print( "Removing outliers from array {}: {}".format( array, ds.RemoveOutliers( array, 2 ) ) )
    print()

#====================================================
#     Plotter
#====================================================
def plotter():
    print( "#################################################" )
    print( "#     Plotter                                    " )
    print( "#################################################" )
    print()
    print( "Plotting cos(x) + i + sin(x): " )
    pt.plotter_complex( "np.cos(x)", "np.sin(x)", 0, np.pi, 0, 1 )
    print()
    
#====================================================
#     Parallelization
#====================================================
def process_1():
    print( "First process!" )
    
def process_2():
    print( "Second process" )
    
def parallelization():
    print( "#################################################" )
    print( "#     Parallelization                            " )
    print( "#################################################" )
    print()
    print( "Parallelizing two processes: " )
    paral.MultiProcesses( process_1, process_2 )
    print()

#====================================================
#     Main
#====================================================
def main():
    mathematics()
    datascience()
    plotter()
    parallelization()
        
if __name__ == "__main__":
    main()