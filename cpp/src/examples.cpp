// My headers
#include "../include/math.hpp"
#include "../include/operators.hpp"
#include "../include/stream.hpp"
#include "../include/utils.hpp"
#include "../include/constants.hpp"

// STD headers
#include <iostream>
#include <cmath>
#include <string>

//====================================================
//     MATH
//====================================================
void math()
 {
  std::cout << std::endl << "======================================================" << std::endl
                         << "     MATH                                             " << std::endl
                         << "======================================================" << std::endl
                         << std::endl;

  // Roundoff
  std::cout << "Round " << 3.546 << " until 2-nd precision digits after comma: " 
            << agr::roundoff( 3.546, 2 ) << "." << std::endl << std::endl;

  // isInBounds
  std::cout << "Check if 3 is between 2 and 4: " << agr::IsInBounds( 3, 2, 4 ) << " (True)." 
            << std::endl << std::endl;

  // parsed_f
  std::cout << "Parsing cos(x) + sin(y) for x=pi/2 and y=pi/4: " << agr::parsed_f( "cos(x)+sin(y)", M_PI/2, M_PI/4 ) 
            << "." << std::endl;
 }

//====================================================
//     OPERATORS
//====================================================
void operators()
 {
  std::cout << std::endl << "======================================================" << std::endl
                         << "     OPERATORS                                        " << std::endl
                         << "======================================================" << std::endl
                         << std::endl;

  // * strings by an integer:
  std::string a = "a";
  std::cout << "Multiplying \"a\" for 5 times: " << a * 5 << "." << std::endl;
 }

//====================================================
//     UTILS
//====================================================
void utils()
 {
  std::cout << std::endl << "======================================================" << std::endl
                         << "     UTILS                                            " << std::endl
                         << "======================================================" << std::endl
                         << std::endl;

  // maxptr
  int *ptr = new int[5];
  std::cout << "Finding max value of this pointer: { ";
  for( int i = 0; i < 5; i++ ) 
   {
    ptr[i] = i;
    std::cout << ptr[i] << agr::empty_space<std::string>;
   }
  std::cout << "} -> " << agr::maxptr( ptr, 5 ) << "." << std::endl << std::endl;

  // runtime_error_func
  // commented since it quit the program. Uncomment to try it:
  // std::cout << "Runtime error function example: ";
  // throw agr::runtime_error_func( "Inserted command", "<command>", "is not supported!" );

  // isFLoatingPoint
  std::cout << "Check if 0.00034 is a floating point: " << agr::isFloatingPoint( 0.00034 ) 
            << " (True)." << std::endl << std::endl;

  // one
  std::cout << "Check incremented value of for( const auto & element: v ) with v vector of dim = 2: ";
  static std::vector <int> v { 1, 2 };

  for( const auto & element: v )
   {
    if( element == 2 ) std::cout << agr::one( element ) << "." << std::endl << std::endl;
   }
 }

//====================================================
//     STREAM
//====================================================
void stream()
 {
  /*std::cout << std::endl << "======================================================" << std::endl
                         << "     STREAM                                           " << std::endl
                         << "======================================================" << std::endl
                         << std::endl;*/

  //Nothing for the moment.
 }

//====================================================
//     MAIN
//====================================================
int main()
 {
  math();
  operators();
  stream();
  utils();
 }