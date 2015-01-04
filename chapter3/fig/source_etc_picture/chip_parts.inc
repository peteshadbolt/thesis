#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.8 phong .1}}
global_settings{assumed_gamma 1.0}
#include "colors.inc"                            
#include "functions.inc"      
#include "transforms.inc"
#include "waveguides.inc"

#declare wg_bend_spline = 
  spline { natural_spline
      -1   <-30,0,0>,
      0   <0,0,0>,
      .1   <1.5,0,0>,
      .9 <8.5,4.5,0>,
      1 <10,4.5,0>,
      2   <10+30,4.5,0>
}

#local wg_size=.07;

#declare wg_cross_section =  sphere {<0,0,0> wg_size*10}

#declare wg_bend = union{
 #local Nr = 0;     
 #local EndNr = 1; 
 #while (Nr <=  EndNr)
    object {wg_cross_section translate wg_bend_spline(Nr)}
 #local Nr = Nr + 0.01;  
 #end 
 pigment{wg_pigment}
} 

#declare coupler=union{
    object { wg_bend  translate y*.5}
    object { wg_bend scale <-1,1,1> translate y*.5}
    object { wg_bend scale <1,-1,1> translate y*-.5}
    object { wg_bend scale <-1,-1,1> translate y*-.5}
    scale .1
}

#declare straight=cylinder{<-1,-.5,0> <1,-.5,0> wg_size pigment{wg_pigment} }

#declare heater=union{box{<-.2,-.1,.0> <.2,.1,.1> pigment{color rgb <1,.6,0>}} scale 2}

#declare mzi=union{
    object { coupler translate <-2,0,0>}
    object { straight translate <0,0,0>}
    object { straight translate <0,1,0>}
    object { heater translate <0,.5,0>}
    object { coupler translate <2,0,0>}
}

