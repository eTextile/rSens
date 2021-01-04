#!/usr/bin/python

import sys

R_MIN = float(sys.argv[1])
R_MAX = float(sys.argv[2])
VCC = float(sys.argv[3])

for R1 in range(2, 10000, 1) :
    V_min = R_MIN / (R_MIN + R1) * VCC
    V_max = R_MAX / (R_MAX + R1) * VCC

    lastEfficiency = Efficiency
    Efficiency = ((V_max - V_min) / VCC * 100)

    print "R1 :", "%.2f" % R1,
    print " [ V_min", "%.2f" % V_min,
    print " - V_max", "%.2f" % V_max,
    print " - Range ", "%.2f" % (V_max - V_min),
    print " ] Efficiency ", "%.2f" % ((V_max - V_min) / VCC * 100)
