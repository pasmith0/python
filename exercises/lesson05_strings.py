#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Strings are immutable objects with a host of methods to interrogate them, parse them or split them up.")
l("Many methods that act on strings treat them as though they were lists of characters.")
presentLesson("String Methods", ll, False)

ll = []; l = ll.append
l(["1", "a = 'Mary hadn\\'t a clue where her little lamb \"Mimsy\" was.'"])
l(["1", "print a"])
execGroups(ll, "Escape strings - quotes I")

ll = []; l = ll.append
l(["1", 'a = "Mary hadn\'t a clue where her little lamb \\"Mimsy\\" was."'])
l(["1", "print a"])
execGroups(ll, "Escape strings - quotes II")

ll = []; l = ll.append
l(["1", "a  = 'Mary thought it was either:\\n'"])
l(["1", "a += '      in the barn,\\n'"])
l(["1", "a += '      in the paddock,\\n'"])
l(["1", "a += '      or in the wolf!'"])
l(["1", "print a"])
execGroups(ll, "Escape strings - newline")

ll = []; l = ll.append
l(["1", "underline = '='"])
l(["1", "title = 'How to Thrill an Audience in 300 Minutes'"])
l(["1", "print title + '\\n' + underline*len(title)"])
execGroups(ll, "Repeat a string")

ll = []; l = ll.append
l(["1", "a = '   This string begins and ends with spaces.   '"])
l(["1", "print '###' + a + '###'"])
l(["1", "print '###' + a.strip() + '###'"])
execGroups(ll, "Strip a string of leading and/or trailing white space")

ll = []; l = ll.append
l(["1", "a = 'xxxThis string begins and ends with x\\'s.xxx'"])
l(["1", "print '###' + a + '###'"])
l(["1", "print '###' + a.strip('x') + '###'"])
execGroups(ll, "Strip a string of leading and/or trailing chars")

ll = []; l = ll.append
l(["1", "a = 'Mary had a little lamb. How about that!!'"])
l(["1", "print a[21] + ' should say \"b\"'"])
execGroups(ll, "String Indexes")

ll = []; l = ll.append
l(["1", "a = 'Mary had a little lamb. How about that!!'"])
l(["1", "print a[:4] + ' should say \"Mary\"'"])
execGroups(ll, "String Slices")

ll = []; l = ll.append
l(["1", "a = 'Mary had a little lamb. How about that!!'"])
l(["1", "print a.split()"])
execGroups(ll, "Split a string on spaces")

ll = []; l = ll.append
l(["1", "a = 'mas, bms01, bms02, bms03, bms04, bms05, bms06, pmg'"])
l(["1", "print a.split(',')"])
execGroups(ll, "Split a string on commas")

ll = []; l = ll.append
l(["1", "a  = 'Mary thought it was either:\\n'"])
l(["1", "a += '      in the barn,\\n'"])
l(["1", "a += '      in the paddock,\\n'"])
l(["1", "a += '      or in the wolf!'"])
l(["1", "print a.splitlines()"])
execGroups(ll, "Split a string on newlines")

ll = []; l = ll.append
l(["1", "a = 'Mary had a little lamb. How about that!!'"])
l(["1", "b = a.find('lamb')"])
l(["1", "print a[b:b+4]"])
execGroups(ll, "Find a substring in a string")

ll = []; l = ll.append
l(["1", "a = 'Mary had a little lamb. How about that!!'"])
l(["1", "b = a.find('lamb')"])
l(["1", "c = len('lamb')"])
l(["1", "print a[b:b+c]"])
execGroups(ll, "Find a substring in a string")

ll = []; l = ll.append
l(["1", "aaa = 'Mary had a little lamb. How about that!!'"])
l(["1", "a = aaa.find('Mary')"])
l(["1", "b = aaa.find('lamb')"])
l(["1", "c = aaa.find('lion')"])
l(["1", "print 'a: ' + str(a) + ', and b: ' + str(b) + ', and c: ' + str(c)"])
execGroups(ll, "Find a substring in a string")

ll = []; l = ll.append
l(["1", "aaa = 'Mary had a little lamb. How about that!!'"])
l(["1", "a = aaa.find('lamb')"])
l(["1", "bbb = aaa[:a] + 'gazelle' + aaa[a+len('lamb'):]"])
l(["1", "print bbb"])
execGroups(ll, "Replace a substring")

ll = []; l = ll.append
l(["1", "aaa = 'Mary had a little lamb. How about that!!'"])
l(["1", "a = aaa.startswith('Mary')"])
l(["1", "print a"])
l(["1", "aaa = 'Mary had a little lamb. How about that!!'"])
l(["1", "a = aaa.startswith('lamb')"])
l(["1", "print a"])
l(["1", "a = aaa.endswith('Mary')"])
l(["1", "print a"])
l(["1", "aaa = 'Mary had a little lamb. How about that!!'"])
l(["1", "a = aaa.endswith('!!')"])
l(["1", "print a"])
execGroups(ll, "startswith() and endswith()")


ll = []; l = ll.append
l("Python has no 'substring' or 'replace' methods for strings.\n \
    Write subroutines of your own:\n \
        'substring' returns characters from a given starting point for a specified number of characters.\n \
        'replace'   returns a string where the first instance of a substring is replaced by a specified string.")
l("Note that positions input to the functions should start at '1', not '0'.")
l("Note that the functions must handle 'not found' conditions and expect odd cases.\n \
    Return 'None' if request cannot be filled.")
l(">>  Find substring beginning at 24 for a length of 7 in string 'superkalifragilisticexpialidocious'.")
l(">>  Replace 'six' with 'twenty' in 'When I was six years old, I saw a magnificent drawing.'")
presentLesson("Exercise: Using String Methods", ll)

ll = []; l = ll.append
l("Split the following string by commas, so that the resulting list is processed by a 'for' loop.\n\n \
        'mas, bms01, bms02, bms03, bms04, bms05, bms06, pmg'\n\n \
    For each of those servers, print 'This system has a <server> server.'")
presentLesson("Exercise: Split a string and process the list", ll)

ll = []; l = ll.append
l("for serverType in 'mas, bms01, bms02, bms03, bms04, bms05, bms06, pmg'.split(','):")
l("    print 'This system has a ' + serverType.strip() + ' server.'")
execCodeBlock(ll)

sys.exit(0)
