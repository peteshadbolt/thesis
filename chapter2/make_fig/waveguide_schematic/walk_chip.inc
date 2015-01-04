#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.8 phong .3}}

#include "colors.inc"                            
#include "functions.inc"      
#include "transforms.inc"
#include "waveguides.inc"

#macro fan_guide(top, bottom)
    #local wg_cross_section =  sphere {<0,0,0> .1}
    #local wg_bend_spline = 
      spline { natural_spline
          -1  <-30,   top,   0>,
          0   <0,     top  ,0>,
          .1  <1.5,   top,  0>,
          .9  <8.5,   bottom,  0>,
          1   <10,    bottom,  0>,
          2   <10+30, bottom,  0> }
     union {
     #local Nr = 0;     
     #local EndNr = 1; 
     #while (Nr <=  EndNr)
        object {wg_cross_section translate wg_bend_spline(Nr)}
     #local Nr = Nr + 0.01;  
     #end 
     pigment{wg_pigment}
    } 
#end 

#declare walk_chip=union
{
 // substrate
 box { <-10, -5, 0> <10, 5, -.8> pigment{ substrate_pigment } }

 // guides
 #local Nr = 0;     
 #local EndNr = 10; 
 #while (Nr <=  EndNr)
     object{ fan_guide(.03*Nr, .4*Nr) }
     object{ fan_guide(-.03*Nr, -.4*Nr) }
     object{ fan_guide(.03*Nr, .4*Nr) scale <-1,1,1>}
     object{ fan_guide(-.03*Nr, -.4*Nr) scale <-1,1,1>}
 #local Nr = Nr + 1;  
 #end 

}

