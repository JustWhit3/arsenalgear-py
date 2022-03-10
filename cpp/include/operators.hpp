#ifndef OPERATORS_HPP
#define OPERATORS_HPP

// STD headers
#include <string>

//====================================================
//     OPERATOR * DEFINITION
//====================================================
template <typename T>
extern std::string operator *( const T& generic_string, unsigned int integer );

template <typename T>
extern std::string operator *( unsigned int integer, const T& generic_string );

#endif