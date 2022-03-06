#define DOCTEST_CONFIG_SUPER_FAST_ASSERTS

// My headers
#include "../include/math.hpp"

//Extra headers
#include <doctest.h>

//====================================================
//     ROUNDOFF
//==================================================== 
TEST_CASE_TEMPLATE( "Testing the roundoff function.", T, double )
 {
  T var = 3.34;
  T var_2 = 3.456;
  T var_3 = 345.56;

  CHECK_EQ( agr::roundoff( var, 1 ), 3.3 );
  CHECK_EQ( agr::roundoff( var_2, 2 ), 3.46 );
  CHECK_EQ( agr::roundoff( var_3, 1 ), 345.6 );
 }

//============================================
//     ISINBOUNDS
//============================================
TEST_CASE_TEMPLATE( "Testing the IsInBounds function", T, double )
 {
  T var_1 = 3;
  T var_2 = 0.2;
  CHECK( agr::IsInBounds( var_1, 2.9, 3.1 ) );
  CHECK( agr::IsInBounds( var_2, 0.1, 0.21 ) );
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