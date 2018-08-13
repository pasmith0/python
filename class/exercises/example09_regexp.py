#!/usr/bin/python
import os, sys

# For regular expression support
import re

# import OptionParser function
from optparse import OptionParser

# Create an instance of the parser
parserObj = OptionParser()

# Define a command line option
parserObj.add_option("--start", dest="start", type='int', default=1, 
            help="Optional. The first step the script will execute. Prior steps will be skipped. [Default: 1]")

# Parse the command line
(options, args) = parserObj.parse_args()


aaa = """Mary had 932 lambs, whose fleece was white as snow,
and everywhere that Mary went, her sheep were sure to go.
(and let me tell you, they take up a lot of room!)
"""

bbb = "a big dog followed a big cat"

ccc = """a big dog followed a 
big cat
"""

# Initialize step number to 1
stepNbr = 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    if re.search("^Mary", aaa):
        print "There's something about Mary..."
    else:
        print "This sentence doesn't start with Mary."

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    if re.search(".*, whose", aaa):
        print "Found comma plus whose"
    else:
        print "No comma plus whose. Why not?"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    m = re.search("^Mary had (?P<count>\d+) lambs", aaa)
    if m:
        print "Parsed " + m.group('count') + " number of lambs"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    m = re.search("^Mary had (?P<count>\d+) lambs.*fleece was (?P<color>\w+)\s", aaa)
    if m:
        print "Parsed " + m.group('count') + " number of " + m.group('color') + " lambs"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    m = re.search("\nand", aaa)
    if m:
        print "Found 'and' after newline"
    else:
        print "No 'and' after newline"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    m = re.search(".*and\s*(?P<afterand>\w+)", aaa)
    if m:
        print "After 'and', there is '" + m.group('afterand') + "'"
    else:
        print "no match"

    m = re.search(".*?and\s*(?P<afterand>\w+)", aaa)
    if m:
        print "After 'and', there is '" + m.group('afterand') + "'"
    else:
        print "no match"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    m = re.search(".*big (?P<animal>\w+)", bbb)
    print "After 'big' there is '" + m.group('animal') + "'"

    m = re.search(".*?big (?P<animal>\w+)", bbb)
    print "After 'big' there is '" + m.group('animal') + "'"

    m = re.search(".*big (?P<animal>\w+)", ccc)
    print "After 'big' there is '" + m.group('animal') + "'"

    m = re.search(".*?big (?P<animal>\w+)", ccc)
    print "After 'big' there is '" + m.group('animal') + "'"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    m = re.search(".*big (?P<animal>\w+)", ccc, flags=re.DOTALL)
    print m.group('animal')

    m = re.search(".*?big (?P<animal>\w+)", ccc, flags=re.DOTALL)
    print m.group('animal')

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    m = re.search(".*and\s*(?P<afterand>\w+)", aaa, flags=re.DOTALL)
    if m:
        print "After 'and', there is '" + m.group('afterand') + "'"
    else:
        print "no match"

    m = re.search(".*?and\s*(?P<afterand>\w+)", aaa, flags=re.DOTALL)
    if m:
        print "After 'and', there is '" + m.group('afterand') + "'"
    else:
        print "no match"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    if re.search("(and", aaa):
        print "Found 'and' after a paren"
    else:
        print "No 'and' after a paren"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    if re.search("\(and", aaa):
        print "Found 'and' after a paren"
    else:
        print "No 'and' after a paren"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    aaa = '{"list":["MBOUI"]}'
    m = re.search("\"list\"\:\[(?P<processes>.*?)\]", aaa)
    if m:
        print m.group('processes')
    else:
        print "no dice"

stepNbr += 1
if options.start <= stepNbr:
    print "\nStep: " + str(stepNbr) + "\n"

    compatibilityDict = {}
    for line in ["aaa-5.7.8:   5.5.5,  6.6.6,   7.7.7,   8.8.8"]:
        if  not re.search("^\s*#.*$", line) \
        and re.search("^.*?:", line):
            (key, val) = line.split(":", 1)
            if key: compatibilityDict[key.strip()] = val.replace(" ", "").split(",")
            if len(compatibilityDict[key.strip()]) != 4: print "hey, not 4"

sys.exit(0)





