#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#define DOCTEST_CONFIG_SUPER_FAST_ASSERTS

// My headers
#include "../include/utils.hpp"
#include "../include/constants.hpp"

// Extra headers
#include <doctest.h>

// STD headers
#include <string>
#include <vector>

using namespace std::string_literals;

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
  const std::string test_string = "\033[31mfirst" + " \""s +
                                  "\033[1m" + static_cast <std::string>( var ) + 
                                  "\033[22m" + "\" "s +
                                  "second\033[39m" +
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

//====================================================
//     MULTI
//==================================================== 
TEST_CASE( "Testing the multi function." )
 {
  CHECK_EQ( agr::multi( "this", 2 ), "thisthis" );
  CHECK_EQ( agr::multi( "a ", 5 ), "a a a a a " );
 }