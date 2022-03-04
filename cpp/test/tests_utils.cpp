#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#define DOCTEST_CONFIG_SUPER_FAST_ASSERTS

// My headers
#include "../include/utils.hpp"

// Extra headers
#include <doctest.h>

// STD headers
#include <string>
#include <vector>

//====================================================
//     MAXPTR
//====================================================
TEST_CASE( "Testing the maxptr function." )
 {
  int *p = new int[5];
  double *t = new double[2];

  for( int i = 0; i < 5; i++ ) p[i] = i;
  for( int i = 0; i < 2; i++ ) t[i] = ( i + 50 ) / 10;

  CHECK_EQ( agr::maxptr( p, 5 ), 4 );
  CHECK_EQ( agr::maxptr( t, 2 ), 5 );
 }

//====================================================
//     CHECK_CONDITION
//====================================================
TEST_CASE_TEMPLATE( "Testing the check_condition function.", T, std::string, const char* )
 {
  const T test_string = "nice", null_str = "";

  CHECK_EQ( agr::check_condition( [](){ return 3 < 4; }, test_string, null_str ), test_string );
  CHECK_EQ( agr::check_condition( [](){ return 3 > 4; }, test_string, null_str ), null_str );
 }

//====================================================
//     ISFLOATINGPOINT
//====================================================
TEST_CASE_TEMPLATE( "Testing the isFLoatingPoint function.", T, double, float, long double )
 {
  T type = 0.;
  const int integer = 2;
  
  CHECK( ! agr::isFloatingPoint( integer ) );
  CHECK( agr::isFloatingPoint( type ) );
 }

//====================================================
//     RUNTIME_ERROR_FUNC
//==================================================== 
TEST_CASE_TEMPLATE( "Testing the runtime_error_func function.", T, std::string, const char* )
 {
  T var = "this";
  const std::string test_string = "first" + static_cast <std::string>(" \"") +
                                  static_cast <std::string>( var ) + 
                                  static_cast <std::string>( "\" " ) +
                                  "second" +
                                  "\n";
                       
  CHECK_THROWS_AS( throw( agr::runtime_error_func( "first", var, "second" ) ), std::runtime_error );
  CHECK_THROWS_MESSAGE( throw( agr::runtime_error_func( "first", var, "second" ) ), test_string );
 }

//====================================================
//     ONE
//==================================================== 
TEST_CASE( "Testing the one function." )
 {
  std::vector <int> v { 1, 2, 3, 4 };
  std::vector <int> counter_ {};

  for( const auto & element: v )
   {
    if( counter_.size() == 2 )
     {
      CHECK_EQ( agr::one( element ), abs( abs( counter_.front() ) - abs( counter_.back() ) ) );
     }
    counter_.push_back( element );
   }
 }

//============================================
//     PARSED_F
//============================================
TEST_CASE( "Testing the parsed_f function." )
 {
  CHECK_EQ( agr::parsed_f( "x + y", 1, 2 ), 3 );
  CHECK_EQ( agr::parsed_f( "cos( x ) - sin( y )", M_PI, M_PI/2 ), -2 );
  CHECK_EQ( agr::parsed_f( "3*( cos( x ) - sin( y ) )", M_PI, M_PI/2 ), -6 );

  static const double p = agr::parsed_f( "3*( cos( x ) - sin( y ) )", M_PI, M_PI/2 );
  CHECK_EQ( p, -6 );
 }