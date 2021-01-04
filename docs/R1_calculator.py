#!/usr/bin/python

import sys

R_MIN = float(sys.argv[1])
R_MAX = float(sys.argv[2])
#VCC = 3.3
VCC = 5.0

lastEfficiency = 0;

for R1 in range(100, 10000000, 10) :
    V_min = R_MIN / (R_MIN + R1) * VCC
    V_max = R_MAX / (R_MAX + R1) * VCC

    efficiency = ((V_max - V_min) / VCC * 100)
    
    if efficiency > lastEfficiency :
        lastEfficiency = efficiency 
        resistor = R1
    #print "R1 :", "%.2f" % R1,
    #print " [ V_min", "%.2f" % V_min,
    #print " - V_max", "%.2f" % V_max,
    #print " - Range ", "%.2f" % (V_max - V_min),
    #print " ] Efficiency ", "%.2f" % ((V_max - V_min) / VCC * 100)

print "R1 = %d Ohm" % resistor
print "Efficiency = %.2f %%" % lastEfficiency

