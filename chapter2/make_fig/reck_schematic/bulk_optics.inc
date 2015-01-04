                                                                                                                                               

// beam
#declare beam_radius=.1;
#declare beam_texture=texture {pigment { color rgb <0,0,.8>} finish{phong 0}}
#declare pump_texture=texture {pigment { color rgb <1,0,0>}  finish{phong 0}}
#declare redblue_texture=texture {pigment { color rgb <.3,0,.3>}  finish{phong 0}}

// pbs
#declare pbs_size=1.3;
#declare pbs_scale=1.2;
#declare pbs_texture=texture { finish {refraction 1.0 ior 1} pigment { color rgbf <.4,.4,1,.9>}}   //color rgbf <.7, .7, 1, .7>
#declare pbs_interface_texture=texture { finish {refraction 1.0 ior 1} pigment { color rgbf <.5,.5,1,0.7>}}   //color rgbf <.7, .7, 1, .7>
#declare pbs_cube=box {<-pbs_size/2, -pbs_size/2, -pbs_size/2> <pbs_size/2, pbs_size/2, pbs_size/2> texture { pbs_texture }}
#declare pbs_interface=box {<-.03, -pbs_scale*pbs_size/2, -pbs_scale*pbs_size/2> <.03, pbs_scale*pbs_size/2, pbs_scale*pbs_size/2> texture { pbs_interface_texture } rotate <0,0,45>}
#declare pbs = union{ object {pbs_cube} object{pbs_interface}}


// prism
#declare prism_size=1.0;
#declare prism_texture=texture { finish {refraction 1.0 ior 1} pigment { color rgbf <.4,.4,1,.4>}};  
#declare prism_cube=box {<-prism_size/2, -prism_size/2, -prism_size/2> <prism_size/2, prism_size/2, prism_size/2>};
#declare prism_negative=box {<0, -prism_size, -prism_size> <prism_size, prism_size, prism_size> rotate z*45};
#declare aprism = difference{ object {prism_cube} object{prism_negative} texture{prism_texture }};

// mirror
#declare mirror_texture=texture { finish {reflection .1} pigment { color rgb <.5,.5,1>}}   //color rgbf <.7, .7, 1, .7>
#declare dmirror_texture=texture { finish {reflection .1} pigment { color rgb <.2,.2,.9>}}   //color rgbf <.7, .7, 1, .7>
#declare mirror_thickness=.2;
#declare mirror_radius=1;
#declare mirror=cylinder { <-mirror_thickness/2, 0, 0>, <mirror_thickness/2, 0, 0>, mirror_radius texture { mirror_texture } scale .7}
#declare dmirror=cylinder { <-mirror_thickness/2, 0, 0>, <mirror_thickness/2, 0, 0>, mirror_radius texture { dmirror_texture } scale .7}

// filter
#declare ifilter_texture=texture { pigment { color rgb <.8,.5,.0>}}   //color rgbf <.7, .7, 1, .7>
#declare ifilter_thickness=.2;
#declare ifilter_radius=1;
#declare ifilter=cylinder { <-ifilter_thickness/2, 0, 0>, <ifilter_thickness/2, 0, 0>, ifilter_radius texture { ifilter_texture } }

// beam displacers
#declare bd_thickness=1;
#declare bd_width=12;
#declare bd_length=3;
#declare bd_texture=texture { finish {refraction 1.0 ior 1} pigment { color rgbf <.5,.5,1,.7>}}   //color rgbf <.7, .7, 1, .7>       
#declare beam_displacer = box {<-bd_length/2, -bd_width/2, -bd_thickness/2> <bd_length/2, bd_width/2, bd_thickness/2> texture { bd_texture }}
                 
