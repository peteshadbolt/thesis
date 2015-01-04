#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.8 phong .1}}
#declare wg_size = 0.05 ; // cross-sectional size of the square waveguide
#declare heater_pigment = pigment{ color rgb <1, .8, 0> }

//#declare wg_pigment = pigment{ color rgb <.2,.2,.8> }
//#declare substrate_pigment = pigment{ color rgb <
//#declare wg_pigment = pigment{ color rgb <.0,.0, .0> }
#declare wg_pigment = pigment{ color rgb <.6,.6,1> }
#declare substrate_pigment = pigment{ color rgb <0.0, 0.0, .04> } 


#declare fiber_array = box{<-.5, -3, -.8> <.5, 3, 0> pigment{color rgb <.0,.0,.0>} finish{phong 0} }
