//My headers
#include "../include/stream.hpp"

//Extra headers
#include <boost/iostreams/stream.hpp>
#include <boost/iostreams/device/null.hpp>

namespace agr
 {
  //====================================================
  //     NULL_STREAM
  //====================================================
  //Definition of the null stream.
  const boost::iostreams::stream<boost::iostreams::null_sink> null_stream 
   {
    boost::iostreams::null_sink{} 
   };
 }