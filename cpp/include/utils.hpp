#ifndef UTILS_HPP
#define UTILS_HPP

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
  inline T maxptr ( T *ptr, int ptr_dim )
   {
    if( ptr_dim == 1 ) return *ptr;
    return *ptr > ( ptr_dim = maxptr( ptr + 1, ptr_dim - 1 ) ) ? *ptr : ptr_dim;
   }

  //====================================================
  //     RUNTIME_THROWER
  //====================================================
  // Function used to throw customized runtime error.
  template <typename T>
  inline std::runtime_error runtime_error_func( const std::string& beg, T variable, const std::string& end )
   {
    static std::string error = beg + 
                               static_cast <std::string>(" \"") + 
                               static_cast <std::string>( variable ) +
                               static_cast <std::string>( "\" " ) + 
                               end;

    return std::runtime_error( error ); 
   }

  //====================================================
  //     ISFLOATINGPOINT
  //====================================================
  // Function to check if an expression is a floating point or not.
  template <typename T>
  inline bool isFloatingPoint( const T& expression )
   {
    return std::is_floating_point <T>::value;
   }

  //====================================================
  //     ONE
  //====================================================
  // Function to find the incremented unit of a loop.
  template <typename T>
  inline T one( const T& iterating_var )
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
 }

#endif