#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Whenever an error condition exists that Python cannot handle (either innately or by design),\n \
    Python reports it as an 'exception' and halts execution.")
l("That's fine in some cases, but it's preferred that control remains within the program.")
l("The 'try-except' structure allows programs to manage exceptions internally and keep control.")
l("When an exception is encountered in the 'try' block, control immediately transfers to the 'except' code block.")
l("A basic use looks like this:\n\n\
        try: \n\
            if inputValue: \n\
                processInput(inputValue) \n\
        except Exception, e: \n\
            print 'Exception encountered. Reason: ' + str(e)")
l("Any amount of code can be put within the try statement, including the whole program, if desired. \n \
    try-except blocks can be nested, and at times it's best to re-raise an exception to allow an outer try to catch it.")
l("'Exception' is a defined class of exceptions. If any of that broad class is encountered, control goes to its block.")
l("The reason for the exception gets put in the variable name supplied. It doesn't have to be 'e', but many times 'e' is used.")
l("Another example also shows that multiple 'except' blocks can apply for various specific exceptions:\n\n\
        try: \n\
            if inputValue: \n\
                processInput(inputValue) \n\
        except NameError, reason: \n\
            # If the variable is not defined, continue without it \n\
            print 'Nothing to process. ' + str(reason) \n\
        except Exception, reason: \n\
            # Any other exceptions, then exit gracefully\n\
            print 'Unexpected exception encountered. Reason: ' + str(reason) \n\
            execStandardEnding()")
l("The 'finally' clause adds code that will always be executed - no matter what - before the construct is exited.")
l("'finally' was poorly implemented before Python 2.5, requiring nesting of try-except within try-finally.")
l("Here's an example of 'finally' that will always close a file, even if an exception is not trapped:\n\n\
        myfile = open('test.txt', 'w')        \n\
        try:                                  \n\
            myfile.write('the Answer is: ')   \n\
            myfile.write(42)   # raises TypeError, which will be propagated to caller  \n\
        finally:                              \n\
            myfile.close()     # will be executed before TypeError is propagated")
l("Even if the 'try' or the 'except' clauses return from a function, the 'finally' block will execute first!\n\n\
        myfile = open('test.txt', 'w')        \n\
        try:                                  \n\
            myfile.write('the Answer is: ')   \n\
            myfile.write(42)   # raises TypeError, which will be propagated to caller  \n\
        except:                               \n\
            print 'Some exception happened!'  \n\
            return 0                          \n\
        finally:                              \n\
            myfile.close()     # will be executed before the function returns")
presentLesson("Handling Exceptions", ll, False)

ll = []; l = ll.append
l('# Catch most Python-defined exceptions (covers all built-in, non-system-exiting exceptions)')
l('try:')
l('    if inputValue:')
l('        print "This will never be executed..."')
l('        processInput(inputValue)')
l('    print "This will never be printed..."')
l('except Exception, e:')
l("    print 'Exception encountered. Reason: ' + str(e)")
execCodeBlock(ll, "Basic try-except trapping 'Exception' class")


ll = []; l = ll.append
l('try:')
l('    if inputValue:')
l('        processInput(inputValue)')
l('except NameError, reason:')
l('    # If the variable is not defined, continue without it')
l("    print 'Nothing to process. ' + str(reason)")
l('except Exception, reason:')
l('    # Any other exceptions, then exit')
l("    print 'Unexpected exception encountered. Reason: ' + str(reason)")
l('    execStandardEnding()')
l('except:')
l('    # Any other unnamed exceptions, then exit. Use caution with this!!')
l("    print 'Fallthrough exception encountered: ' + str(sys.exc_info()[0])")
l('    execStandardEnding()')
execCodeBlock(ll, "Multiple 'except's: specific, class, and generic, in a hierarchy")


ll = []; l = ll.append
l('try:')
l('    print "This is a string, but contatenating an integer: " + 10')
l('except TypeError:')
l('    print "It is not required to capture the reason, but more is better!"')
execCodeBlock(ll, "The reason variable does not have to be provided")


ll = []; l = ll.append
l('#  Sometimes an exception just means the command gets skipped')
l('#  Note that several exceptions can be tupled on an expect...')
l('try:')
l('    print "This is a string, but contatenating an integer: " + 10')
l('except (RuntimeError, TypeError, NameError):')
l('    pass   # Note: this is a placeholder statement')
execCodeBlock(ll, "Use of 'pass' to ignore exceptions")


ll = []; l = ll.append
l('# The else clause continues processing when no exception is encountered.')
l('# Using this clause can prevent confusion as to which code produces an exception.')
l('try:')
l('    if inputValue:')
l('        print "Will process value: " + inputValue')
l('except NameError, reason:')
l('    # If the variable is not defined, continue without it')
l('    print "Nothing to process. " + str(reason)')
l('except Exception, reason:')
l('    # Any other exceptions, then exit')
l('    print "Unexpected exception encountered. Reason: " + str(reason)')
l('    execStandardEnding()')
l('else:')
l('    processInput(inputValue)')
execCodeBlock(ll, "The else clause documents continued processing, but is never needed")


ll = []; l = ll.append
l('# But how can I make my own exception?')
l('# One way is to use the "raise" command.')
l('try:')
l('    print "Nothing really wrong here..."')
l('    raise Exception("spam", "eggs")')
l('    print "This will never print"')
l('except Exception, inst:')
l('    print "Type: " + str(type(inst))   # the exception instance')
l('    print "Args: " + str(inst.args)    # arguments stored in .args')
l('    print "inst: " + str(inst)')
l('    x, y = inst.args')
l('    print "x = ", x')
l('    print "y = ", y')
execCodeBlock(ll, "Raising an exception of your own")


ll = []; l = ll.append
execGroups(ll, "Examples are in example07_exceptions.py")




















