#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Comparisons evaluate to True or False, and expressions that are either comparisons\n \
    or other expressions that evaluate to True or False can be used as conditions in an 'if' statement.")
l("To recap: False; None; 0; and empty strings, lists and hashes all evaluate to False; while anything else is True.")
l("Compound conditions rely on the syntactic conjunctions: 'and' and 'or'.")
l("'if a:' is a value conditional test. If the variable 'a' evaluates to True, then the block under the 'if' is executed.")
l("'if someFunction(a):' is a value conditional test. If someFunction returns a value that evaluates to True, then the block under the 'if' is executed.")
l("'if <exp a> and <exp b>:' If the expressions 'a' and 'b' both evaluate to True, then the block under the 'if' is executed.")
l("'if <exp a> or  <exp b>:' If either expression 'a' or 'b' evaluates to True, then the block under the 'if' is executed.")
presentLesson("Conditional Processing", ll, False)

ll = []; l = ll.append
l("a = 4")
l("if a:")
l("    print 'a is True'")
execCodeBlock(ll, "Most basic if statement")

ll = []; l = ll.append
l("a = 0")
l("if a:")
l("    print 'a is True'")
l("else:")
l("    print 'a is False'")
execCodeBlock(ll, "Most basic if-else statement")

ll = []; l = ll.append
l("a = 0")
l("if a > 10:")
l("    print 'a > 10'")
l("elif a > 5:")
l("    print 'a > 5 and <= 10'")
l("elif a > 2:")
l("    print 'a > 2 and <= 5'")
l("else:")
l("    print 'a <= 2'")
execCodeBlock(ll, "A Basic Case Structure, using elif")

ll = []; l = ll.append
l(["B1", "a = 20"])
l(["B1", "b = 30"])
l(["B1", "if  a == 20 and b < 45:"])
l(["B1", '    print "Condition met"'])
l(["B1", "else:"])
l(["B1", '    print "no dice!"'])
l(["B2", "if  ( a == 20 and b < 45 ):"])
l(["B2", '    print "Condition met"'])
l(["B2", "else:"])
l(["B2", '    print "no dice!"'])
l(["B3", "if  (a == 20) and (b < 45):"])
l(["B3", '    print "Condition met"'])
l(["B3", "else:"])
l(["B3", '    print "no dice!"'])
l(["B4", "if  ( (a == 20) and (b < 45) ):"])
l(["B4", '    print "Condition met"'])
l(["B4", "else:"])
l(["B4", '    print "no dice!"'])
execGroups(ll, "Compound Conditions and Grouping with Parens")

ll = []; l = ll.append
l(["B1", "a = 20"])
l(["B1", "b = 30"])
l(["B1", "if  a == 20  \\"])
l(["B1", "and b < 45:"])
l(["B1", '    print "Condition met"'])
l(["B1", "else:"])
l(["B1", '    print "no dice!"'])
execGroups(ll, "Continuation Makes Compound Conditions More Readable")

ll = []; l = ll.append
l(["B1", "a = 20"])
l(["B1", "b = 30"])
l(["B1", "if  (   a == 20  \\"])
l(["B1", "    and b <  45  \\"])
l(["B1", "    ):"])
l(["B1", '    print "Condition met"'])
l(["B1", "else:"])
l(["B1", '    print "no dice!"'])
execGroups(ll, "Use of Parens With Continuation")

ll = []; l = ll.append
l(["B1", "a = 20"])
l(["B1", "b = 30"])
l(["B1", "if  (   (   a == 20  \\"])
l(["B1", "        and b <  45  \\"])
l(["B1", "        )            \\"])
l(["B1", "    or  (   a == 25  \\"])
l(["B1", "        and b >  45  \\"])
l(["B1", "        )            \\"])
l(["B1", "    ):"])
l(["B1", '    print "Condition met"'])
l(["B1", "else:"])
l(["B1", '    print "no dice!"'])
execGroups(ll, "Use of Parens Really Matters for Complex Logic")

ll = []; l = ll.append
l(["B1", "a = 4"])
l(["B1", "default = 10"])
l(["B1", "c = a or default"])
l(["B1", 'print "c ends up: " + str(c)'])
l(["B2", "a = 0"])
l(["B2", "c = a or default"])
l(["B2", 'print "c ends up: " + str(c)'])
execGroups(ll, "As Soon as a Condition is True, Processing Stops")

ll = []; l = ll.append
l(["B1", "a = 4"])
l(["B1", "b = 10"])
l(["B1", "c = ((a < b) and a ) or b"])
l(["B1", 'print "c ends up: " + str(c)'])
l(["B2", "a = 10"])
l(["B2", "b = 5"])
l(["B2", "c = ((a < b) and a ) or b"])
l(["B2", 'print "c ends up: " + str(c)'])
execGroups(ll, "Example: A Way to Pick the Lesser Value")

ll = []; l = ll.append
l(["1", "# What if you accidentally compare a number to a string?"])
l(["2", "# One answer is to force an exception when both values are not numbers."])
l(["B4", "a = 6"])
l(["B4", "b = '4'"])
l(["B4", "if a < b:"])
l(["B4", "    print '6 is less than 4'"])
l(["B4", "else:"])
l(["B4", "    print '6 is not less than 4'"])
l(["B5", "a = 6"])
l(["B5", "b = '4'"])
l(["B5", "if ((a - b) < 0):"])
l(["B5", "    print '6 is less than 4'"])
l(["B5", "else:"])
l(["B5", "    print '6 is not less than 4'"])
execGroups(ll, "Accidental comparison of number to string")

ll = []; l = ll.append
l(["B6", ''])
l(["B6", "a = 6"])
l(["B6", "b = 4"])
l(["B6", "if ((a - b) < 0):"])
l(["B6", "    print '6 is less than 4'"])
l(["B6", "else:"])
l(["B6", "    print '6 is not less than 4'"])
execGroups(ll)

ll = []; l = ll.append
l(["B4", "a = 6"])
l(["B4", "b = '4'"])
l(["B4", "if a < b:"])
l(["B4", "    print 'a is less than b'"])
l(["B4", "    if a < 10:"])
l(["B4", "        print 'a is less than 10'"])
l(["B4", "else:"])
l(["B4", "    print 'a is not less than b'"])
execGroups(ll, "Nested if statements")

ll = []; l = ll.append
execGroups(ll, "More examples are in example08_conditional.py")

