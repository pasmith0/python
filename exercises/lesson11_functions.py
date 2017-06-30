#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Functions allow for reuse of code.")
l("Python functions behave differently in some ways than those of other languages, \n \
    particularly where it comes to variable referencing and namespaces.")
l("A basic function has a definition: \n\n\
          -- its name  \n\
          -- its argument list in parens \n\
          -- a block of code \n\
          -- multiple possible exits and return values (cleanest to use 'return' statements) \n\n\
          def formatName(first, middle, last):  \n\
              return last + ', ' + first + ' ' + middle  \n\n\
          formattedName = formatName('Rodney', 'Allen', 'Rippy')")

l("\n     All arguments must be supplied when calling a function, or an exception is thrown:\n\n\
          def formatName(first, middle, last):  \n\
              return last + ', ' + first + ' ' + middle  \n\n\
          formattedName = formatName('Rodney', 'Rippy') \n\
          TypeError: formatName() takes exactly 3 arguments (2 given)")

l("\n     All arguments are positional, so the function expects to see them in order.")

l("\n     Default argument values can be defined 'arg=default', in which case \n \
    they do not have to be supplied when calling the function: \n\n\
          def formatName(first, last, middle=''):  \n\
              return last + ', ' + first + ' ' + middle  \n\n\
          formattedName = formatName('Rodney', 'Rippy')")        

l("\n     Default arguments should be at the end of the argument list; otherwise, the position of args will be in doubt. \n \
    A syntax error results when you try to define a function that way: \n\n\
          def formatName(first, middle='', last):  \n\
              return last + ', ' + first + ' ' + middle  \n\n\
          SyntaxError: non-default argument follows default argument") 

l("\n     If the full number of parameters is supplied to the function call, then the argument name is not needed in the call: \n\n\
          def formatName(first, last, middle=''):  \n\
              return last + ', ' + first + ' ' + middle  \n\n\
          formattedName = formatName('Rodney', 'Rippy', 'Allen')")        

l("\n     But if one or more optional parms is skipped, any default used must use it's name: \n\n\
          def formatName(first, last, middle='', salutation=''):  \n\
              return last + ', ' + salutation + ' ' + first + ' ' + middle  \n\n\
          formattedName = formatName('Rodney', 'Rippy', salutation='Mr.')") 

l("\n     To reorder parameters in a function call, all parameters can be referenced by 'name=value', not just those with defaults: \n\n\
          def formatName(first, last, middle='', salutation=''):  \n\
              return last + ', ' + salutation + ' ' + first + ' ' + middle  \n\n\
          formattedName = formatName(salutation='Mr.', last='Stooge', first='Moe') \n\
          formattedName = formatName(salutation='Mr.', last='Stooge', first='Curly') \n\
          formattedName = formatName(salutation='Mr.', last='Stooge', first='Shemp') \n\
          formattedName = formatName(salutation='Mr.', last='Stooge', first='Larry')")        
       
l("\n     A variable number of arguments can be accepted by a function definition. \n \
    Dereference a tuple to define a variable number of arguments: \n\n\
          def funcName(parm1, parm2, parm3='xxx', *parmList): \n\
              print str(parmList)                             \n\n\
          funcName('a', 'b', 'c', 'd', 'e', 'f')              \n\
          ('d', 'e', 'f')")

l("\n     All variables are passed by reference to Python functions, not by value. \n \
    So, arguments with mutable data can be changed by a function, and that change affects the variable passed in:  \n\n\
          def funcName(list1, list2): \n\
              for index in range(len(list1)): \n\
                  list1[index] += 4 \n\n\
          funcName(myList1, myList2)  << myList1 will be changed !!")

l("\n     The 'scope' of variables determines where they can be referenced: \n\n\
          Rule 1: A variable is local where it is defined.  \n\
          Rule 2: A variable is global if it can be referenced outside its local scope.  \n\
          Rule 3: All variables defined within a function are local variables.  \n\
          Rule 4: Defining a variable in a function with the same name as an external variable does not alter the external variable.  \n\
          Rule 5: All variables not local to a function can be used - and altered - within the function.")

