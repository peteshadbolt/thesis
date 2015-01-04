#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.8 phong .1}}

#declare wg_size = 0.10 ; // cross-sectional size of the square waveguide
//#declare wg_pigment = pigment{ color rgb <.4,.4,1> }
#declare heater_pigment = pigment{ color rgb <1, .8, 0> }

//#declare wg_pigment = pigment{ color rgb <.2,.2,.8> }
//#declare substrate_pigment = pigment{ color rgb <.5, .5, .6> } 
#declare wg_pigment = pigment{ color rgb <.9,.9, 1.0> }
#declare substrate_pigment = pigment{ color rgbf <0.05, 0.05, .2> } 


#declare fiber_array = box{<-.5, -3, -.8> <.5, 3, 0> pigment{color rgb <.0,.0,.0>} finish{phong 0} }
