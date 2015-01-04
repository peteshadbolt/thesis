
#declare lighting=1;    //1 = slow lighting
#declare cameratype=0;  //1 = top down

// camera                                                   
#declare camsize= .12;
#if (cameratype)                                            
camera{ orthographic location  < -15, 0, 10> right camsize*640*x up camsize*240*y 
                      look_at < 15, 0, 0> sky <0,0,1>}
#else
camera{ perspective location  < 0, 60, 80> 
                    right x*image_width/image_height
                    sky z
                    look_at < 0, -25, -40> 
                    angle 40
                }
//camera{ orthographic location  < -13, 9, 7> right camsize*640*x up camsize*240*y 
                      //look_at < -13.5, 4, 0> sky <0,0,1>}
#end 

//#declare camsize= .08;
//camera{ orthographic location  < -25, 3, 8> right camsize*640*x up camsize*240*y 
                     //look_at < -22, 3, 0> sky <0,0,1>}

// lighting                              
#if (lighting)
light_source {<-15,-15,25> color rgb 1.0 area_light <23, 0, 0> <0, 23, 0> 4, 4 adaptive 1 jitter orient fade_distance 100 fade_power 2}
#else
light_source {<-5,-15,25> color rgb <1,1,1>}
light_source {<-3,-16,25> color rgb <1,1,1>}
#end 
