#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.8 phong .3}}

#declare pmf_pigment = pigment{ color rgb <.1,.1,.9> }
#declare pmf_radius = 0.10;

#macro pmf_bend(x0, y0,  x1, y1)
    #local pmf_cross_section =  sphere {<0,0,0> pmf_radius}
    #local pmf_bend_spline = 
      spline { natural_spline
          -1  <x0-30,            y0,   0>,
          0   <x0,               y0  ,0>,
          .1  <x0+(x1-x0)*.15,   y0,  0>,
          .9  <x1-(x1-x0)*.15,   y1,  0>,
          1   <x1,               y1,  0>,
          2   <x1+30,            y1,  0> }
     union {
     #local Nr = 0;     
     #local EndNr = 1; 
     #while (Nr <=  EndNr)
        object {pmf_cross_section translate pmf_bend_spline(Nr)}
     #local Nr = Nr + 0.01;  
     #end 
     pigment{pmf_pigment}
    } 
#end 


#declare wire_radius = 0.10 ; // cross-sectional size of the wire
#declare wire_pigment = pigment{ color rgb <0,0,0>   }

#macro wire_bend(x0, y0,  x1, y1)
    #local wire_cross_section =  sphere {<0,0,0> wire_radius}
    #local wire_bend_spline = 
      spline { natural_spline
          -1  <x0-30,            y0,   0>,
          0   <x0,               y0  ,0>,
          .1  <x0+(x1-x0)*.15,   y0,  0>,
          .9  <x1-(x1-x0)*.15,   y1,  0>,
          1   <x1,               y1,  0>,
          2   <x1+30,            y1,  0> }
     union {
     #local Nr = 0;     
     #local EndNr = 1; 
     #while (Nr <=  EndNr)
        object {wire_cross_section translate wire_bend_spline(Nr)}
     #local Nr = Nr + 0.01;  
     #end 
     pigment{wire_pigment}
    } 
#end 

//SMA connector
#declare sma = union{
    cylinder { <-.3, 0, 0> <.3, 0, 0>, .2}
    pigment{ color rgb <1,.6,0> }
} 

//splitter
#declare splitter_box = union{
    box { <-.5,-.3,-.1> <.5,.3,.1> }
    pigment{ color rgb <0,0,.2> }
} 

#declare one_to_two = union{
    object {splitter_box } 
    object{ pmf_bend(0, -.2, 3, -.5) }
    object{ pmf_bend(0, .2, 3, .5) }
} 

#declare one_to_three = union{
    object {splitter_box } 
    object{ pmf_bend(0, -.2, 3, -1) }
    object{ pmf_bend(0, 0, 3, 0) }
    object{ pmf_bend(0, .2, 3, 1) }
} 

