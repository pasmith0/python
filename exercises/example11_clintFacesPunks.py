#!/usr/bin/python2.3
import os, sys
from random import randint

def makeMyDay(numberPunks):
    """
    Clint shoots a punk at random!
    returns 1 for success, 0 for a clean miss

    numberPunks: the number of punks Clint must face down
    """
    if randint(0,1):
        numberPunks -= 1
        print "Go ahead, punk. Make my day..."
        print "One less punk... only " + str(numberPunks) + " to go."
        return True

    return False

eastSidePunks = 10
if makeMyDay(eastSidePunks):
    print "Should only be 9 punks now. There are: " + str(eastSidePunks) + "\n"
else:
    print "Righteous. The punks played it cool.\n"

sys.exit(0)
