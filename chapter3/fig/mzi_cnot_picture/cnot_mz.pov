#version 3.6; // 3.7
global_settings{assumed_gamma 1.0}
#include "stage.inc"                            
#include "waveguides.inc"
#include "fiber_and_wire.inc"
#include "chip_parts.inc"

// half the chip
#declare half_chip = union{
object{ coupler translate <2, 1, 0>}
object{ mzi translate <4, 1, 0>}
object{ mzi translate <8, 1, 0>}
object{ mzi translate <8, -1, 0>}
object{ heater translate <4, -.5, 0>}
object{straight scale <2,1,1> translate <3, -1, 0>}
object{straight scale <2,1,1> translate <3, 0, 0>}
object{straight translate <12, -1, 0>}
object{straight translate <12, 0, 0>}
object{straight translate <12, 1, 0>}
object{straight translate <12, 2, 0>}
object{straight scale <6, 1, 1> translate <7, 3, 0>}
object{straight scale <6, 1, 1> translate <7, -2, 0>}
}

#declare cnot_mz=union{
// cz
object{ coupler translate -y*2}
object{ coupler }
object{ coupler translate y*2}

object{half_chip}
object{half_chip scale x*-1}


// substrate
box { <-13, -3.5, 0> <-3, 3.5, -.8> pigment{ rgb <.5, .5, .9> } }
//box { <-3, -3.5, 0> <3, 3.5, -.8> pigment{   rgb <.4, .4, .9> }} 
box { <-3, -3.5, 0> <3, 3.5, -.8> pigment{   rgb <.9, .7, .5> }} 
box { <3, -3.5, 0> <13, 3.5, -.8> pigment{   rgb <.5, .5, .9> } }
}

// Fibers
#declare fiber_array=union{
    object{ pmf_bend(-20, -2, -13, -1.5) translate z*-.2}
    object{ pmf_bend(-20, -4, -13, -2.5) translate z*-.2}
    object{ pmf_bend(-20, -0, -13, -.5) translate z*-.2}
    object{ pmf_bend(-20, 1, -13, .5) translate z*-.2}
    object{ pmf_bend(-20, 3, -13, 1.5) translate z*-.2}
    object{ pmf_bend(-20, 5, -13, 2.5) translate z*-.2}
    box { <-14, -3.5, -.8> <-13, 3.5, 0> pigment {rgbf <.8,.8,1,.7>}}
}

// Chip
#declare coupled_chip=union{
object{cnot_mz translate <0,0,0>}
object{fiber_array}
object{fiber_array scale -x}
}

