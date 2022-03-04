#define DOCTEST_CONFIG_SUPER_FAST_ASSERTS

// My headers
#include "../include/operators.hpp"

// Extra headers
#include <doctest.h>

// STD headers
#include <string>

//====================================================
//     OPERATOR * REDEFINITION
//====================================================
TEST_CASE( "Testing the * redefinition for string multiplication by an integer." )
 {
  const std::string example = "a"; 

  CHECK_EQ( example * 3, "aaa" );
  CHECK_EQ( 3 * example, "aaa" );
 }