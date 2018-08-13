#!/usr/bin/python
import os, sys

print "\nExercise 1"

# Calculate volume of a cube
length = 5.0
volume = length**3
print "Cube volume for length " + str(length) + " is " + str(volume)

# Calculate volume of a sphere
radius = 5.0
pi = 3.14
volume = 4 * pi * radius**3 / 3
print "Sphere volume for radius " + str(radius) + " is " + str(volume)

# Calculate volume of a pyramid
length = 5.0
height = 8.0
volume = length**2 * height / 3.0
print "Pyramid volume for length " + str(length) + " and height " + str(height) + " is " + str(volume)

print "\nExercise 2"

# Selection of volume based on shape
shape = "pyramid"

if shape == "cube":
    # Calculate volume of a cube
    length = 5.0
    volume = length**3
    print "Cube volume for length " + str(length) + " is " + str(volume)
elif shape == "sphere":
    # Calculate volume of a sphere
    radius = 5.0
    pi = 3.14
    volume = 4 * pi * radius**3 / 3
    print "Sphere volume for radius " + str(radius) + " is " + str(volume)
elif shape == "pyramid":
    # Calculate volume of a pyramid
    length = 5.0
    height = 8.0
    volume = length**2 * height / 3.0
    print "Pyramid volume for length " + str(length) + " and height " + str(height) + " is " + str(volume)
else:
    print "Unrecognized shape: " + shape

print "\nExercise 3"

#============================================================
#  Function to determine volume of a cube, sphere or pyramid
#============================================================

def getVolumeForShape(shape, radius, length, height):
    """
    Calculate the volume of a cube, sphere or four-sided pyramid.
    Returns the volume or 0 for failure.

    shape:  Either "cube", "sphere", or "pyramid"
    radius: The radius of a sphere. "None" if other shape.
    length: The length of the base of a cube or a four-sided pyramid. "None" if other shape.
    height: The height of a four-sided pyramid. "None" if other shape.
    """

    # Selection of volume based on shape
    if shape == "cube":
        # Calculate volume of a cube
        if type(length) != float:
            print "Length needs to be floating decimal, but received: " + str(length)
            return 0
        volume = length**3
    elif shape == "sphere":
        # Calculate volume of a sphere
        if type(radius) != float:
            print "Radius needs to be floating decimal, but received: " + str(radius)
            return 0
        pi = 3.14
        volume = 4 * pi * radius**3 / 3
    elif shape == "pyramid":
        # Calculate volume of a pyramid
        if type(length) != float:
            print "Length needs to be floating decimal, but received: " + str(length)
            return 0
        if type(height) != float:
            print "Height needs to be floating decimal, but received: " + str(height)
            return 0
        volume = length**2 * height / 3.0
    else:
        print "Unrecognized shape: " + str(shape)
        return 0
    return volume

length = 5.0
radius = 6.0
height = 8.0

shape = "cube"
print "Cube volume for length " + str(length) + " is " + str(getVolumeForShape(shape, radius, length, height))
shape = "sphere"
print "Sphere volume for radius " + str(radius) + " is " + str(getVolumeForShape(shape, radius, length, height))
shape = "pyramid"
print "Pyramid volume for length " + str(length) + " and height " + str(height) + " is " + str(getVolumeForShape(shape, radius, length, height))
shape = "cone"
print "Cone volume for length " + str(length) + " and height " + str(height) + " is " + str(getVolumeForShape(shape, radius, length, height))

print "\nExercise 4"

length = 1
while length < 11:
    print "Cube volume for length " + str(length) + " is " + str(getVolumeForShape("cube", None, float(length), None))
    length += 1

sys.exit(0)


def altGetVolumeForShape(shape, radius, length, height):
    """
    Calculate the volume of a cube, sphere or four-sided pyramid.
    Returns the volume or 0 for failure.

    shape:  Either "cube", "sphere", or "pyramid"
    radius: The radius of a sphere. "None" if other shape.
    length: The length of the base of a cube or a four-sided pyramid. "None" if other shape.
    height: The height of a four-sided pyramid. "None" if other shape.
    """
    # Validate shape
    if  shape != "cube"   \
    and shape != "sphere" \
    and shape != "pyramid":
        print "Unrecognized shape: " + shape
        return 0

    # Selection of volume based on shape
    if shape == "cube":
        # Calculate volume of a cube
        if type(length) != float:
            print "Length needs to be floating decimal, but received: " + str(length)
            return 0
        volume = length**3
    elif shape == "sphere":
        # Calculate volume of a sphere
        if type(radius) != float:
            print "Radius needs to be floating decimal, but received: " + str(radius)
            return 0
        pi = 3.14
        volume = 4 * pi * radius**3 / 3
    elif shape == "pyramid":
        # Calculate volume of a pyramid
        if type(length) != float:
            print "Length needs to be floating decimal, but received: " + str(length)
            return 0
        if type(height) != float:
            print "Height needs to be floating decimal, but received: " + str(height)
            return 0
        volume = length**2 * height / 3.0

    return volume




