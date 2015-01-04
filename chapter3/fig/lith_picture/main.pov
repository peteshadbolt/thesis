#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.7 phong 0}}
global_settings{assumed_gamma 1.0}

#include "colors.inc"                            
#include "functions.inc"      
#include "transforms.inc"
#include "stage.inc"
#include "walk_chip.inc"
#include "bulk_optics.inc"
#include "bs_chip.inc"
#include "source.inc"
#include "fiber_and_wire.inc"
#include "waveguides.inc"
#include "chip_parts.inc"
#include "cnot_mz.inc"


// A little bit of fiber
//#declare straight = union{ cylinder{ <0, 0, 0> <3, 0, 0> pmf_radius pigment{pmf_pigment} } }

// Floor                                                                      
plane {z, -1 pigment{color rgb <1,1,1>} finish{ambient .45}}


union{
box { <-5, 2, 0-wg_size> <5, -2, -.8> pigment{color rgbf <.5, .5, .9, .5>} }

box { <-5, 2, 0-wg_size> <5, -2, wg_size> pigment{color rgbf <.8, .5, .5, .995>} }

box { <-5, 2, wg_size> <5, -2, wg_size*4> pigment{color rgbf <.5, .8, .5, .995>} }

object{mzi}
object{straight translate <4,0,0>}
object{straight translate <4,1,0>}
object{straight translate <-4,0,0>}
object{straight translate <-4,1,0>}
object{heater scale x*2 translate <0,-.5,wg_size*4>}
object{heater scale <6, .2, 1> translate <0,-.5,wg_size*4>}
object{heater scale <.1, 3, 1> translate <2.35, -1.1,wg_size*4>}
object{heater scale <.1, 3, 1> translate <-2.35, -1.1,wg_size*4>}
scale 1.5
}


