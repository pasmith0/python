#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Variables appear to hold values for reuse by the name of the variable.\n \
    In fact Python variables point to values.")
l("Variable assignment, using the '=' sign, creates a storage area to hold a value in memory\n \
    and then creates an alias for that location with the variable name. \n \
    Once no variables point to a storage area, that data is cleaned up.")
l("Assignment allows multiple variables to access the same memory location, so Python aliasing is important to understand.")
l("The type of the variable: string, integer, float, Boolean, etc..., is assigned based on the last value stored.\n \
    So, a variable can be re-typed on the fly by assignment.")
l("Some data types are 'mutable' and can be altered through variables, while others are 'immutable.'")
l("Examples of immutable data are numbers and strings. \n\n \
        >>> a = 5   # <-- This is an inline comment! Integer 5 is stored in memory. Variable 'a' points to it. \n \
        >>> b = 5   # A second integer 5 is stored, and variable 'b' points to it \n \
        >>> c = a   # Variable 'c' points to the same memory location as variable 'a'")
l("    >>> a = 6           # Because integers are immutable, the stored value of 5 cannot be changed. 'a' points to a stored value of 6. \n \
        >>> print a, b, c   # Note that print accepts multiple things to display, separated by commas \n \
        6 5 5               # Notice that 'c' still points to 5, even though 'a' points to a 6 \n \
        >>>")
l("Examples of mutable data are lists and dictionaries and other mutable objects. \n \
    We'll see later on how different the rules can be for variables pointing to the same mutable data.")
presentLesson("Variables", ll, False)

ll = []; l = ll.append
l("A variable name begins with a letter or an underscore.")
l("Variable names can contain both letters and digits (just not the first letter!), and they are case-sensitive.")
l("Spaces make no sense in a variable name and don't work.")
l("Variable naming convention is 'camel case', the first letter is lowercase, and the first letter of subsequent words is uppercase.")
l("Camelcase examples: \n\n \
         myFirstVariable \n\n \
         __moveAllRPMs            << Note abbreviations are usually caps too \n\n \
         numberEmployeesOver40")
l("Remember to use descriptive variable names! So good for documentation of the program. (even if I keep my course examples short...)")
l("Remember to never use a Python keyword as a variable name. \n\n \
         Keywords: \n\n \
           and      as     assert   break     class   continue  \n \
           def      del    elif     else      except  exec      \n \
           finally  for    from     global    if      import    \n \
           in       is     lambda   nonlocal  not     or        \n \
           one      pass   raise    return    try     while     \n \
           with     yield  True     False")
presentLesson("Variable Names", ll)

ll = []; l = ll.append
l(['1', 'a = 4'])
l(['1', 'print a'])
execGroups(ll, "Assign and reuse a variable")

####################

ll = []; l = ll.append
l(['1', "a = 4"])
l(['1', "print '\"a\" has value, ' + str(a) + ', and type: ' + str(type(a))"])
execGroups(ll, "Variable Type Integer")
ll = []; l = ll.append
l(['1', "a = 'Mary had a little lamb...'"])
l(['1', "print '\"a\" has value, ' + str(a) + ', and type: ' + str(type(a))"])
execGroups(ll, "Variable Type String")
ll = []; l = ll.append
l(['1', "a = 4.0"])
l(['1', "print '\"a\" has value, ' + str(a) + ', and type: ' + str(type(a))"])
execGroups(ll, "Variable Type Float")

#####################

ll = []; l = ll.append
l("The 'print' statement can print the output of any type, including objects, like that returned by 'type().'")
l("But strings can only be concatenated (added) to other strings.\n \
    That's why the 'str' built-in function is used to 're-cast' integer and object types in that last print.")
l("Since we'll use the 'print' statement a lot, we can discuss string concatenation before continuing.")
presentLesson("String Concatenation", ll)

ll = []; l = ll.append
l(['1', "a = 4.0"])
l(['1', "print a"])

l(['2', "a = 4.0"])
l(['2', "b = 'My child has a GPA of ' + a"])

l(['3', "a = 4.0"])
l(['3', "b = 'My child has a GPA of ' + str(a)"])
l(['3', "print b"])

l(['4', "a = 4.0"])
l(['4', "print type(a)"])

l(['5', "print '\"a\" has value, '"])

