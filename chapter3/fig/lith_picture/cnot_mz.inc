#version 3.6; // 3.7
#include "stage.inc"                            
#include "waveguides.inc"
#include "fiber_and_wire.inc"
#include "chip_parts.inc"

// half the chip
#declare half_chip = union{
object{ coupler translate <2, 1, 0>}
object{straight scale <2,1,1> translate <3, -1, 0>}
object{straight scale <2,1,1> translate <3, 0, 0>}


object{straight scale <1,1,1> translate <4, 1, 0>}
object{straight scale <1,1,1> translate <4, 2, 0>}


//object{straight scale <6, 1, 1> translate <7, 3, 0>}
//object{straight scale <6, 1, 1> translate <7, -2, 0>}
}

#declare cnot_mz=union{
// cz
object{ coupler translate -y*2}
object{ coupler }
object{ coupler translate y*2}

object{half_chip}
object{half_chip scale x*-1}


// substrate
box { <-5, -3.5, 0> <-1, 3.5, -.8> pigment{ rgb <.3, .3, .9> } }
//box { <-3, -3.5, 0> <3, 3.5, -.8> pigment{   rgb <.4, .4, .9> }} 
box { <-1, -3.5, 0> <1, 3.5, -.8> pigment{   rgb <.2, .2, .9> }} 
box { <1, -3.5, 0> <5, 3.5, -.8> pigment{   rgb <.3, .3, .9> } }
}

// Fibers
#declare fiber_array=union{
    box { <-14, -3.5, -.8> <-13, 3.5, 0> pigment {rgbf <.8,.8,1,.7>}}
}

// Chip
#declare coupled_chip=union{
object{cnot_mz translate <0,0,0>}
}