// waveplates                 
#declare wp_thickness=.1;
#declare twp_thickness=.1;
#declare wp_radius=.8;   
#declare qwp_texture=texture { finish {refraction 1.0 ior 1.5} pigment { color rgbf <1,.2,.2,.2>}}   //color rgbf <.7, .7, 1, .7>
#declare hwp_texture=texture { finish {refraction 1.0 ior 1.5} pigment { color rgbf <.0,.5.1,.2>}}   //color rgbf <.7, .7, 1, .7>
#declare qwp = cylinder { <-wp_thickness/2, 0, 0>, <wp_thickness/2, 0, 0>, wp_radius texture { qwp_texture } }
#declare hwp = cylinder { <-wp_thickness/2, 0, 0>, <wp_thickness/2, 0, 0>, wp_radius texture { hwp_texture } }
#declare tqwp = cylinder { <-twp_thickness/2, 0, 0>, <twp_thickness/2, 0, 0>, wp_radius texture { qwp_texture } }
#declare thwp = cylinder { <-twp_thickness/2, 0, 0>, <twp_thickness/2, 0, 0>, wp_radius texture { hwp_texture } }

// crystals
#declare bbo_thickness=.3;
#declare bbo_radius=1.1;
#declare bbo_texture=texture { finish {refraction 1.0 ior 1.5} pigment { color rgbf <1,.1,.1,.2>}}
#declare bbo = cylinder { <-bbo_thickness/2, 0, 0>, <bbo_thickness/2, 0, 0>, bbo_radius texture { bbo_texture } }

// little box
#declare sbox_size=.9;
#declare sbox_texture=texture { finish {refraction 1.0 ior 1.5} pigment { color rgbf <1, .4, .1, .5>}}   //color rgbf <.7, .7, 1, .7>
#declare sbox = box {<-sbox_size/4, -sbox_size/2, -sbox_size/2> <sbox_size/4, sbox_size/2, sbox_size/2> texture {sbox_texture} }

// detectors
#declare detector_size=.6;
#declare detector_texture=texture {pigment { color rgb <.0,.0,.0>}}
//#declare detector = difference{ sphere { <0, 0, 0>, 1} box{ <0, 1, 1>, <-5, -1, -1> } texture{detector_texture} scale detector_size}
#declare detector = box{<-1, -.5, -.2> <1, .5, .2> texture{detector_texture} scale detector_size}

// detectors
#declare fiber_coupler_size=.8;
#declare fiber_coupler_texture=texture {pigment { color rgb <.1,.1,.7>}}
#declare fiber_coupler = difference{ sphere { <0, 0, 0>, .5} box{ <0, 1, 1>, <-5, -1, -1> } texture{fiber_coupler_texture} scale fiber_coupler_size}

// beam dump            
#declare dump_length=2;
#declare dump_width=1;
#declare dump_texture=texture { pigment { color rgb 0.05}}
#declare dump_body = box {<-dump_length/2, -dump_width/2, -dump_width/2> <dump_length/2, dump_width/2, dump_width/2>}
#declare dump_chop = box {<dump_length/4, -dump_width, -dump_width> <dump_length, dump_width, dump_width> rotate y*15}
#declare dump = difference{ object{dump_body} object{dump_chop}  texture { dump_texture }}

// beam dump            
#declare laser_length=4;
#declare laser_width=2;
#declare laser_texture=texture { pigment { color rgb 0.05}}
#declare laser_body = box {<-laser_length/2, -laser_width/2, -laser_width/2> <laser_length/2, laser_width/2, laser_width/2>}
#declare laser_shutter = cylinder {<laser_length/2, 0, 0>, <laser_length/2+.5, 0, 0>, .5}
#declare laser = union{ object{laser_body} object{laser_shutter} texture { laser_texture } scale .8}

// lens                    
#declare big=1;
#declare lens_texture=texture { finish {refraction 1.0 ior 1} pigment { color rgbf <.3,.3,1,.6>}}   //color rgbf <.7, .7, 1, .7>
#declare lens_sphere=sphere {<-.4+big,0,0> big}
#declare lens_box=box {<0, -big, -big> <big*3, big, big>}
#declare lens = difference{ object {lens_sphere} object{lens_box} texture{lens_texture}}
#declare small_lens = difference{ object {lens_sphere translate .15*x} object{lens_box} texture{lens_texture}}
