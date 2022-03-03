#ifndef STREAM_HPP
#define STREAM_HPP

//Extra headers
#include <boost/iostreams/stream.hpp>
#include <boost/iostreams/device/null.hpp>

namespace agr
 {
  //====================================================
  //     OBJECTS DEFINITION
  //====================================================
  extern const boost::iostreams::stream<boost::iostreams::null_sink> null_stream;
 }

#endif