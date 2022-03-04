//My headers
#include "../include/operators.hpp"

//====================================================
//     STRING * INT
//====================================================
//Multiply a string by an integer.
std::string operator * ( const std::string& generic_string, unsigned int integer ) 
 {
  std::string output = "";

  while ( integer -- ) 
   {
    output += generic_string;
   }
   
  return output;
 }

//====================================================
//     INT * STRING
//====================================================
//Multiply an integer by a string.
std::string operator * ( unsigned int integer, const std::string& generic_string ) 
 {
  return generic_string * integer;
 }