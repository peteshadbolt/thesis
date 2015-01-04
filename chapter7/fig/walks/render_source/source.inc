#version 3.6; // 3.7
#default{ finish{ ambient 0.1 diffuse 0.8 phong .0}}
#include "colors.inc"                            
#include "functions.inc"      
#include "bulk_optics.inc"

#declare s=5;

#declare source=union{

// pump beams
cylinder { <-5,5,0>, <3,5,0>, beam_radius texture { pump_texture }}
cylinder { <0, 5, 0>, <0, 7, 0>, beam_radius texture { pump_texture }}
cylinder { <6, 5, 0>, <8, 5, 0>, beam_radius texture { pump_texture }}

// purple beam
cylinder { <0, 5, 0>, <6, 5, 0>, beam_radius texture { redblue_texture }}

// upconverted beams
cylinder { <6, 5, 0>, <6, 2.5, 0>, beam_radius texture { beam_texture }}
cylinder { <6, 2.5, 0>, <-1, 2.5, 0>, beam_radius texture { beam_texture }}
cylinder { <-1, 2.5, 0>, <-1, 0, 0>, beam_radius texture { beam_texture }}
cylinder { <-1, 0, 0>, <8, 0, 0>, beam_radius texture { beam_texture }}

// laser
object { laser translate <-6, 5, 0>}


// mirrors        
object { dmirror rotate z*45 translate <6, 5, 0>}
object { dmirror rotate z*135 translate <6, 2.5, 0>}
object { dmirror rotate z*135 translate <-1, 2.5, 0>}
object { dmirror rotate z*45 translate <-1, 0, 0>}

// attenuator
object { pbs rotate z*90 translate <0, 5, 0> }
object { hwp translate <-2, 5, 0> }

//upconversion
object { bbo translate <3, 5, 0> }
object { lens translate <2, 5, 0>  }
object { lens rotate z*180 translate <4, 5, 0>  }

// dumps
object { dump rotate z*90 translate <0, 8, 0> }
object { dump translate <9, 5, 0> }

// downconversion stack
object { lens translate <3, 0, 0>  }
object { bbo translate <7, 0, 0> }
object { dmirror translate <7.5, 0, 0> }
object { ifilter translate <8, 0, 0> }                                                                                                                                                                



object{
difference{
cone { <0, 0, 0>, 0.0 <5, 0, 0>, 1.0}
cone { <0, 0, 0>, 0 <6, 0, 0>, 0.99}
}
texture{
pigment { color rgbf <1,.7,.7,.9>}
}
translate x*7.5
}
                                                                      

// Downconversion helper
//cone{ <7, 0, 0>, 0.0 <20, 2, 3>, 1.0    pigment{ color rgbf<1,.9,.9,.55> } }

// Downconversion collection
object { aprism rotate z*180 translate <12, -.92, 0> }
object { aprism rotate z*90 translate <12, .92, 0> }

object { aprism rotate z*180 translate <12, .0, -1> }
object { aprism rotate z*90 translate <12, -.0, 1> }

//downconverted beams
cylinder { <7, 0, 0>, <12, 1, 0>, beam_radius texture { pump_texture }}
cylinder { <12, 5, 0>, <12, 1, 0>, beam_radius texture { pump_texture }}

cylinder { <7, 0, 0>, <12, -1, 0>, beam_radius texture { pump_texture }}
cylinder { <12, -5, 0>, <12, -1, 0>, beam_radius texture { pump_texture }}

cylinder { <7, 0, 0>, <12, 0, -1> beam_radius texture { pump_texture }}
cylinder { <12, -5, -1>, <12, 0, -1>, beam_radius texture { pump_texture }}

cylinder { <7, 0, 0>, <12, 0, 1>, beam_radius texture { pump_texture }}
cylinder { <12, 5, 1>, <12, 0, 1>, beam_radius texture { pump_texture }}

//object { small_lens rotate z*90 translate <12, 3, 0>  }
//object { small_lens rotate z*-90 translate <12, -3, 0>  }
//object { small_lens rotate z*-90 translate <12, -3, -1>  }
//object { small_lens rotate z*90 translate <12, 3, 1>  }

object { qwp rotate z*90 translate <12, 2, 1>  }
object { hwp rotate z*90 translate <12, 2.25, 1>  }
object { qwp rotate z*90 translate <12, 2.5, 1>  }

object { fiber_coupler rotate z*90 translate <12, 5, 0>  }
object { fiber_coupler rotate z*-90 translate <12, -5, 0>  }
object { fiber_coupler rotate z*-90 translate <12, -5, -1>  }
object { fiber_coupler rotate z*90 translate <12, 5, 1>  }

}
