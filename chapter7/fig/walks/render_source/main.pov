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

// A little bit of fiber
#declare straight = union{ cylinder{ <0, 0, 0> <3, 0, 0> pmf_radius pigment{pmf_pigment} } }

// Floor                                                                      
plane {z, -2 pigment{color rgb <1,1,1>} finish{ambient .45}}

//Source
object{source translate <-35,3,0> }

// Connect PMF from source to chip
#macro ppmf(x0, y0, z0, x1,  y1, x2, y2)
    #local pmf_cross_section =  sphere {<0,0,0> pmf_radius}
    #local pmf_bend_spline = 
      spline { cubic_spline
          -1  <x0,               y0+30,   z0>,
          0   <x0,               y0  , z0>,
          //.25 <x0,               (y1+y0)/2.  ,0>,
          .7  <x1,               y1  ,0>,
          //.75 <(x1+x2)/2.,               y1  ,0>,
          1   <x2,               y2,  0>,
          2   <x2+30,            y2,  0> }
     union {
     #local Nr = 0;     
     #local EndNr = 1; 
     #while (Nr <=  EndNr)
        object {pmf_cross_section translate pmf_bend_spline(Nr)}
     #local Nr = Nr + 0.001;  
     #end 
     pigment{pmf_pigment}
    } 
#end 

object{ppmf(-23,-2,0, -18,-5, -15,-.75)}
object{ppmf(-21,-2,-1, -18,-3, -15,-.25)}





// Connect PMF from source to chip
#macro ppmf2(x0, y0, z0, x1,  y1, x2, y2)
    #local pmf_cross_section =  sphere {<0,0,0> pmf_radius}
    #local pmf_bend_spline = 
      spline { cubic_spline
          -1  <x0,               y0-20,   z0>,
          0   <x0,               y0  , z0>,
          //.25 <x0,               (y1+y0)/2.  ,0>,
          .7  <x1,               y1  ,0>,
          //.75 <(x1+x2)/2.,               y1  ,0>,
          1   <x2,               y2,  0>,
          2   <x2+50,            y2,  0> }
     union {
     #local Nr = 0;     
     #local EndNr = 1; 
     #while (Nr <=  EndNr)
        object {pmf_cross_section translate pmf_bend_spline(Nr)}
     #local Nr = Nr + 0.001;  
     #end 
     pigment{pmf_pigment}
    } 
#end 

object{ppmf2(-23,8,0, -17,10, -15,.75)}
object{ppmf2(-21,8,1, -18,9, -15,.25)}