l(['6', "a = 4.0"])
l(['6', "print '\"a\" has value, ' + str(a)"])

l(['7', "a = 4.0"])
l(['7', "print '\"a\" has value, ' + str(a) + ', and type: ' + str(type(a))"])
execGroups(ll, "String Concatenation")

#####################

ll = []; l = ll.append
l("Rather than assigning a number to a variable directly,\n \
    the result of an operation involving numbers can be assigned to a variable.")
presentLesson("Integer Operations", ll)


ll = []; l = ll.append
l(['1', "a = 4 + 5"])
l(['1', "print a"])
l(['1', "b = a + 2"])
l(['1', "print b"])
l(['1', "c = a + b"])
l(['1', "print c"])
execGroups(ll, "Integer Addition")

ll = []; l = ll.append
l(['1', "a = 24 - 5"])
l(['1', "print a"])
l(['1', "b = a - 2"])
l(['1', "print b"])
l(['1', "c = a - b"])
l(['1', "print c"])
l(['1', "d = b - a"])
l(['1', "print d"])
execGroups(ll, "Integer Subtraction")

ll = []; l = ll.append
l(['1', "a = 4 * 5"])
l(['1', "print a"])
l(['1', "b = a * 2"])
l(['1', "print b"])
l(['1', "c = a * b"])
l(['1', "print c"])
execGroups(ll, "Integer Multiplication")

ll = []; l = ll.append
l(['1', "a = 27 / 5"])
l(['1', "print a"])
l(['1', "b = a / 2"])
l(['1', "print b"])
l(['1', "c = b / a"])
l(['1', "print c"])
l(['1', "a = -27 / 5"])
l(['1', "print a"])
l(['1', "b = a / 2"])
l(['1', "print b"])
l(['1', "c = b / a"])
l(['1', "print c"])
execGroups(ll, "Integer Division")

ll = []; l = ll.append
l(['1', "a = 27 // 5"])
l(['1', "print a"])
l(['1', "b = a // 2"])
l(['1', "print b"])
l(['1', "c = b // a"])
l(['1', "print c"])
l(['1', "a = -27 // 5"])
l(['1', "print a"])
l(['1', "b = a // 2"])
l(['1', "print b"])
l(['1', "c = b // a"])
l(['1', "print c"])
execGroups(ll, "Integer Division With Truncation")

ll = []; l = ll.append
l(['1', "a = 25 % 5"])
l(['1', "print a"])
l(['1', "b = 25 % 2"])
l(['1', "print b"])
execGroups(ll, "Integer Modulus (Remainder after division)")

ll = []; l = ll.append
l(['1', "a = 5**5"])
l(['1', "print a"])
l(['1', "b = a**2"])
l(['1', "print b"])
execGroups(ll, "Integer Exponentiation")

ll = []; l = ll.append
l("Floating point numbers have decimals.\n \
    The result of an operation involving type float is always type float.")
presentLesson("Floating Point Operations", ll)

ll = []; l = ll.append
l(['1', "a = 4.0 + 5.7"])
l(['1', "print a"])
l(['1', "b = a + 2"])
l(['1', "print b"])
l(['1', "c = a + b"])
l(['1', "print c"])
execGroups(ll, "Float Addition")

ll = []; l = ll.append
l(['1', "a = 24.0 - 5.4"])
l(['1', "print a"])
l(['1', "b = a - 2"])
l(['1', "print b"])
l(['1', "c = a - b"])
l(['1', "print c"])
l(['1', "d = b - a"])
l(['1', "print d"])
execGroups(ll, "Float Subtraction")

ll = []; l = ll.append
l(['1', "a = 4.0 * 5.3"])
l(['1', "print a"])
l(['1', "b = a * 2"])
l(['1', "print b"])
l(['1', "c = a * b"])
l(['1', "print c"])
execGroups(ll, "Float Multiplication")

ll = []; l = ll.append
l(['1', "a = 25.0 / 5"])
l(['1', "print a"])
l(['1', "b = a / 2"])
l(['1', "print b"])
l(['1', "c = b / a"])
l(['1', "print c"])
execGroups(ll, "Float Division")

