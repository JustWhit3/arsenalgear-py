#ifndef NUMERICS_HPP
#define NUMERICS_HPP

// STD headers
#include <cmath>

namespace agr
 {
  //====================================================
  //     ROUNDOFF
  //====================================================
  // Function to round a floating point to n-th decimal place.

  // 1-st overload:
  template <typename T>
  extern inline T roundoff( const T& value, const unsigned char prec )
   {
    T pow_10 = pow( 10.0f, static_cast <T> ( prec ) );

    return round( value * pow_10 ) / pow_10;
   }

  // 2-nd overload:
  template <typename T>
  extern inline T roundoff( const T& value )
   {
    if( value < 0 ) return ceil( value - 0.5 );
    else return floor( value + 0.5 );
   }

  //====================================================
  //     ISINBOUNDS
  //====================================================
  // Function to check if a number lies in a certain bound or not.
  template <typename T>
  extern inline bool IsInBounds( const T& value, const T& low, const T& high )
   {
    return !( value < low ) && ( value < high );
   } 
 }

#endif