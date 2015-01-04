#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.8 phong .0}}
#include "colors.inc"                            
#include "functions.inc"      
#include "bulk_optics.inc"

#declare s=5;

#declare source=union{

// pump beams
cylinder { <3,0,0>, <14,0,0>, beam_radius texture { beam_texture }}

// laser
object { laser scale .5 translate <3, 0, 0>}

object { ifilter rotate z*90 scale .8 translate <12, 2, 0> }
object { ifilter rotate z*90 scale .8 translate <12, -2, 0> }

// dumps
object { dump scale .7 translate <14, 0, 0> }

// downconversion stack
object { lens scale <.5, 1, 1> translate <6, 0, 0>  }
object { bbo translate <7, 0, 0> }
//object { dmirror translate <7.5, 0, 0> }

//object{
//difference{
//cone { <0, 0, 0>, 0.0 <5, 0, 0>, 1.0}
//cone { <0, 0, 0>, 0 <6, 0, 0>, 0.99}
//}
//texture{
//pigment { color rgbf <1,.7,.7,.9>}
//}
//translate x*7.5
//}
                                                                      
// Downconversion helper
//cone{ <7, 0, 0>, 0.0 <20, 2, 3>, 1.0    pigment{ color rgbf<1,.9,.9,.55> } }

// Downconversion collection
object { aprism rotate z*180 translate <12, -.92, 0> }
object { aprism rotate z*90 translate <12, .92, 0> }

//downconverted beams
cylinder { <7, 0, 0>, <12, 1, 0>, beam_radius texture { pump_texture }}
cylinder { <12, 3, 0>, <12, 1, 0>, beam_radius texture { pump_texture }}

cylinder { <7, 0, 0>, <12, -1, 0>, beam_radius texture { pump_texture }}
cylinder { <12, -3, 0>, <12, -1, 0>, beam_radius texture { pump_texture }}

object { fiber_coupler scale .5 rotate z*90 translate <12, 3, 0>  }
object { fiber_coupler scale .5 rotate z*-90 translate <12, -3, 0>  }

}
