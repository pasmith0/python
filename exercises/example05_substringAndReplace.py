#!/usr/bin/python
import sys

"""
Python has no 'substring' or 'replace' methods for strings.
Write subroutines of your own:
    'substring' returns characters from a given starting point for a specified number of characters.
    'replace'   returns a string where the first instance of a substring is replaced by a specified string.

Note that positions input to the functions should start at '1', not '0'.

Note that the functions must handle 'not found' conditions and expect odd cases.
Return 'None' if request cannot be filled.

>>  Find substring beginning at 24 for a length of 7 in string 'superkalifragilisticexpialidocious'.

>>  Replace 'six' with 'twenty' in 'When I was six years old, I saw a magnificent drawing.'
"""

def substring(srcString, startPos, length):
    """
    Return the substring within 'srcString' that begins as character 'startPos' for 'length' chars.
    If startPos is too high for the length of srcString, return "".
    If length calls for a substring beyond the bounds of srcString, return all that is possible.

    srcString: the source string of the substring to be returned.
    startPos: the first character for the substring, count starting at 1 for the first char of the string.
    length:   max length of the returned substring. 
    """
    startIndex = startPos - 1
    lastIndex  = startIndex + length
    if startPos > len(srcString):
        return ""
    if lastIndex > len(srcString):
        lastIndex = None
    return srcString[startIndex:lastIndex]

def replaceString(srcString, strTarget, strReplacement, nbrReplacements=1):
    """
    Return a copy of srcString where the first example of 'strTarget' within 'srcString' is replaced by 'strReplacement'.
    If nbrReplacements > 1, then replace additional examples of 'strTarget' up to that count.

    srcString: the source string to be modified.
    strTarget:       the string to be replaced
    strReplacement:  the replacement string 
    nbrReplacements: the number of strTarget examples to be replaced. Default is one.
    """
    startPos = 0
    for count in range(nbrReplacements):
        targetIndex = srcString.find(strTarget, startPos)
        if targetIndex >= 0:
            srcString = srcString[:targetIndex] + strReplacement + srcString[targetIndex + len(strTarget):]
            # Reset start position so that any example of target string within replacement string
            # is not itself replaced. After a replacement, look beyond it for next target.
            startPos = targetIndex + len(strReplacement)
    return srcString

print substring("1234567890", 4, 4)
print substring("1234567890", 4, 5)
print substring("1234567890", 4, 6)
print substring("1234567890", 4, 7)
print substring("1234567890", 4, 8)
print substring("1234567890", 4, 9)
print substring("1234567890", 4, 10)

print " "
print substring("1234567890", 4, 4)
print substring("1234567890", 5, 4)
print substring("1234567890", 6, 4)
print substring("1234567890", 7, 4)
print substring("1234567890", 8, 4)
print substring("1234567890", 9, 4)
print substring("1234567890", 10, 4)
print substring("1234567890", 11, 4)

print " "
print replaceString("1234567890123456789012345678901234567890", "456", "xxx")
print replaceString("1234567890123456789012345678901234567890", "456", "xxx", 1)
print replaceString("1234567890123456789012345678901234567890", "456", "xxx", 2)
print replaceString("1234567890123456789012345678901234567890", "123", "xxx", 3)
print replaceString("1234567890123456789012345678901234567890", "123", "xxx", 4)
print replaceString("1234567890123456789012345678901234567890", "890", "xxx", 4)
print replaceString("1234567890", "0", "xxx")

print " "
print replaceString("1234567890123456789012345678901234567890", "456", "xxx")
print replaceString("1234567890123456789012345678901234567890", "456", "xxx", 1)
print replaceString("1234567890123456789012345678901234567890", "456", "xxx", 2)
print replaceString("1234567890123456789012345678901234567890", "123", "xxx", 3)
print replaceString("1234567890123456789012345678901234567890", "123", "xxx", 4)
print replaceString("1234564564564567890123456789012345678901234567890", "456", "wx456yz", 9)
print replaceString("1234567890", "0", "xxx")

print " "
# Find substring beginning at 24 for a length of 7 in string 'superkalifragilisticexpialidocious'.
print substring('superkalifragilisticexpialidocious', 24, 7)

# Replace 'six' with 'twenty' in 'When I was six years old, I saw a magnificent drawing.'
print replaceString('When I was six years old, I saw a magnificent drawing.', 'six', 'twenty')

sys.exit(0)
