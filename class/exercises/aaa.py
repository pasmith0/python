#!/usr/bin/python

"""
     1. Write a "sequence" that calculates each.

     2. Write a 'selection' that calculates each based on a condition.
     3. Write a "subroutine' that can be used repeatedly.

     4. Write a loop that calculates the volume of a cube for lengths from 1 to 10 using the subroutine.


     Volumes:

     Cube:     length**3
     Sphere:   (4/3) * pi * radius**3    [ alt:  4 * pi * radius**3 / 3 ]
     Pyramid:  (length**2 * height) / 3
"""
length = 5
if length:
    volCube = length**3.0
    print "Volume of Cube: " + str(volCube)

pi = 3.14
radius = 5
if radius and pi >= 3.14:
    volSphere = 4 * pi * radius**3 / 3
    print "Volume of Sphere: " + str(volSphere)

height = 4
if height and length:
    volPyramid = (length**2.0 * height) / 3.0
    print "Volume of Pyramid: " + str(volPyramid)

height = 6
for number in range(10):
    length = number + 1
    volPyramid = (length**2.0 * height) / 3.0
    print "Volume of Pyramid for Length of " + str(length) + ": " + str(volPyramid)

def volCube(length):
    if length:
        return length**3.0
    else:
        return None

volume = volCube(10)
if volume:
    print "Volume is " + str(volume)
else:
    print "Length must be zero!"

    
