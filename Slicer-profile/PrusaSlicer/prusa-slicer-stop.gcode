G4 ; wait
M221 S100
M104 S0 ; turn off temperature
M140 S0 ; turn off heatbed
M107 ; turn off fan
M400 ; wait for complete
{if layer_z < max_print_height}G1 Z{z_offset+min(layer_z+30, max_print_height)}{endif} F420; Move print head up
M400 ; wait for complete
G1 X0 Y215 F3000 ; home X axis
M300 S440 P300 ; play sound
M300 S0 P100 ; mute
M300 S440 P300 ; play sound
M84 ; disable motors