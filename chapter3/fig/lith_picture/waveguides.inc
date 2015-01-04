#version 3.6; // 3.7
#declare wg_size = 0.05 ; // cross-sectional size of the square waveguide
#declare heater_pigment = pigment{ color rgb <1, .8, 0> }

#declare wg_pigment = pigment{ color rgb <.0,.0,.0> }
//#declare substrate_pigment = pigment{ color rgb <
//#declare wg_pigment = pigment{ color rgb <.0,.0, .0> }
//#declare wg_pigment = pigment{ color rgb <.6,.6,1> }
#declare substrate_pigment = pigment{ color rgbf <0.7, 0.7, .9, .8> } 


#declare fiber_array = box{<-.5, -3, -.8> <.5, 3, 0> pigment{color rgb <.0,.0,.0>} finish{phong 0} }
