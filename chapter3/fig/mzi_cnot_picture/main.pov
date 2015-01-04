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
#declare straight = union{ cylinder{ <0, 0, 0> <3, 0, 0> pmf_radius pigment{pmf_pigment} } }

// Floor                                                                      
plane {z, -1 pigment{color rgb <1,1,1>} finish{ambient .45}}

//Source
//object{coupled_chip scale 2 translate <-25,0,0> }

 //substrate
union{
union{
box { <-5, 2, 0> <5, -2, -.8> pigment{ rgb <.3, .3, .9> } }
object{mzi}
object{heater translate <-4,.5,0>}
cylinder{<-5,-.5,0> <-3,-.5,0> wg_size*1.5 pigment{wg_pigment} }
cylinder{<-5,+.5,0> <-3,+.5,0> wg_size*1.5 pigment{wg_pigment} }
cylinder{<5,-.5,0> <3,-.5,0> wg_size*1.5 pigment{wg_pigment} }
cylinder{<5,+.5,0> <3,+.5,0> wg_size*1.5 pigment{wg_pigment} }

object{detector scale .5 translate < 5.3, .5, 0>}
object{detector scale .5 translate < 5.3, -.5, 0>}
scale 1.5
translate <-25,1,0>
}

union{
box { <-5, 2, 0> <5, -2, -.8> pigment{ rgb <.3, .3, .9> } }
object{mzi}
object{heater translate <4,.5,0>}
cylinder{<-5,-.5,0> <-3,-.5,0> wg_size*1.5 pigment{wg_pigment} }
cylinder{<-5,+.5,0> <-3,+.5,0> wg_size*1.5 pigment{wg_pigment} }
cylinder{<5,-.5,0> <3,-.5,0> wg_size*1.5 pigment{wg_pigment} }
cylinder{<5,+.5,0> <3,+.5,0> wg_size*1.5 pigment{wg_pigment} }
scale 1.5
translate <-47,1,0>
}
translate <22, 3, 0>
}


