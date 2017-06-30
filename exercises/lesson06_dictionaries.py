#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Python dictionaries are hash tables, also known as associative arrays, \n \
    because data related to a key value is accessed by that key.")
l("Normally, related data is kept in a dictionary, but unrelated data can just as well co-reside.")
l("Because dictionaries use a hash storage scheme, dictionary access does not follow any expected order.")
presentLesson("Containers: Dictionaries", ll, False)

ll = []; l = ll.append
l(["1", "myDict = {}"])
l(["1", "myDict['key'] = 'value'"])
l(["2", "print myDict"])
l(["2", "print len(myDict)"])
l(["2", "print myDict['key']"])
execGroups(ll, "Most basic dictionary")

ll = []; l = ll.append
l(["1", "myDict = {}"])
l(["1", "myDict['dog']  = 'cat'"])
l(["1", "myDict['cat']  = 'bird'"])
l(["1", "myDict['bird'] = 'worm'"])
l(["1", "print myDict"])
l(["2", "print len(myDict)"])
l(["2", "print myDict['cat']"])
l(["2", "print myDict['bird']"])
l(["2", "print myDict['dog']"])
l(["3", "print myDict['hey!!']"])
execGroups(ll, "A simple dictionary")

ll = []; l = ll.append
l(["1", "myDict = {'dog': 'bark', 'cat': 'meow', 'horse': 'winnie'}"])
l(["1", "print myDict"])
l(["1", "print len(myDict)"])
l(["1", "keyList = myDict.keys()"])
l(["1", "                # Any order this happens to be in is just by chance!"])
l(["1", "print keyList"])
l(["3", "print keyList.sort()"])
l(["3", "print keyList"])
execGroups(ll, "List of dictionary keys")

ll = []; l = ll.append
l(["1", "myDict = {'dog': 'bark', 'cat': 'meow', 'horse': 'winnie'}"])
l(["1", "print myDict"])
l(["B2", "if 'cat' in myDict:"])
l(["B2", "    print 'myDict has key: \\'cat\\''"])
execGroups(ll, "Determine if a key exists")

ll = []; l = ll.append
l(["1", "myDict = {}"])
l(["1", "myDict['dog']  = 'cat'"])
l(["1", "myDict['cat']  = 'bird'"])
l(["1", "myDict['bird'] = 'worm'"])
l(["1", "print myDict"])
l(["1", "aKey = 'dog'"])
l(["1", "print myDict[aKey]"])
execGroups(ll, "Variables hold key values")

ll = []; l = ll.append
l(["1", "myDict = {}"])
l(["1", "myDict['dog']  = 'cat'"])
l(["1", "myDict['cat']  = 'bird'"])
l(["1", "myDict['bird'] = 'worm'"])
l(["1", "print myDict"])
l(["1", "keyList = myDict.keys()"])
l(["1", "keyList.sort()"])
l(["B3", "for animal in keyList:"])
l(["B3", "    print 'key: ' + animal + ', can eat ' + myDict[animal]"])
execGroups(ll, "Loop through dictionary keys")

ll = []; l = ll.append
l(["1", "myDict = {}"])
l(["1", "myDict['dog']  = 'cat'"])
l(["1", "myDict['cat']  = 'bird'"])
l(["1", "myDict['bird'] = 'worm'"])
l(["1", "print myDict"])
l(["1", "keyList = myDict.keys()"])
l(["1", "keyList.sort()"])
l(["B3", "for animal, prey in myDict.iteritems():"])
l(["B3", "    print 'key: ' + animal + ', can eat ' + prey"])
l(["B3", "print 'iteritems output: ' + str(myDict.iteritems())"])
l(["B4", "mockList = [ ['bird', 'worm'], ['cat', 'bird'], ['dog', 'cat'] ]"])
l(["B4", "for animal, prey in mockList:"])
l(["B4", "    print 'key: ' + animal + ', can eat ' + prey"])
execGroups(ll, "Loop through dictionary keys and values")

ll = []; l = ll.append
l("Given some data about event attendance and diet restrictions, determine how many of each kind of lunch are needed:\n \
         meat              \n \
         meat-gluten free  \n \
         veggie            \n \
         veggie-gluten free\n\n \
    Here are the starter dictionaries that will feed your logic puzzle (not a real brain-teaser!):\n \
         kidsDict = { 'Adams': ['John', 'Sue'], 'Brown': ['Jennifer'], 'Crow': ['Heidi', 'Paul', 'Betty']}\n \
         kidsDict['Douglas'] = ['Frank', 'Tom', 'Cheryl']\n \
         kidsDict['Jackson'] = ['Marie', 'Shakira', 'Chuck']\n \
           >>  add more, if you want to! \n \
         rsvpList = ['Douglas', 'Crow', 'Jackson']   # Extend, but not ALL will attend  \n \
         veganList = ['Paul Crow', 'Sue Adams', 'Shakira Jackson']\n \
         glutenFreeList = ['Heidi Crow', 'Shakira Jackson']\n\n")
presentLesson("Exercise: Lunch permutations!", ll)
