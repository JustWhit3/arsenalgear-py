#ifndef OPERATORS_HPP
#define OPERATORS_HPP

// STD headers
#include <string>

namespace agr
 {
  //====================================================
  //     OPERATOR * DEFINITION
  //====================================================
  extern std::string operator * ( const std::string& generic_string, unsigned int integer );
  extern std::string operator * ( unsigned int integer, const std::string& generic_string );
 }

#endif