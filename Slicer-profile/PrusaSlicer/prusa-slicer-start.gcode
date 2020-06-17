M862.3 P "[printer_model]" ; printer model check
G90 ; use absolute coordinates
M83 ; extruder relative mode
G28 ; Home
M400 ; wait for complete
G1 Z50 F420 ; Raise Z
; then preheat
M104 S[first_layer_temperature] ; set extruder temp
M140 S[first_layer_bed_temperature] ; set bed temp
M190 S[first_layer_bed_temperature] ; wait for bed temp
M109 S[first_layer_temperature] ; wait for extruder temp

G28 ; home
G29 ; mesh bed leveling
G92 E0.0 ; reset extruder distance position
M211 S0 ; Disable software endtop to allow nozzel move to y=-1
G1 Y-1 F2500.0 ; go outside print area
M400 ; wait for complete
G1 Z30 F420 ; Raise Z
M400 ; wait for complete
M300 S440 P500 ; play sound
M0 S30 Clean nozzle then click to continue ; wait for user to clean nozzle
G1 Z0.3 F420.0 ; Lower Z
M400 ; wait for complete
G1 X60.0 E15.0 F1000.0 ; intro line
G1 X100.0 E21.5 F1000.0 ; intro line
M400 ; wait for complete
G1 Z2.0 F420 ; lift the extruder a bit
M400 ; wait for complete
G92 E0.0 ; reset extruder distance position
G1 Y0 ; move to Y0
M211 S1 ; re-enable software endstop