#!/usr/bin/python
import sys

"""
Subroutines to handle stacks and queues.
"""

# Stack routines (LIFO)

def addToStack(value, stackList):
    stackList.append(value)

def unshiftStack(stackList):
    return stackList.pop()

aaa = []
print "Return value: ", addToStack("a", aaa)
print "Return value: ", addToStack("b", aaa)
print "Return value: ", addToStack("c", aaa)
print "Return value: ", addToStack("d", aaa)
print "New stack with values added to it   : " + str(aaa)

value = unshiftStack(aaa)
print "New stack with value removed from it: " + str(aaa)
print "Value removed from stack: " + value

value = unshiftStack(aaa)
print "New stack with value removed from it: " + str(aaa)
print "Value removed from stack: " + value


# Queue routines (FIFO)

def addToQueue(value, queueList):
    queueList.append(value)

def popQueue(queueList):
    return queueList.pop(0)

aaa = []
print "Return value: ", addToQueue("a", aaa)
print "Return value: ", addToQueue("b", aaa)
print "Return value: ", addToQueue("c", aaa)
print "Return value: ", addToQueue("d", aaa)
print "New queue with values added to it   : " + str(aaa)

value = popQueue(aaa)
print "New queue with value removed from it: " + str(aaa)
print "Value removed from queue: " + value

value = popQueue(aaa)
print "New queue with value removed from it: " + str(aaa)
print "Value removed from queue: " + value

sys.exit(0)
