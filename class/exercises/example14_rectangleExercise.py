#!/usr/bin/python

import math

"""
     Write a program that determines the center point of a rectangle,
     given the length, width and lower-left corner point of the rectangle.

        Devise and use classes for the following:

             1. A point
                    include x and y coordinates
                    a method for the formatted print of the point
                    a method to calculate the distance of the point from the ori
             2. A rectangle.
                    include the length, width, and corner point as attributes
                    a method to find the xCoord of the central point of the rec
                    a method to find the yCoord of the central point of the rec
                    a method to determine and report the central point
                    a method to report the distance of the central point from the origin
"""

class Point:
    def __init__(self, xCoord, yCoord):
        self.xCoord = xCoord
        self.yCoord = yCoord

    def showPoint(self, preamble=""):
        print preamble + '(' + str(self.xCoord) + ", " + str(self.yCoord) + ")"

    def distFromOrigin(self):
        self.distance = math.sqrt(self.xCoord ** 2  +  self.yCoord ** 2)

class Rectangle:
    def __init__(self, length, width, xCoord, yCoord):
        self.length = length
        self.width  = width
        self.xCoord = xCoord
        self.yCoord = yCoord

    def getCentralX(self):
        return self.xCoord + 0.5 * self.width

    def getCentralY(self):
        return self.yCoord + 0.5 * self.length

    def presentCenter(self, x, y):
        centerPoint = Point(x, y)
        centerPoint.showPoint("The rectangle's center point is at ")
        centerPoint.distFromOrigin()
        print "Distance of center point from origin: " + str(centerPoint.distance)

myRectangle = Rectangle(12, 15, 4, 7)
myRectangle.presentCenter(myRectangle.getCentralX(), myRectangle.getCentralY())













