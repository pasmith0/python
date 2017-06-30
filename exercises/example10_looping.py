#!/usr/bin/python
import sys

# import OptionParser function
from optparse import OptionParser

# Create an instance of the parser
parserObj = OptionParser()

# Define a command line option
parserObj.add_option("--start", dest="start", type='int', default=1, 
            help="Optional. The first step the script will execute. Prior steps will be skipped. [Default: 1]")

# Parse the command line
(options, args) = parserObj.parse_args()


# Initialize step number to 1
stepNbr = 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    # while loop with break to end infinite loop
    aaa = ""
    maxstring = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    while True:
        print "Somebody stop me!!!!!"
        aaa += "x"
        if aaa == maxstring:
            break      

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"
    # while loop with continue to print odd numbers < 20 and > 40 within range
    # and to quit for numbers over 60
    # Use pass statement to do nothing on exception.
    test = 0
    while test < 100:
        try:
            test += 1
            if test % 2:
                if test in range(20, 41):
                    continue
                if test > 60:
                    break
                print "Odd number: " + str(test)
        except:
            pass
            
stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"
    # Test each condition in trueList and falseList

    testList  = [ [], {}, True, 1, '', -1, False, ' ', [''], None, 0, {'a': 'b'} ]

    # Display a condition as true or false
    def testCondition(cond):
        condDisplay = "|" + str(cond) + "|"
        if cond: 
            print condDisplay.ljust(12) + " is True"
        else:
            print condDisplay.ljust(12) + " is False"

    for test in testList:
        testCondition(test)

    print 

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    # Read directly from a file.
    lineCount = 0
    for line in open("./lesson10_looping.py"):
        lineCount += 1
    print "Lines in ./lesson10_looping.py are: " + str(lineCount)

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    outerList = [ ["a", "w"], ["b", "x"], ["c", "y"], ["d", "z"] ]

    # loop through a list of lists
    for charA, charB in outerList:
        print charA + "  " + charB

    print

    # alt loop through a list of lists
    for innerList in outerList:
        print innerList[0] + "  " + innerList[1]
        for inner in innerList:
            print inner

    print

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    stringList = [ "aaa", "bbb", "ccc", "ddd" ]

    # loop through index and values using 'enumerate'
    for index, value in enumerate(stringList):
        print str(index) + "  " + str(value)

    print

    # loop through index and values using 'zip'
    for index, value in zip(range(len(stringList)), stringList):
        print str(index) + "  " + str(value)

    print

    # loop through two lists side by side using 'zip'
    otherList = [ "www", "xxx", "yyy", "zzz" ]
    for one, two in zip(otherList, stringList):
        print str(one) + "  " + str(two)

    print

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    # loop through characters in a string, print ASCII values
    for char in "[mystroMAS] cd /home/mystro/rpms":
        print "Char: " + char + ",  ASCII: " + str(ord(char))

    print

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    # use continue in a for loop
    outString = ""
    for char in "xTxxxhxisxx xstxrxxxinxgxx xxhaxsx xxsxxtxxraxxxyx excxkxsxexs":
        if char == "x":
            continue
        outString += char

    if outString:
        print "Clean string: " + outString

    print

sys.exit(0)




































sys.exit(0)
