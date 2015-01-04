
#declare lighting=1;

// camera                                                   
#declare camsize= .08;
#declare cameratype=1;        
//#if (cameratype)                                            
//camera{ orthographic location  < 25, 5, 15> right camsize*640*x up camsize*480*y 
                      //look_at <24,0,2.5> sky <0,0,1>}
//#else
//camera{ orthographic location <15, 0, 100> right camsize*640*x up camsize*480*y look_at <15,0,0> sky <0,0,1>}
//#end 

camera{ perspective location <45,45,20>*.7 look_at <6,0,0> sky <0,0,1> angle 35}
                              
// lighting                              
#if (lighting)
light_source {<5,5,35> color rgb 1.0 area_light <23, 0, 0> <0, 23, 0> 4, 4 adaptive 1 jitter orient fade_distance 100 fade_power 2}
#else
light_source {<-5,-15,25> color rgb <1,1,1>}
light_source {<-3,-16,25> color rgb <1,1,1>}
#end 
