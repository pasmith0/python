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
    # Test each condition in trueList and falseList

    trueList  = [ True, 1, -1, ' ', [''], {'a': 'b'} ]
    falseList = [ False, None, 0, '', [], {} ]

    # Display a condition as true or false
    def testCondition(cond):
        condDisplay = "|" + str(cond) + "|"
        if cond: 
            print condDisplay.ljust(12) + " is True"
        else:
            print condDisplay.ljust(12) + " is False"

    for a in trueList:
        testCondition(a)

    print 

    for a in falseList:
        testCondition(a)

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"
    
    # What happens if a variable does not exist?

    if undefVar:
        print "do some work"
    else:
        print "do something else"


stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"
    
    # What happens if a variable does not exist?

    def testVariableExists(testVar):
        if testVar in globals():
            return True
        return False

    if testVariableExists('undefVar'):
        print "do some work"
    else:
        print "nothing to do, man"

    myVar = "I am here!"
    if testVariableExists('myVar'):
        print "do some work"
    else:
        print "nothing to do, man"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    # A simple switch arrangement

    def sortKeys(theDict):
        theDictKeyList = theDict.keys()
        theDictKeyList.sort()
        return theDictKeyList

    tally = {}
    tally["00to20"] = 0
    tally["20to30"] = 0
    tally["30to50"] = 0
    tally["50to80"] = 0
    tally["over80"] = 0

    employeeSalary = 55000

    if   employeeSalary < 20000:
        tally["00to20"] += 1
    elif employeeSalary < 30000:
        tally["20to30"] += 1
    elif employeeSalary < 50000:
        tally["30to50"] += 1
    elif employeeSalary < 80000:
        tally["50to80"] += 1
    else:
        tally["over80"] += 1

    for category in sortKeys(tally):
        print "Number employees making " + category + " is " + str(tally[category]) 

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    # A compound condition

    a = 20
    b = 1

    if  a == 20 and b < 45:
        print "Condition met"
    else:
        print "no dice!"

    if  ( a == 20 and b < 45 ):
        print "Condition met"
    else:
        print "no dice!"

    if  (a == 20) and (b < 45):
        print "Condition met"
    else:
        print "no dice!"

    if  ( (a == 20) and (b < 45) ):
        print "Condition met"
    else:
        print "no dice!"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    # You can line up the 'and' with the 'if' so the conditions form a column
    if  a == 20  \
    and b < 45:
        print "Condition met"
    else:
        print "no dice!"

    # When I use parens on multiple lines, the 'and' goes with them!
    if  (   a == 20  \
        and b <  45  \
        ):
        print "Condition met"
    else:
        print "no dice!"

    # Now for something more complicated...

    if  (   (   a == 20  \
            and b <  45  \
            )            \
        or  (   a == 25  \
            and b >  45  \
            )            \
        ):
        print "Condition met"
    else:
        print "no dice!"

    # But also without the encompassing parens...

    if  (   a == 20  \
        and b <  45  \
        )            \
    or  (   a == 25  \
        and b >  45  \
        ):
        print "Condition met"
    else:
        print "no dice!"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    # Getting tricky with 'or'...
    # If first condition is false, then the second is used
    # If first condition is true, then it is used

    a = 4
    default = 10

    c = a or default
    print "c ends up: " + str(c)

    a = 0
    c = a or default
    print "c ends up: " + str(c)

    # Example, empty directory, versus non-empty directory

    directory  = ""
    defaultDir = "."
    myDir      = directory or defaultDir
    print "Selected dir: " + myDir

    directory  = "/usr/local/mystro"
    defaultDir = "."
    myDir      = directory or defaultDir
    print "Selected dir: " + myDir

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    # Getting tricky with 'and'...
    # If first condition is false, then it is used
    # If first condition is true, then the second is used

    # Example, one way to use the lesser of a or b
    a = 4
    b = 10

    c = ((a < b) and a ) or b
    print "c ends up: " + str(c)

    a = 10
    b = 5
    c = ((a < b) and a ) or b
    print "c ends up: " + str(c)

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    # Example, one way to use the greater of a or b
    a = 4
    b = 10

    c = ((a > b) and a ) or b
    print "c ends up: " + str(c)

    a = 20
    b = 5
    c = ((a > b) and a ) or b
    print "c ends up: " + str(c)

sys.exit(0)




































sys.exit(0)
