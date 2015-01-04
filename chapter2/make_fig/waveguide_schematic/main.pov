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

#declare wg_bend_spline = 
  spline { natural_spline
      -1   <-30,0,0>,
      0   <0,0,0>,
      .1   <1.5,0,0>,
      .9 <8.5,4.5,0>,
      1 <10,4.5,0>,
      2   <10+30,4.5,0>
}

#local wg_size=.3;

//#declare wg_cross_section =  sphere {<0,0,0> wg_size*10}
#declare wg_cross_section =  box {<-1,-1,-1> <1,1,1> scale wg_size}

#declare wg_bend = union{
 #local Nr = 0;     
 #local EndNr = 1; 
 #while (Nr <=  EndNr)
    object {wg_cross_section translate wg_bend_spline(Nr)}
 #local Nr = Nr + 0.01;  
 #end 
 pigment{wg_pigment}
} 

#declare straight=cylinder{<-1,-.5,0> <1,-.5,0> wg_size pigment{color rgb <1,0,0>} }

// substrate
box { <-5, -3, 1> <5, 3, -1.5> pigment{ substrate_pigment} translate <-5, 2, 0>} 

// Bend
object { wg_bend scale <-1,1,1> translate <0,0,0>}

