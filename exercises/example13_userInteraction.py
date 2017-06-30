#!/usr/bin/python2.3
import string
import sys
import os
import time
import re

# Present a menu of choices to the user, who then selects one.
# Optionally allow the user to select multiple choices before 
# okaying final set of selections.

foundLibrary = False
sys.path.append("/home/mystro/lib")
try: 
    from upgradeLibrary import *
    foundLibrary = True
except:
    pass
if not foundLibrary: 
    print "ERROR: Could not source upgradeLibrary.py."
    sys.exit(1)

# Present a menu of choices to the user, who then selects one.
# Optionally allow the user to select multiple choices before 
# okaying final set of selections.

def displayMenu(headingList, optionList, selectionDict):
    os.system("clear")
    print "\n\n"
    maxLen = 0
    for headingLine in headingList:
        print "     " + headingLine
        if len(headingLine) > maxLen: maxLen = len(headingLine)
    print "     " + "="*maxLen + "\n"
    optionNumber = 0
    for option in optionList:
        optionNumber += 1
        if  option in selectionDict \
        and selectionDict[option]:
            selectedInd = "_X_"
        else:
            selectedInd = "___"
        print "      " + selectedInd + " " + str(optionNumber).rjust(3) + ".  " + option
    print "\n"

def promptUserSelections(maxSelection):
    # Infinite loop
    while True:
        result = raw_input("Please enter your selections separated by commas, or 'q' to exit: ")
        result = result.replace(" ", "")
        if result.lower() in ['q', 'quit']:
            return 'q'
        elif re.search("^[,0-9]+$", result):
            selectionsOkay = True
            selectionList = result.split(",")
            for selection in selectionList:
                if int(selection) not in range(1, maxSelection + 1):
                    print "Selection is out of range..."
                    selectionsOkay = False
            if selectionsOkay:
                return selectionList
        else:
            print "Unrecognized result..."

def promptUserConfirmation(result):
    # Infinite loop
    while True:
        result = raw_input("Do you accept those selections? Respond 'y', 'n' or 'q' to exit: ")
        if result.lower() in ['q', 'quit']:
            return 'q'
        elif result.lower() in ['y', 'yes', 'n', 'no']:
            return result
        else:
            print "Unrecognized result..."
            time.sleep(4)

def interactMenu(headingList, optionList):
    selectionDict = {}
    result = []
    while True:
        displayMenu(headingList, optionList, selectionDict)
        if result:
            confirm = promptUserConfirmation(result)
            if confirm.lower() in ['q', 'quit']:
                return 0
            elif confirm.lower() in ['y', 'yes']:
                break
            elif confirm.lower() in ['n', 'no']:
                selectionDict = {}
        displayMenu(headingList, optionList, selectionDict)
        result = promptUserSelections(len(optionList))
        if type(result) != list: return 0
        result.sort()
        selectionDict = {}
        for index in result:
            selectionDict[optionList[int(index) - 1]] = True
    return result


# >>> Main Program <<<

headingList = ["Upgrade Menu", "Make your selections"]
optionList  = ["ECP", "SIA", "RCEA"]
result = interactMenu(headingList, optionList)
if not result:
    print "User quit program, exiting..."
    sys.exit(1)
elif not len(result):
    print "User made no selections, exiting..."
    sys.exit(1)
else:
    print "User chose selections: " + str(result) + ". Processing them..."

sys.exit(0)





