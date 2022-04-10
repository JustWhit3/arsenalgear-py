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
  std::cout << "\n" << "======================================================" << "\n"
                    << "     MATH                                             " << "\n"
                    << "======================================================" << "\n"
                    << "\n";

  // Roundoff
  std::cout << "Round " << 3.546 << " until 2-nd precision digits after comma: " 
            << agr::roundoff( 3.546, 2 ) << "." << "\n\n";

  // isInBounds
  std::cout << "Check if 3 is between 2 and 4: " << agr::IsInBounds( 3, 2, 4 ) << " (True)." 
            << "\n\n";

  // parsed_f
  std::cout << "Parsing cos(x) + sin(y) for x=pi/2 and y=pi/4: " << agr::parsed_f( "cos(x)+sin(y)", M_PI/2, M_PI/4 ) 
            << "." << "\n";
 }

//====================================================
//     OPERATORS
//====================================================
void operators()
 {
  std::cout << "\n" << "======================================================" << "\n"
                    << "     OPERATORS                                        " << "\n"
                    << "======================================================" << "\n"
                    << "\n";

  // * strings by an integer:
  std::string a = "a";
  std::cout << "Multiplying \"a\" for 5 times: " << a * 5 << agr::empty_space<std::string_view> * 5
            << "adding spaces." << "\n";
 }

//====================================================
//     UTILS
//====================================================
void utils()
 {
  std::cout << "\n" << "======================================================" << "\n"
                    << "     UTILS                                            " << "\n"
                    << "======================================================" << "\n"
                    << "\n";

  // maxptr
  int *ptr = new int[5];
  std::cout << "Finding max value of this pointer: { ";
  for( int i = 0; i < 5; i++ ) 
   {
    ptr[i] = i;
    std::cout << ptr[i] << agr::empty_space<std::string>;
   }
  std::cout << "} -> " << agr::maxptr( ptr, 5 ) << "." << "\n\n";

  // runtime_error_func
  // commented since it quit the program. Uncomment to try it:
  // std::cout << "Runtime error function example: ";
  // throw agr::runtime_error_func( "Inserted command", "<command>", "is not supported!" );

  // isFLoatingPoint
  std::cout << "Check if 0.00034 is a floating point: " << agr::isFloatingPoint( 0.00034 ) 
            << " (True)." << "\n\n";

  // one
  std::cout << "Check incremented value of for( const auto & element: v ) with v vector of dim = 2: ";
  static std::vector <int> v { 1, 2 };

  for( const auto & element: v )
   {
    if( element == 2 ) std::cout << agr::one( element ) << "." << "\n\n";
   }

  // multi
  std::cout << "Repeating \"this\" for 3 times_ " << agr::multi( "this", 3 ) << "\n\n";
 }

//====================================================
//     STREAM
//====================================================
void stream()
 {
  /*std::cout << "\n" << "======================================================" << "\n"
                      << "     STREAM                                           " << "\n"
                      << "======================================================" << "\n"

                      << "\n";*/  
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