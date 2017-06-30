#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Lists and tuples are essentially arrays of data. They contain data items that can be accessed by index.")
l("They are the same except that tuples cannot be altered. Tuples, like strings and numbers, are called 'immutable'.")
l("|| So, how do you pronouce 'tuple'?                    \n  \
   || Some say like 'couple'; others say like 'quadruple'.\n  \
   || It's likely meant to sound like 'quintuple', 'sextuple', etc...")
l("A comma is the tuple constructor. This is a one-tuple: '12,'  This is not: '(12)' \n \
        The first,  '12,'  evaluates to '(12,)', as does '(12,)'. So, don't forget the comma! And the parens look good.\n \
        The second, '(12)' evaluates to '12', not a tuple at all...")
l("A zero-tuple does not require the comma, but just empty parens:  '()' evaluates to '()'")
l("Any higher than a one-tuple does not require an ending comma, like this: '(\"a\", \"b\", \"c\")'")
presentLesson("Containers: Lists and Tuples", ll, False)

ll = []; l = ll.append
l(["1", "myList = [40, 50, 60, 70]"])
l(["1", "print myList"])
l(["2", "print len(myList)"])
l(["3", "print myList[0]"])
l(["4", "print myList[1]"])
l(["4", "print myList[2]"])
l(["4", "print myList[3]"])
l(["5", "print myList[4]"])
execGroups(ll, "a Basic List of Integers")

ll = []; l = ll.append
l(["1", "myTuple = (40, 50, 60, 70)"])
l(["1", "print myTuple"])
l(["1", "print len(myTuple)"])
l(["2", "print myTuple[0]"])
l(["2", "print myTuple[1]"])
l(["2", "print myTuple[2]"])
l(["2", "print myTuple[3]"])
l(["2", "print myTuple[4]"])
execGroups(ll, "a Basic Tuple of Integers")

ll = []; l = ll.append
l(["1", "myList = [40, 50.0, '60', type(70), 45 - 12, 10 < 100]"])
l(["1", "print myList"])
l(["1", "print len(myList)"])
l(["1", "print myList[0]"])
l(["1", "print myList[1]"])
l(["1", "print myList[2]"])
l(["1", "print myList[3]"])
l(["1", "print myList[4]"])
l(["1", "print myList[5]"])
execGroups(ll, "a Basic List of Mixed Type")

ll = []; l = ll.append
l(["1", "myList = [ 40, \\\n               50, \\\n               60, \\\n               70  \\\n             ]"])
l(["1", "print myList"])
execGroups(ll, "Use of Continuation to keep it neat and maintainable")

ll = []; l = ll.append
l(["1", "myList = [ 40, \n               50, \n               60, \n               70  \n             ]"])
l(["1", "print myList"])
execGroups(ll, "But a continuation char isn't really needed!")

ll = []; l = ll.append
l("Everything in Python is an object, meaning it has stored attributes and subroutines called 'methods'. \n \
    The methods for lists make them useful.")
l("List methods allow for adding, deleting, inserting and changing list values, as well as selecting 'slices,' or subsets, of lists.")
l("Tuples lack any methods that would alter them.")
presentLesson("Lists Methods", ll)

ll = []; l = ll.append
l(["1", "employeeAgeList = []"])
l(["1", "employeeAgeList.append(30)"])
l(["1", "employeeAgeList.append(53)"])
l(["1", "employeeAgeList.append(29)"])
l(["1", "employeeAgeList.append(37)"])
l(["1", "employeeAgeList.append(72)"])
l(["2", "print employeeAgeList"])
l(["2", "print len(employeeAgeList)"])
execGroups(ll, "Another Way to Build a List")

ll = []; l = ll.append
l(["1", "employeeAgeList = [30, 53, 29, 37, 72]"])
l(["1", "print employeeAgeList"])
l(["1", "            # Find the index of value 37."])
l(["1", "myIndex = employeeAgeList.index(37)"])
l(["1", "print myIndex"])
l(["2", "            # Find the index of value 999."])
l(["2", "myIndex = employeeAgeList.index(999)"])
l(["2", "print myIndex"])
execGroups(ll, "Find the first index of a value in the list")