ll = []; l = ll.append
l(['1', "a = 25.888 // 5.0"])
l(['1', "print a"])
l(['1', "print type(a)"])
l(['1', "b = a // 2"])
l(['1', "print b"])
l(['1', "c = b // a"])
l(['1', "print c"])
l(['1', "a = -25.888 // 5.0"])
l(['1', "print a"])
l(['1', "b = a // 2"])
l(['1', "print b"])
l(['1', "c = b // a"])
l(['1', "print c"])
execGroups(ll, "Float Division As Integer Division")

ll = []; l = ll.append
l(['1', "a = 5.4**5"])
l(['1', "print a"])
l(['1', "b = a**2"])
l(['1', "print b"])
l(['1', "c = a**0.5"])
l(['1', "print c"])
l(['1', "d = 12**0.5"])
l(['1', "print d"])
execGroups(ll, "Float Exponentiation")

ll = []; l = ll.append
l("Variables can be re-cast to another type, but the results are only as useful as the starting values!")
presentLesson("Recasting Variable Types", ll)

ll = []; l = ll.append
l(['1', "a = 4"])
l(['1', "b = float(a)"])
l(['1', "print '\"b\" has value, ' + str(b) + ', and type: ' + str(type(b))"])
execGroups(ll, "Recast Integer to a Float")

ll = []; l = ll.append
l(['1', "a = 4.7"])
l(['1', "b = int(a)"])
l(['1', "print '\"b\" has value, ' + str(b) + ', and type: ' + str(type(b))"])
execGroups(ll, "Recast Float to an Integer")

ll = []; l = ll.append
l(['1', "a = 4.7"])
l(['1', "b = str(a)"])
l(['1', "print '\"b\" has value, ' + b + ', and type: ' + str(type(b))"])
execGroups(ll, "Recast Float to a String")

ll = []; l = ll.append
l(['1', "a = 5"])
l(['1', "b = str(a)"])
l(['1', "print '\"b\" has value, ' + b + ', and type: ' + str(type(b))"])
execGroups(ll, "Recast Integer to a String")

ll = []; l = ll.append
l(['1', "a = '4.7'"])
l(['1', "b = float(a)"])
l(['1', "print '\"b\" has value, ' + str(b) + ', and type: ' + str(type(b))"])
execGroups(ll, "Recast String to a Float: string is a float")

ll = []; l = ll.append
l(['1', "a = '12'"])
l(['1', "b = float(a)"])
l(['1', "print '\"b\" has value, ' + str(b) + ', and type: ' + str(type(b))"])
execGroups(ll, "Recast String to a Float: string is an integer")

ll = []; l = ll.append
l(['1', "a = 'foo'"])
l(['1', "b = float(a)"])
l(['1', "print '\"b\" has value, ' + str(b) + ', and type: ' + str(type(b))"])
execGroups(ll, "Recast String to a Float: string is not a number")

ll = []; l = ll.append
l(['1', "a = '4.7';  b = int(a)"])
l(['1', "print '\"b\" has value, ' + str(b) + ', and type: ' + str(type(b))"])
execGroups(ll, "Recast String to an Integer: string is a float")

ll = []; l = ll.append
l(['1', "a = '12'"])
l(['1', "b = int(a)"])
l(['1', "print '\"b\" has value, ' + str(b) + ', and type: ' + str(type(b))"])
execGroups(ll, "Recast String to an Integer: string is an integer")

ll = []; l = ll.append
l(['1', "a = 'foo'"])
l(['1', "b = int(a)"])
l(['1', "print '\"b\" has value, ' + str(b) + ', and type: ' + str(type(b))"])
execGroups(ll, "Recast String to an Integer: string is not a number")

ll = []; l = ll.append
l("Store the value of pi in a variable.\n \
    Store the value of 6 for a radius in another variable.\n \
    Calculate and print the area of a circle using those two variables.\n \
    Report the area this way: 'The area of the circle is ...'")
l("Cast the area as an integer and print that out.")
presentLesson("Exercise: Using Variables", ll)

ll = []; l = ll.append
l(['1', "pi = 3.14"])
l(['1', "radius  = 6"])
l(['1', "areaCircle = pi * radius**2"])
l(['1', "print 'The area of the circle is ' + str(areaCircle) + '\\n\\n'"])
l(['1', "print 'The integer area of the circle is ' + str(int(areaCircle)) + '\\n\\n'  #  Note the nesting of functions!"])
execGroups(ll, "Example: Completed Exercise")

sys.exit()
