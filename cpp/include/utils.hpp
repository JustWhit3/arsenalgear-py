#ifndef UTILS_HPP
#define UTILS_HPP

// Extra headers
#include <exprtk.hpp>

// STD headers
#include <stdexcept>
#include <functional>
#include <type_traits>
#include <vector>

namespace agr
 {
  //====================================================
  //     MAXPTR
  //====================================================
  // Function used to find the maximum value of a generic pointer containing listed values.
  // NB: second argument is the pointer dimension.
  template <typename T>
  extern inline T maxptr ( T *ptr, int a )
   {
    if ( a == 1 ) return *ptr;
    return *ptr > ( a = maxptr ( ptr + 1, a - 1 ) ) ? *ptr : a;
   }

  //====================================================
  //     RUNTIME_THROWER
  //====================================================
  // Function used to throw customized runtime error.
  template <typename T_var>
  extern inline std::runtime_error runtime_error_func( const std::string& beg, T_var variable, const std::string& end )
   {
    static std::string error = beg + 
                               static_cast <std::string>(" \"") + 
                               static_cast <std::string>( variable ) +
                               static_cast <std::string>( "\" " ) + 
                               end;

    return std::runtime_error( error ); 
   }

  //====================================================
  //     CHECK_CONDITION
  //====================================================
  // Function to check if a condition is verified and in positive case, return it, else return other.
  template <typename T>
  extern inline T check_condition( const std::function <bool()>& condition, const T& return_it, const T& return_false )
   {
    if( condition() ) return return_it;
    else return return_false;
   }

  //====================================================
  //     ISFLOATINGPOINT
  //====================================================
  // Function to check if an expression is a floating point or not.
  template <typename T>
  extern inline bool isFloatingPoint( const T& expression )
   {
    return std::is_floating_point <T>::value;
   }

  //====================================================
  //     ONE
  //====================================================
  // Function to find the incremented unit of a loop.
  template <typename T>
  extern inline T one( const T& iterating_var )
   {
    static std::vector<T> counter_( 2 );

    if( isFloatingPoint( iterating_var ) )
     {
      if( counter_.size() < 2 ) counter_.push_back( iterating_var );
      if( counter_.size() == 2 ) return abs( abs( counter_.front() ) - abs( counter_.back() ) );
      return static_cast <T> ( NULL );
     }
    return 1;
   }


  

  //====================================================
  //     PARSED_F
  //====================================================
  // Function used to parse a mathematical function f(x,y).
  template <typename T_str, typename T_var>
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