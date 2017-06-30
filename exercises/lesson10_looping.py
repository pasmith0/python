#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Repetition of commands is accomplished through several looping structures.")
l("The 'for <variable(s)> in <list>' construct should be familiar now, as should the 'while <condition>' loop.")
l("       The for loop: \n \
           ------------- \n\n \
              for <variable(s)> in <list or list generator>: \n \
                  sequence \n")
l("       The while loop: \n \
           --------------- \n\n \
              while <condition>: \n \
                  sequence \n")
l("Loops normally end when the for loop runs out of data or the while loop condition fails.")
l("Two special commands also control processing within a loop:\n\n \
          break:      forces the loop to end immediately and continue with the next statement after the loop.\n\n \
          continue:   causes the rest of processing for the current loop iteration to be bypassed. \n \
                      Control passes to the next iteration (if any).")
l("An infinite loop results when infinite data is supplied to a for loop, or when the while condition is never (or can't be) false.")
l("Loops can contain any valid sequence of code, including other (nested) loops.")
presentLesson("Repetition Through Looping", ll, False)

ll = []; l = ll.append
l("a = 4")
l("while a > 0:")
l("    print a")
l("    a -= 1")
execCodeBlock(ll, "A basic while loop")

ll = []; l = ll.append
l("for aaa in ['a', 'b', 'c']:")
l("    print aaa")
execCodeBlock(ll, "A basic for loop")

ll = []; l = ll.append
l('aaa = ""')
l('maxstring = "xxxxxxxxxxxxxxxxxxxxxxxxxx"')
l("while True:")
l('    print "Somebody stop me!!!!!"')
l('    aaa += "x"')
l("")
l("    if aaa == maxstring:")
l("        break")
execCodeBlock(ll, "An infinite while loop with break")   

ll = []; l = ll.append
l('def testCondition(cond):')
l('    # Display a condition as true or false')
l('    condDisplay = "|" + str(cond) + "|"')
l('    if cond: ')
l('        print "   " + condDisplay.ljust(12) + " is True"')
l('    else:')
l('        print "   " + condDisplay.ljust(12) + " is False"')
l('')
l("testList  = [ [], {}, True, 1, '', -1, False, ' ', [''], None, 0, {'a': 'b'} ]")
l('for test in testList:')
l('    testCondition(test)')
execCodeBlock(ll, "Testing True and False Values")   

ll = []; l = ll.append
l('test = 0')
l('while test < 100:')
l('    try:')
l('        test += 1')
l('        if test % 2:')
l('            if test in range(20, 41):')
l('                continue')
l('            if test > 60:')
l('                break')
l('            print "Odd number: " + str(test)')
l('    except:')
l('        pass')
execCodeBlock(ll, "Example with break, continue and pass")

ll = []; l = ll.append
l('lineCount = 0')
l('for line in open("./lesson10_looping.py"):')
l('    lineCount += 1')
l('print "Lines in ./lesson10_looping.py are: " + str(lineCount)')
execCodeBlock(ll, "Loop through lines in a file")
  
ll = []; l = ll.append
l('outerList = [ ["a", "w"], ["b", "x"], ["c", "y"], ["d", "z"] ]')
l('')
l('for charA, charB in outerList:')
l('    print charA + "  " + charB')
execCodeBlock(ll, "Loop through a list of lists, Option 1")

ll = []; l = ll.append
l('outerList = [ ["a", "w"], ["b", "x"], ["c", "y"], ["d", "z"] ]')
l('')
l('for innerList in outerList:')
l('    print innerList[0] + "  " + innerList[1]')
l('    for inner in innerList:')
l('        print inner')
execCodeBlock(ll, "Loop through a list of lists, Option 2")

ll = []; l = ll.append
l('stringList = [ "aaa", "bbb", "ccc", "ddd" ]')
l('')
l('for index, value in enumerate(stringList):')
l('    print str(index) + "  " + str(value)')
execCodeBlock(ll, "Loop through index and values using 'enumerate'")

ll = []; l = ll.append
l('stringList = [ "aaa", "bbb", "ccc", "ddd" ]')
l('')
l('for index, value in zip(range(len(stringList)), stringList):')
l('    print str(index) + "  " + str(value)')
execCodeBlock(ll, "Loop through index and values using 'zip'")

ll = []; l = ll.append
l('stringList = [ "aaa", "bbb", "ccc", "ddd" ]')
l('otherList  = [ "www", "xxx", "yyy", "zzz" ]')
l('')
l('for one, two in zip(stringList, otherList):')
l('    print str(one) + "  " + str(two)')
execCodeBlock(ll, "Interleave two lists using 'zip'")

ll = []; l = ll.append
l('for char in "[mystroMAS] cd /home/mystro/rpms":')
l('    print "Char: " + char + ",  ASCII: " + str(ord(char))')
execCodeBlock(ll, "Loop through characters in a string, print ASCII values")

ll = []; l = ll.append
l(['B1', 'outString = ""'])
l(['B1', 'for char in "xTxxxhxisxx xstxrxxxinxgxx xxhaxdx xxsxxtxxraxxxyx excxkxsxexs":'])
l(['B1', '    if char == "x":'])
l(['B1', '        continue'])
l(['B1', '    outString += char'])
l(['B2', 'if outString:'])
l(['B2', '    print "\\nClean string: \\"" + outString + "\\""'])
execGroups(ll, "Loop through characters in a string, excluding 'x's")

ll = []; l = ll.append
execGroups(ll, "More examples are in example10_looping.py")