l("\n     The scope of any variables defined within a function is local to the function, \n \
    but a variable referenced within a function, but not defined there, can be fulfilled by a variable in the outer scope! \n\n\
          def cookieDough(ingredientList): \n\
              if noTimeToBake:  \n\
                  print 'Skip this recipe!' \n\n\
          noTimeToBake = True \n\
          cookieDough(['apples', 'flour', 'sugar']) \n\n\
          This is very dangerous and not modular! Never rely on globally scoped variables, but be aware of potential bugs.")
presentLesson("Function Basics", ll, False)

ll = []; l = ll.append
l(['B1', 'global total'])
l(['B1', 'total = 25'])
l(['B1', ''])
l(['B1', 'def printTotal():'])
l(['B1', '    print "Total is ", total'])
l(['B1', ''])
l(['B1', 'printTotal()'])
l(['B1', ''])
execGroups(ll, "A function will use an external variable if it exists!!")


ll = []; l = ll.append
l('global total1')
l('total1 = 0  # This is global variable')
l('')
l('def sum( arg1, arg2 ):')
l('    total1 = arg1 + arg2')
l('    print "Inside  the function local  total : ", total1')
l('    return total1')
l('')
l('# Now you can call sum function')
l('sumVal = sum( 10, 20 )')
l('print "Outside the function global total : ", total1')
l('print "Sum is: ", sumVal ')
l('')
execCodeBlock(ll, "Scope of an external variable reused in a function")

ll = []; l = ll.append
l('global total2')
l('total2 = 0  # This is global variable.')
l('')
l('def sum2( arg1, arg2 ):')
l('    myTotal = arg1 + total2')
l('    print "Inside  the function local  total : ", myTotal')
l('    return myTotal')
l('')
l('# Now you can call sum function')
l('sumVal = sum2( 10, 20 )')
l('print "Outside the function global total : ", total2 ')
l('print "Sum is: ", sumVal ')
l('')
execCodeBlock(ll, "External variable is not altered by function")

ll = []; l = ll.append
l('total3 = 0  # This is global variable.')
l('')
l('def sum( arg1, arg2 ):')
l('    # Use global statement to pull global "total" into local scope')
l('    xglobal total3')
l('    total3 = arg1 + arg2')
l('    print "Inside  the function local  total : ", total3')
l('    return total3')
l('')
l('# Now you can call sum function')
l('sumVal = sum( 10, 20 )')
l('print "Outside the function global total : ", total3 ')
l('print "Sum is: ", sumVal ')
l('')
execCodeBlock(ll, "Scope of an external variable made global within a function")

ll = []; l = ll.append
l('def foo(x_list):')
l('    x_list.remove(1)')
l('    x_list[2] = [99] ')   
l('')
l('x = [0,1,2,3]')
l('foo(x)')
l('print str(x)')
l('')
execCodeBlock(ll, "Arguments are passed by reference, so mutable args can change")

ll = []; l = ll.append
l('def bar(x_list):')
l('    x_list = [4, 5, 6]  # This is a new object, not what x_list originally referred to!')
l('')
l('x = [0,1,2,3]')
l('bar(x)')
l('print str(x)')
l('')
execCodeBlock(ll, "Reassigning an argument name creates a new storage location")

ll = []; l = ll.append
l("When a mutable argument is assigned a default value in the definition of a function, it is done just once \n \
    when the function is first interpreted, so altering that value within the function changes it permanently. \n \
    This can cause unexpected behavior for the unaware. \n \
    The lesson is: don't do that.")
presentLesson("Beware of Changing Default Values Within Functions", ll)

ll = []; l = ll.append
l('def aaa(xxx, zzz=[]):')
l('    zzz.append(xxx)')
l('    return zzz')
l('')
l('print aaa("b")')
l('print aaa("c")')
l('print aaa("y", [])')
l('print aaa("z")')
execCodeBlock(ll, "Function reassigns a mutable argument with default value")

























