#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.7 phong 0}}
global_settings{assumed_gamma 1.0}

#include "colors.inc"                            
#include "functions.inc"      
#include "transforms.inc"
#include "stage.inc"

// Floor                                                                      
plane {z, -10 pigment{color rgb <1,1,1>} finish{ambient .45}}

union{
sphere {<0,0,0>, 1 pigment{color rgbf <.7,.7,1,.8>}}
torus { 1, .01 }
torus { 1, .01 rotate x*90}
torus { 1, .01 rotate z*90}
cylinder {z*1.2, -z*1.1, .01}
cylinder {z*1.2, -z*1.1, .01 rotate x*90}
cylinder {z*1.2, -z*1.1, .01 rotate y*90}

sphere {<0,0,0>, .05 pigment{color rgb <1,0,0>}}
sphere {<1,0,0>, .05 pigment{color rgb <1,0,0>}}
sphere {<-1,0,0>, .05 pigment{color rgb <1,0,0>}}
sphere {<0,-1,0>, .05 pigment{color rgb <1,0,0>}}
sphere {<0,1,0>, .05 pigment{color rgb <1,0,0>}}
sphere {<0,0,1>, .05 pigment{color rgb <1,0,0>}}
sphere {<0,0,-1>, .05 pigment{color rgb <1,0,0>}}

cone { x*1.2, .03 x*1.3 0}
cone { y*-1.2, .03 y*-1.3 0}
cone { z*1.2, .03 z*1.3 0}

scale 3
}
