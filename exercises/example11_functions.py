#!/usr/bin/python2.3
import os, sys

# import OptionParser function
from optparse import OptionParser

# Create an instance of the parser
parserObj = OptionParser()

# Define a command line option
parserObj.add_option("--start", dest="start", type='int', default=1, 
            help="Optional. The first step the script will execute. Prior steps will be skipped. [Default: 1]")

# Parse the command line
(options, args) = parserObj.parse_args()

# Some examples regarding scope
# Initialize step number to 1
stepNbr = 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    total = 0  # This is global variable.

    def sum( arg1, arg2 ):
       total = arg1 + arg2
       print "Inside the function local total : ", total
       return total

    # Now you can call sum function
    sumVal = sum( 10, 20 )
    print "Outside the function global total : ", total 
    print "Sum is: ", sumVal 


stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    total = 0  # This is global variable.

    def sum( arg1, arg2 ):
       # Use global statement to pull global "total" into local scope
       global total
       total = arg1 + arg2
       print "Inside the function local total : ", total
       return total

    # Now you can call sum function
    sumVal = sum( 10, 20 )
    print "Outside the function global total : ", total 
    print "Sum is: ", sumVal 


stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    total = 0  # This is global variable.

    def sum2( arg1, arg2 ):
       # Use global statement to pull global "total" into local scope
       myTotal = arg1 + total
       print "Inside the function local total : ", myTotal
       return myTotal

    # Now you can call sum function
    sumVal = sum2( 10, 20 )
    print "Outside the function global total : ", total 
    print "Sum is: ", sumVal 


stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    # If a variable is not defined in a function,
    # it will use an available global variable !!
    # --> define all variables within a function !

    total = 25

    def printTotal():
        print "Total is AAA ", total

    printTotal()

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    def foo(x_list):
        x_list.remove(1)
        x_list[2] = [99]    

    x = [0,1,2,3]
    foo(x)
    print str(x)

    def bar(x_list):
        x_list = [4, 5, 6]  # This is a new object, not what x_list originally referred to!

    x = [0,1,2,3]
    bar(x)
    print str(x)

print
sys.exit(0)


