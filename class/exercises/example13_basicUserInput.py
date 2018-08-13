#!/usr/bin/python
import os, sys

def getUserInput(prompt, number=False):
    while True:
        result = raw_input(prompt + ": ")
        # Test for empty string and type
        if result.strip():
            if number:
                if result.strip().isdigit():
                    break
            else:
                break
    return result.strip()

promptList = [ ["first name", False], ["last name", False], ["home town", False], ["age", True], ["salary", True] ]

print "all kinds of instructions... q to quit"
while True:
    rList = []
    for prompt, number in promptList:
        rList.append(getUserInput(prompt, number=number))
        if rList[-1].lower() == "q":
            sys.exit(0)
    print rList[0] + " " + rList[1] + " lives in " + rList[2] + " and makes $" + rList[4] + ". Not bad for " + rList[3] + " years old!"

sys.exit(0)
