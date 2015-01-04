#declare cameratype=0;  //1 = top down

// camera                                                   
#declare camsize= .09;
camera{ 
perspective location  < 10, -14, 8> 
right x*image_width/image_height
sky z
look_at < 0, 0, .4> 
angle 30}


// lighting                              
#if (lighting)
light_source {<-15,-15,25> color rgb 1.0 area_light <23, 0, 0> <0, 23, 0> 4, 4 adaptive 1 jitter orient fade_distance 100 fade_power 2}
#else
light_source {<-5,-15,25> color rgb <1,1,1>}
light_source {<-3,-16,25> color rgb <1,1,1>}
#end 
