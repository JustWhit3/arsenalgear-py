#!/bin/python3

#====================================================
#     MODULES
#====================================================
from arsenalgear import mathematics as mt

#====================================================
#     Mathematics
#====================================================
def mathematics():
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

#====================================================
#     Main
#====================================================
def main():
    mathematics()
        
if __name__ == "__main__":
    main()