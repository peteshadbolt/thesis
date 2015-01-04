#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.8 phong .3}}

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

#local wg_size=.18;

#declare wg_cross_section =  sphere {<0,0,0> wg_size*10}

#declare wg_bend = union{
 #local Nr = 0;     
 #local EndNr = 1; 
 #while (Nr <=  EndNr)
    object {wg_cross_section translate wg_bend_spline(Nr)}
 #local Nr = Nr + 0.05;  
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


#declare straight=cylinder{<-1,-.5,0> <1,-.5,0> wg_size pigment{color rgb <1,0,0>} }

#declare heater=box{<-.7,-.2,.2> <.7,.2,.3> pigment{color rgb <1,1,0>} }

#declare mzi=union{
    object { coupler translate <-2,0,0>}
    object { straight translate <0,-.5,0>}
    object { straight translate <0,.5,0>}
    object { heater translate <0,.5,0>}
    object { coupler translate <2,0,0>}
}

#declare bs_chip=union{
 //couplers
 #local row = 0;     
 #local n_rows = 8; 
 #local col = -n_rows;     
 #local n_cols = n_rows; 
 #while (col <  n_cols)
     #local row = abs(col);
     #while (row <  n_rows)
        object { coupler translate <col*2,row,0>}
     #local row = row + 2;  
     #end 
 #local col = col + 1;  
 #end 

 //connecting wgs
 #local row = 0;     
 #local n_rows = 9; 
 #while (row <  n_rows)
     cylinder{<-n_rows*2, row-.5, 0> <-row*2-1, row-.5, 0> wg_size pigment{wg_pigment} }
     cylinder{<n_rows*2, row-.5, 0> <row*2+1, row-.5, 0> wg_size pigment{wg_pigment} }
 #local row = row + 1;  
 #end 

 // fill the gaps
 #local col = 0;     
 #local n_cols = n_rows; 
 #while (col <  n_cols/2)
     cylinder{<0+col*4-1, n_rows-1.5, 0> <0+col*4+1, n_rows-1.5, 0> wg_size pigment{wg_pigment} }
     cylinder{<0-col*4-1, n_rows-1.5, 0> <0-col*4+1, n_rows-1.5, 0> wg_size pigment{wg_pigment} }
 #local col = col + 1;  
 #end 

 // substrate
 box { <-n_cols*2, -2, 0> <n_cols*2, n_rows, -.8> pigment{ substrate_pigment} }
}
