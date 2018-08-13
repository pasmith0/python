#!/usr/bin/python
import os, sys

def getArea(type, radius, length, width):
    if type == "circle":
        pi = 3.14
        area = pi * radius**2
    elif type == "rectangle":
        area = length * width
    return area

for radius in [1, 2, 3, 4, 5, 6]:
    print "A.  Area is: " + str(getArea("circle", radius, 0, 0))

print " "
for radius in range(1, 7):
    print "B.  Area is: " + str(getArea("circle", radius, 0, 0))

print " "
for radius in range(7):
    print "C:  Area is: " + str(getArea("circle", radius, 0, 0))

print " "
radiusList = [1, 5, 7, 40, 8]
for i in range(len(radiusList)):
    print "D:  Area is: " + str(getArea("circle", radiusList[i], 0, 0))

print " "
for radius in radiusList:
    print "E.  Area is: " + str(getArea("circle", radius, 0, 0))


sys.exit(0)
