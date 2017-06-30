#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Values and the expressions that evaluate to values can be compared to each other.")
l("The main types of comparison: equality, non-equality, truth, falsehood and rank.")
l("Comparison is safest and sanest when the values being compared have the same type,\n \
    but python does allow comparisons of different types.")

l("The operators <, >, ==, >=, <=, and != compare the values of two objects. \n \
    The objects need not have the same type. If both are numbers, they are converted to a common type. \n \
    Otherwise, objects of different types always compare unequal, and are ordered consistently but arbitrarily.")

l("Comparisons evaluate to either 'True' or 'False', which are not strings but are built-in keywords of type 'bool'")

presentLesson("Comparison Operations", ll, False)

ll = []; l = ll.append
l(['1', "print 4 == 5"])
l(['1', "print 4 < 5"])
l(['1', "print 4 > 5"])
l(['1', "print 4 != 5"])

l(['2', "print 4 >= 5"])
l(['2', "print 4 <= 5"])

l(['3', "print 4 == 5.3"])
l(['3', "print 4 < 5.3"])
l(['3', "print 4 > 5.3"])
l(['3', "print 4 != 5.3"])
l(['3', "print 4 >= 5.3"])
l(['3', "print 4 <= 5.3"])

l(['4', "print type(4 < 5)"])
execGroups(ll, "Basic Comparisons")


ll = []; l = ll.append
l(['1', "print 4 == '5'"])
l(['1', "print 4 < '5'"])
l(['1', "print 4 > '5'"])
l(['1', "print 4 != '5'"])
l(['1', "print 4 >= '5'"])
l(['1', "print 4 <= '5'"])

l(['2', "print 5 == '5'"])
l(['2', "print 5 < '5'"])
l(['2', "print 5 > '5'"])

l(['4', "a = 4"])
l(['4', "b = 5"])
l(['4', "print a == b"])
l(['4', "print a < b"])
l(['4', "print a > b"])

l(['5', "a = 4"])
l(['5', "b = 4.0"])
l(['5', "print a == b"])
l(['5', "print a != b"])
l(['5', "print a < b"])
l(['5', "print a > b"])
execGroups(ll, "Basic Comparisons, Mismatched Types")


ll = []; l = ll.append
l(['1', "print 4 == 5 or 3 == 3.0"])
l(['2', "print 4 == 5 and 3 == 3.0"])
l(['3', "print 4 == 4.0 and 3 == 4.0"])
l(['4', "print 3 == 3.0 and 4 == 4.0"])
l(['5', "print 3 == 3.0 and (4 == 5 or 6 == 6.0)"])
execGroups(ll, "Compound Comparisons Using And and Or")


ll = []; l = ll.append
l(['1', 'print "apple" < "banana"'])
l(['1', 'print "apple" < "Apple"'])
l(['1', 'print "apple" < "Banana"'])
l(['2', 'print "apple" < "Ab"'])
l(['2', 'print "apple" < "A"'])
l(['2', 'print "apple" < "a"'])
l(['2', 'print "apple" < "aq"'])
execGroups(ll, "String Comparisons: Lexographical Order")

sys.exit(0)
