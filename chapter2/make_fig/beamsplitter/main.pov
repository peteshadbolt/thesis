#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.8 phong .3}}
global_settings{assumed_gamma 1.0}

#include "colors.inc"                            
#include "functions.inc"      
#include "transforms.inc"
#include "stage.inc"
#include "waveguides.inc"
#include "bulk_optics.inc"
#include "source.inc"
#include "fiber_and_wire.inc"

// Floor                                                                      
plane {z, -2 pigment{color rgb <1,1,1>} finish{ambient .45}}

object{pbs rotate z*90 translate <0,0,0>}

//Beams
cylinder{ -x*3 x*3 0.05 texture{pump_texture}}
cylinder{ -y*3 y*3 0.05 texture{pump_texture}}

cone { <-2, 0, 0>, 0.15 <-1.5, 0, 0>, .0 texture{pump_texture} }
cone { <-2, 0, 0>, 0.15 <-1.5, 0, 0>, .0 texture{pump_texture} translate 3.5*x}

cone { <0,-2, 0>, 0.15 <0,-1.5,  0>, .0 texture{pump_texture} }
cone { <0,-2, 0>, 0.15 <0,-1.5,  0>, .0 texture{pump_texture} translate 3.5*y}
