#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.8 phong .3}}
global_settings{assumed_gamma 1.0}
#include "colors.inc"                            
#include "functions.inc"      
#include "bulk_optics.inc"
#include "stage.inc"
#include "transforms.inc"
#include "fiber.inc"

// floor                                                                      
plane {z, -10 pigment{color rgb <1,1,1>} finish{ambient 1}}

// pump beam 
cylinder { <-10, 0, 0>, <15, 0, 0>, .3 texture { pump_texture }}
                                                                      
// Crystal
box { <-1, -2, -2> <1, 2, 2> pigment { color rgbf <.6,.6,1,.5>}}

//Downconverted cone
#declare dcone= difference{
cone { <0, 0, 0>, 0.0 <13, 0, 0>, 4.0}
cone { <0, 0, 0>, 0 <14, 0, 0>, 4.0}
pigment { color rgbf <1,.6,.6,.5>}
}

difference{
    union{
    object{ dcone rotate y*9}
    object{ dcone rotate y*-9}
    }
    box{ <10, -100, -100> <100, 100, 100>}
}

sphere{ <10, -2.8, 0> .5 pigment {color rgb <.2, 1, .2>} }
sphere{ <10, 2.8, 0> .5 pigment {color rgb <.2, 1, .2>} }
