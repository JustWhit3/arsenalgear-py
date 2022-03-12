
#====================================================
#     MODULES
#====================================================
import sys
import numpy as np
sys.path.append("arsenalgear/")
from arsenalgear import mathematics as mt
from arsenalgear import machinelearning as ml
from arsenalgear import plotter as pt


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
#     Machine learning
#====================================================
def machinelearning():
    print( "#################################################" )
    print( "#     Machine Learning                           " )
    print( "#################################################" )
    print()
    print( "Not easy to produce AMS score or plots, see repository JustWhit3/higgs-decay-classification for an example." )
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
#     Main
#====================================================
def main():
    mathematics()
    machinelearning()
    plotter()
        
if __name__ == "__main__":
    main()