ll = []; l = ll.append
l(["1", "employeeAgeList = [30, 53, 29, 37, 72]"])
l(["1", "print employeeAgeList"])
l(["1", "print len(employeeAgeList)"])
l(["2", "            # Removes by 'value'. Deletes the first matching value found."])
l(["2", "employeeAgeList.remove(72)"])
l(["2", "print employeeAgeList"])
l(["2", "print len(employeeAgeList)"])
l(["3", "            # Deletes by 'index'"])
l(["3", "del employeeAgeList[2]"])
l(["3", "            # Note that the list is re-indexed anytime it's changed."])
l(["3", "print employeeAgeList"])
l(["3", "print len(employeeAgeList)"])
execGroups(ll, "Removing a List Value")

ll = []; l = ll.append
l(["1", "myList = [40, 50, 60, 70]"])
l(["1", "print myList"])
l(["2", "            # Make the value 'new' the value for index 2"])
l(["2", "myList.insert(2, 'new')"])
l(["2", "            # Note that the rest of the list adjusts to higher indexes"])
l(["2", "print myList"])
l(["2", "print len(myList)"])
execGroups(ll, "Inserting a List Value")

ll = []; l = ll.append
l(["1", "employeeAgeList = [30, 53, 29, 37, 72]"])
l(["1", "print employeeAgeList"])
l(["1", "print len(employeeAgeList)"])
l(["2", "            # Increment the first value"])
l(["2", "employeeAgeList[0] += 1"])
l(["2", "            # Change the fifth value to 64"])
l(["2", "employeeAgeList[4] = 64"])
l(["2", "print employeeAgeList"])
l(["2", "print len(employeeAgeList)"])
execGroups(ll, "Changing a List Value")

ll = []; l = ll.append
l(["1", "employeeAgeList = [30, 53, 29, 37, 72]"])
l(["1", "print employeeAgeList"])
l(["1", "            # sort() outputs None"])
l(["1", "print employeeAgeList.sort()"])
l(["2", "            # --> and sorts the list in place"])
l(["2", "print employeeAgeList"])
l(["3", "employeeAgeList = [30, 53, 29, 37, 72]"])
l(["3", "print employeeAgeList"])
l(["3", "            # For python 2.6+, sorted() returns the sorted list and leaves the original unchanged"])
l(["3", "print sorted(employeeAgeList)"])
execGroups(ll, "Sorting a list: sort() and sorted()")

ll = []; l = ll.append
l(["1", "employeeAgeList = [30, 53, 29, 37, 72]"])
l(["1", "print employeeAgeList"])
l(["1", "            # sort() outputs None"])
l(["1", "print employeeAgeList.sort()"])
l(["1", "            # --> and sorts the list in place"])
l(["1", "print employeeAgeList"])
l(["1", "            # reverse() outputs None"])
l(["1", "print employeeAgeList.reverse()"])
l(["1", "            # --> so now the list is sorted in reverse order"])
l(["1", "print employeeAgeList"])
execGroups(ll, "Reversing a list: reverse()")

ll = []; l = ll.append
l("Create a list of people's names: Bob, Mark, Sarah, Keith, Nicole, Renee, Keith.\n \
    Add to that list another name: Luigi.\n \
    Remove from that list: Keith.\n \
    Insert 'Elaine' just after Nicole.\n \
    Change the name Bob to Robert")
l("Print out your list.")
presentLesson("Exercise: Build and Alter A List", ll)

ll = []; l = ll.append
l(["1", "nameList = ['Bob', 'Mark', 'Sarah', 'Keith', 'Nicole', 'Renee', 'Keith']"])
l(["1", "print nameList"])
l(["1", "            # Luigi is added to the end of the list"])
l(["1", "nameList.append('Luigi')"])
l(["1", "print nameList"])
l(["1", "            # Removes the first (lowest indexed) value of 'Keith'"])
l(["1", "nameList.remove('Keith')"])
l(["1", "print nameList"])
l(["1", "nameList.insert(4, 'Elaine')"])
l(["1", "print nameList"])
l(["1", "nameList[0] = 'Robert'"])
l(["1", "print nameList"])
execGroups(ll, "")

