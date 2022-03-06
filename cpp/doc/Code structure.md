# Code structure

## Table of contents

- [Namespaces](#namespaces)
  - [Arg](#arg)
- [Constants](#constants)
  - [null_str](#nullstr)
  - [empty_space](#emptyspace)
- [Math](#math)
  - [roundoff](#roundoff)
  - [isInBounds](#isinbounds)
  - [parsed_f](#parsed_f)
- [Operators](operators)
  - [std::string * int (and vice-versa)](#std--string---int--and-vice-versa-)
- [Stream](#stream)
  - [null_stream](#nullstream)
- [Utils](#utils)
  - [maxptr](#maxptr)
  - [runtime_error_func](#runtimeerrorfunc)
  - [check_condition](#checkcondition)
  - [isFloatingPoint](#isFloatingPoint)
  - [one](#one)

## Namespaces

### agr

It is a global namespace which contains all the code of the library.

## Constants

### null_str

Header file and source code: [constants.hpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/constants.hpp)

Namespace: `agr`

Complete definition: `template <typename T> extern const T null_str = ""`

Usage: it is used to define the empty string generalizing its type to `std::string` or `const char*` regarding to the context.

Example usage: `agr::null_str<std::string>`

### Empty space

Header file and source code: [constants.hpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/constants.hpp)

Namespace: `agr`

Complete definition: `template <typename T> extern const T empty_space = " "`

Usage: it is used to define the empty string space with different type (`std::string` or `const char*`) regarding to the context.

Example usage: `agr::empty_space<std::string>`

## Math

### roundoff

Header file and source code: [math.hpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/math.hpp)

Namespace: `agr`

Complete definition: `template <typename T> extern inline T roundoff( const T& value, const unsigned char prec )`

Usage: it is used to round the value of a floating point at the `prec` decimal point.

Example usage: `agr::roundoff( 123.4, 2 )`

### isInBounds

Header file and source code: [math.hpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/math.hpp)

Namespace: `agr`

Complete definition: `template <typename T> extern inline bool IsInBounds( const T& value, const T& low, const T& high )`

Usage: it is used to check if a value is the bound [`low`,`high`].

Example usage: `agr::isInBounds( 3.2, 1.0, 5.3 )`

### parsed_f

Header file and source code: [math.hpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/math.hpp)

Namespace: `agr`

Complete definition: `template <typename T> extern inline double parsed_f( const T_str& expr, double x, double y )`

Usage: it is used to parse a string containing a two-variables function signature into a real cpp function in two points.
>**NOTE**: the signature will be changed in order to extend the function to an n-variables function parser.

Example usage: `agr::parsed_f( "cos(x)+sin(y)", M_PI, M_PI/4 )`

## Operators

### std::string * int (and vice-versa)

Header file: [operators.hpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/math.hpp)

Source code: [operators.cpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/src/math.cpp)

Namespace: `agr`

Complete definition (1-st overload): `extern std::string operator * ( const std::string& generic_string, unsigned int integer )`
Complete definition (2-nd overload): `extern std::string operator * ( unsigned int integer, const std::string& generic_string )`

Usage: it is used to allow multiplications of a string by an integer.

Example usage: 

```cpp
std::string a = "this"; 
std::cout << a * 5;
```

## Stream

### null_stream

Header file: [stream.hpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/math.hpp)

Source code: [stream.cpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/src/math.cpp)

Namespace: `agr`

Complete definition (1-st overload): `extern boost::iostreams::stream<boost::iostreams::null_sink> null_stream`

Usage: it is used to define the null-stream.

Example usage: see [here](https://github.com/JustWhit3/osmanip/blob/main/include/manipulators/csmanip.hpp)

## Utils

### maxptr

Header file and source code: [utils.hpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/math.hpp)

Namespace: `agr`

Complete definition (1-st overload): `template <typename T> extern inline T maxptr ( T *ptr, int a )`

Usage: function used to find the maximum value of a pointer of dimension `a`

Example usage: `agr::maxptr( pointer, pointer_dimension )`

### runtime_error_func

Header file and source code: [utils.hpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/math.hpp)

Namespace: `agr`

Complete definition (1-st overload): `template <typename T_var> extern inline std::runtime_error runtime_error_func( const std::string& beg, T_var variable, const std::string& end )`

Usage: function used to throw customized runtime error.

Example usage: `throw agr::runtime_error_func( "This variable", var, "is not supported!" )`

### check_condition

Header file and source code: [utils.hpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/math.hpp)

Namespace: `agr`

Complete definition (1-st overload): `template <typename T> extern inline T check_condition( const std::function <bool()>& condition, const T& return_it, const T& return_false )`

Usage: function used to check if a given expression is true and in positive case return something else return something else.

Example usage: `agr::check_condition( [ = ] { return isFloatingPoint( variable ); }, 1, 100 )`

### isFloatingPoint

Header file and source code: [utils.hpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/math.hpp)

Namespace: `agr`

Complete definition (1-st overload): `template <typename T> extern inline bool isFloatingPoint( const T& expression )`

Usage: function used to check if an expression is a floating point (double, float or variations) or not.

Example usage: `agr::isFloatingPoint( 0.000003 )`

### one

Header file and source code: [utils.hpp](https://github.com/JustWhit3/arsenalgear/blob/main/cpp/include/math.hpp)

Namespace: `agr`

Complete definition (1-st overload): `template <typename T> extern inline T one( const T& iterating_var )`

Usage: function used to find the incremented unit of a loop.

Example usage:

```cpp
static std::vector <int> v { 1, 2 };
for( const auto & element: v ) std::cout << agr::one( element );
```