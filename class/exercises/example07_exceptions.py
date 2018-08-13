#!/usr/bin/python
import sys


def processInput(inputValue):
    return True

def execStandardEnding():
    return True


# Catch most Python-defined exceptions (covers all built-in, non-system-exiting exceptions)
try:
    if inputValue:
        print "This will never be executed..."
        processInput(inputValue)
    print "This will never be printed..."
except Exception, e:
    print '\nException encountered. Reason: ' + str(e)



try:
    if inputValue:
        processInput(inputValue)
except NameError, reason:
    # If the variable is not defined, continue without it
    print '\nNothing to process. ' + str(reason)
except Exception, reason:
    # Any other exceptions, then exit
    print '\nUnexpected exception encountered. Reason: ' + str(reason)
    execStandardEnding()
except:
    # Any other unnamed exceptions, then exit. Use caution with this!!
    print '\nFallthrough exception encountered: ' + str(sys.exc_info()[0])
    execStandardEnding()



try:
    print "\nThis is a string, but contatenating an integer: " + 10
except TypeError, e:
    print "\nTrapped a familiar error condition: " + str(e)



try:
    print "\nThis is a string, but contatenating an integer: " + 10
except TypeError:
    print "\nIt's not required to capture the reason, but more is better!"



#  Sometimes an exception just means the command gets skipped
#  Note that several exceptions can be tupled on an expect...
try:
    print "\nThis is a string, but contatenating an integer: " + 10
except (RuntimeError, TypeError, NameError):
    pass   # Note: this is a placeholder statement in Python, where a command is required but nothing to do.



# The else clause continues processing when no exception is encountered.
# Using this clause can prevent confusion as to which code produces an exception.
try:
    if inputValue:
        print "Will process value: " + inputValue
except NameError, reason:
    # If the variable is not defined, continue without it
    print '\nNothing to process. ' + str(reason)
except Exception, reason:
    # Any other exceptions, then exit
    print '\nUnexpected exception encountered. Reason: ' + str(reason)
    execStandardEnding()
else:
    processInput(inputValue)



# But how can I make my own exception?
# One way is to use the 'raise' command.
try:
    print "\nNothing really wrong here..."
    raise Exception('spam', 'eggs')
    print "This will never print"
except Exception, inst:
    print type(inst)   # the exception instance
    print inst.args    # arguments stored in .args
    print inst                  
    x, y = inst.args
    print 'x =', x
    print 'y =', y



# The finally clause is always executed after everything else
# Before Python 2.5, finally only worked with nesting.
try:
    try:
        if inputValue:
            print "Will process value: " + inputValue
    except NameError, reason:
        # If the variable is not defined, continue without it
        print '\nNothing to process. ' + str(reason)
finally:
    print "And last but not least...."

# The finally clause is always executed after everything else
# Before Python 2.5, finally only worked with nesting.
print "\nThis woould work in python 2.5+ :"
print "\ntry:"
print "    if inputValue:"
print "        print 'Will process value: ' + inputValue"
print "except NameError, reason:"
print "    print 'Nothing to process. ' + str(reason)"
print "finally:"
print "    print 'And last but not least....'"
print
print
sys.exit(0)