# Aliasing lists and tuples
ll = []; l = ll.append
l("As noted previously, multiple variables pointing to the same mutable list each can change the list.")
l("So altering a list through one variable changes the list for any other variables aliased to it.")
l("If you pass a list variable to a function, and the function changes the list, then it is also changed in the calling routine!")
presentLesson("Aliased variables for lists", ll)

ll = []; l = ll.append
l(["1", "nameList = ['Bob', 'Mark', 'Sarah', 'Keith', 'Nicole', 'Renee', 'Keith']"])
l(["1", "print nameList"])
l(["2", "            # Aliasing is done through assignment"])
l(["2", "myNameList = nameList"])
l(["2", "print myNameList"])
l(["3", "            # Removes the first (lowest indexed) value of 'Keith'"])
l(["3", "nameList.remove('Keith')"])
l(["3", "print nameList"])
l(["3", "            # myNameList has changed! That's because it's the same list."])
l(["3", "print myNameList"])
execGroups(ll, "Aliased list variables")

ll = []; l = ll.append
l('global popList')
l("def popList(aList):")
l("    return aList.pop()")
execCodeBlock(ll, "Aliased list variables passed to a function")
ll = []; l = ll.append
l(["1", "myList = [1, 2, 3, 4, 5]"])
l(["2", "print popList(myList)"])
l(["2", "            # myList has changed!"])
l(["2", "print myList"])
execGroups(ll)

ll = []; l = ll.append
l("The builtin 'list' function makes a list object of a sequence.\n \
    If it operates on a list, it returns a copy of the list, not an alias.")
l("The basic sequence types: strings, Unicode strings, lists and tuples. \n \
    'list' also operates on dictionaries, but only on the keys.")
presentLesson("The 'list' function", ll)

ll = []; l = ll.append
l(["1", "print list('a')"])
l(["2", "print list('Python')"])
l(["3", "print list(['a', 'b', 'c'])"])
l(["4", "print list((1,))"])
l(["5", "print list((1,4,6))"])
l(["6", "print list({'a':4, 'b':7})"])
l(["7", "print list(24)"])
execGroups(ll, "The list function")

ll = []; l = ll.append
l(["1", "listX = ['a', 'b', 'c']"])
l(["1", "listA = listX"])
l(["2", "listB = list(listX)"])
l(["3", "listA.remove('b')"])
l(["3", "print listX"])
l(["4", "listB.remove('c')"])
l(["4", "print listB"])
l(["4", "print listX"])
execGroups(ll, "The list function copies a list")

ll = []; l = ll.append
l("Lists can be used to implement FIFO 'queues' and LIFO 'stacks'.")
l("Just like a 'queue' of customers waiting in line at the bank, the first in the queue gets processed first.")
l("    last in --> 3  \n \
                    2 \n \
                    1 \n \
                    0 --> first in, first out")
l("Just like a 'stack' of plates in a cupboard, the last plate put on the stack gets processed (used) first.")
l("    last in --> 3 --> last in, first out \n \
                    2 \n \
                    1 \n \
                    0")

l("Lists have methods to process them as either stacks or queues.")
l("Actions to 'push' values to the end of a queue or stack are needed. The append() method does that.")
l("Actions to 'pop' values from the end of a stack or the front or a queue are needed. And they need to return the value for processing.")
presentLesson("Lists used as Stacks or Queues", ll)

ll = []; l = ll.append
l(["1", "myList = [40, 50, 60, 70]"])
l(["1", "print myList"])
l(["1", "myList.append(80)"])
l(["1", "print myList"])
l(["2", "a = myList.pop()"])
l(["3", "print myList"])
l(["3", "print a"])
l(["4", "a = myList.pop()"])
l(["4", "print myList"])
l(["4", "print a"])
execGroups(ll, "Stack Methods: append() and pop()")

