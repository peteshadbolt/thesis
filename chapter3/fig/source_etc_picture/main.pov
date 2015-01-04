#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.8 phong .3}}
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
plane {z, -.3 pigment{color rgb <1,1,1>} finish{ambient .45}}

//Source
object{source translate <-40,3,0> }

object{coupled_chip scale .2 translate <-21,3,0> }

object{detector scale .8 translate < -15,4,0> }
object{detector scale .8 translate < -15,2,0> }
object{detector scale .8 translate < -15,0,0> }
object{detector scale .8 translate < -15,6,0> }
//Chip

box{<-1, -1, -1> <1,1,1> scale <.8,1,.5> translate <-12,3,0> }
box{<-1, -1, -1> <1,1,1> scale <1,.8,.5> translate <-21,-0,0> }



