#ifndef NUMERICS_HPP
#define NUMERICS_HPP

// Extra headers
#include <exprtk.hpp>

// STD headers
#include <cmath>

namespace agr
 {
  //====================================================
  //     ROUNDOFF
  //====================================================
  // Function to round a floating point to n-th decimal place.
  template <typename T>
  extern inline T roundoff( const T& value, const unsigned char prec )
   {
    T pow_10 = pow( 10.0f, static_cast <T> ( prec ) );

    return round( value * pow_10 ) / pow_10;
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

  //====================================================
  //     PARSED_F
  //====================================================
  // Function used to parse a mathematical function f(x,y).
  template <typename T_str>
  extern inline double parsed_f( const T_str& expr, double x, double y )
   {
    static exprtk::rtl::io::file::package<double> fileio_package;

    static exprtk::symbol_table <double> symbol_table;
    symbol_table.add_variable( "x", x );
    symbol_table.add_variable( "y", y );

    static exprtk::expression <double> expression;
    expression.register_symbol_table( symbol_table );
  
    static exprtk::parser <double> parser;
    if ( ! parser.compile( expr, expression ) )
     {
      throw std::runtime_error( "Error in the inserted expression!" );
     }
    
    return expression.value();
   }
 }

#endif