ll = []; l = ll.append
l(["1", "myList = [40, 50, 60, 70]"])
l(["1", "print myList"])
l(["1", "myList.append(80)"])
l(["1", "print myList"])
l(["1", "a = myList.pop(0)"])
l(["2", "print myList"])
l(["2", "print a"])
l(["3", "a = myList.pop(0)"])
l(["4", "print myList"])
l(["4", "print a"])
execGroups(ll, "Queue Methods: append() and pop(0)")

ll = []; l = ll.append
l("What if you need part of a list, not just a single value?")
l("Python allows referencing of 'slices' of a list.")
l("    A slice:   [ <first index> : <one after the last index> ]")
presentLesson("List slices", ll)

ll = []; l = ll.append
l(["1", "myList = [40, 50, 60, 70, 80, 90]"])
l(["1", "print myList"])
l(["1", "            # prints a sublist of indexes 1 thru 2, noninclusive of index 3"])
l(["1", "print myList[1:3]"])
l(["2", "            # prints a sublist of indexes 1 thru end-of-list"])
l(["2", "print myList[1:]"])
l(["3", "            # Indexes can be negative too! Prints the last value in the list."])
l(["3", "print myList[-1]"])
l(["4", "            # prints a sublist of the two values nearest the last value of the list, noninclusive of the last value"])
l(["4", "print myList[-3:-1]"])
l(["5", "            # prints a sublist of the last three values in the list"])
l(["5", "print myList[-3:]"])
l(["6", "            # prints a sublist of the first two values in the list"])
l(["6", "print myList[:2]"])
execGroups(ll, "Slices")

ll = []; l = ll.append
l(["1", "myList = [40, 50, 60, 70, 80, 90]"])
l(["1", "print myList"])
l(["2", "myList[1:3] = ['here', 'we', 'go!']"])
l(["3", "print myList                     # Indexes 1 and 2 were replaced by a longer sublist"])
execGroups(ll, "List Assignment Using Slices")

ll = []; l = ll.append
l("The range() function appeared in a 'for' loop already, but you didn't know it outputs a list.")
l("When range() gets a single parameter, 'value', it outputs a list of [0,..., value-1].")
l("When range() gets two parameters, val1 and val2, it outputs a list of [val1,..., val2-1].")
presentLesson("The range() function", ll)

ll = []; l = ll.append
l(["1", "            # Prints a list containing 0 thru 3"])
l(["1", "print range(4)"])
l(["2", "            # Prints a list containing 0 thru 3"])
l(["2", "print range(0, 4)"])
l(["3", "            # Prints a list containing 2 thru 7"])
l(["3", "print range(2, 8)"])
l(["4", "myList = [40, 50, 60, 70, 80, 90]"])
l(["4", "            # Prints the indexes for myList. Very useful!"])
l(["4", "print range(len(myList))"])
l(["5", "            # Prints a list containing 2 thru 9 by twos. Note '9' does not apply."])
l(["5", "print range(2, 10, 2)"])
l(["6", "            # Prints a list containing 10 thru 3 in reverse order."])
l(["6", "print range(10, 2, -1)"])
l(["7", "            # Prints a list containing 10 thru 3 in reverse order by threes."])
l(["7", "print range(10, 2, -3)"])
l(["8", "            # Prints a list containing len(myList) thru 1 in reverse order."])
l(["8", "print range(len(myList), 0, -1)"])
l(["9", "            # Prints an empty list, because -1 does not follow 6"])
l(["9", "print range(len(myList), -1)"])
execGroups(ll, "range() function")

ll = []; l = ll.append
l("myList = [40, 50, 60, 70, 80, 90]")
l('for value in myList:')
l("    print value")
execCodeBlock(ll, "Loop over a list")

ll = []; l = ll.append
l("myList = [40, 50, 60, 70, 80, 90]")
l('for index in range(len(myList)):')
l("    print myList[index]")
execCodeBlock(ll, "Loop over a list's indexes")

ll = []; l = ll.append
l("Create subroutines to push and pop values from a queue list. Returns the popped value and/or the new list.\n \
    Create subroutines to shift and unshift values from a stack list. Returns the popped value and/or the new list.'")
presentLesson("Exercise: Create subroutines to handle stacks and queues", ll)

sys.exit(0)
