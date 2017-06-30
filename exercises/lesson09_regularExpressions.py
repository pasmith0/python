#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Just as linux/unix globs allow for pattern matching, Python code uses regular expressions to test strings.")
l("Like many languages, Python incorporates the ever-popular Perl regular expressions.\n \
    which are powerful at matching patterns and extracting data.")
l("A regular expression can be quite simple or exhaustively cryptic, depending on the need, \n \
    and usually one or more of these special matching characters is used in the pattern:\n\n \
    Perl regular expressions, Basic usage \n \
    ------------------------------------- \n\n\
     Uses characters with specific meanings to produce search patterns \n\n\
     ^   -- beginning of line \n\
     $   -- end of line \n\
     .   -- any character except the newline character \n\
     \s  -- whitespace character \n\
     \S  -- non-whitespace character  \n\
     \w  -- word character \n\
     \W  -- non-word character \n\
     \d  -- digit \n\
     \D  -- non-digit \n\
     \\n  -- newline character \n\
     \\t  -- tab \n\
     \\r  -- carriage return \n\
     \\\\  -- backslash character itself \n\n\
     [...]        -- custom collection  [TMH]    matches 'T', 'M', or 'H' \n\
     [-0-9]       -- same as \d \n\
     [A-Za-z0-9_] -- same as \w \n\
     [ \\n\\t\\r]    -- same as \s \n\
     [^0-9]       -- non-digit, same as \D \n\n\
     |     -- separates alternatives    (Mr|Mrs) matches either 'Mr' or 'Mrs' \n\n\
     *     -- 0 or more characters      \s*      matches 0 or more white space chars \n\
     +     -- 1 or more characters      \w+      matches 1 or more word chars \n\
     ?     -- 0 or 1 characters         \d?      matches 0 or 1 digits \n\
     {m}   -- exactly 'm' characters    \W{3}    matches 3 non-word chars \n\
     {m,n} -- from 'm' to 'n' chars     x{3,6}   matches 3 to 6 x's \n\
     *?    -- greedy vs. nongreedy      .*?      matches any number of any character, but not greedy")
presentLesson("Regular Expressions", ll, False)

ll = []; l = ll.append
l(["1", "aString = 'lesson09_regularExpressions.py'"])
l(["1", "result = re.search('regular', aString)"])
l(["1", "print 'Result is an object: ' + str(result)"])
execGroups(ll, "A basic regexp match")

ll = []; l = ll.append
l(["1", "aString = 'lesson09_regularExpressions.py'"])
l(["1", "result = re.search('goose', aString)"])
l(["1", "print 'Result is NOT an object: ' + str(result)"])
execGroups(ll, "A basic regexp non-match")

ll = []; l = ll.append
l(["B2", "aString = 'lesson09_regularExpressions.py'"])
l(["B2", "if re.search('regular', aString):"])
l(["B2", "    print 'Found \"regular\" in ' + aString"])
execGroups(ll, "Use of regexp in if statement, matching")

ll = []; l = ll.append
l(["B2", "aString = 'lesson09_regularExpressions.py'"])
l(["B2", "if not re.search('goose', aString):"])
l(["B2", "    print 'No \"goose\" in ' + aString"])
execGroups(ll, "Use of regexp in if statement, non-matching")

ll = []; l = ll.append
l(["1", "aString = 'lesson09_regularExpressions.py'"])
l(["1", "print 'Result: ' + str(re.search('\d+', aString))"])
execGroups(ll, "One or more digits")

ll = []; l = ll.append
l(["1", "aString = 'lesson09_regularExpressions.py'"])
l(["1", "print 'Result: ' + str(re.search('^l', aString))"])
execGroups(ll, "'l' at front of string")

ll = []; l = ll.append
l(["1", "aString = 'lesson09_regularExpressions.py'"])
l(["1", "print 'Result: ' + str(re.search('^l.*?y$', aString))"])
execGroups(ll, "'l' at front of string, and 'y' at end, non-greedy")

ll = []; l = ll.append
l(["1", "aString = 'lesson09_regularExpressions.py'"])
l(["1", "print 'Result: ' + str(re.search('^l.*z$', aString))"])
execGroups(ll, "'l' at front of string, and 'z' at end, greedy")

ll = []; l = ll.append
l(["1", "aString = 'lesson09_regularExpressions.py'"])
l(["1", "print 'Result: ' + str(re.search('^l.*y$', aString))"])
execGroups(ll, "'l' at front of string, and 'y' at end, greedy is okay")

ll = []; l = ll.append
l(["1", "aString = 'lesson09_regularExpressions.py'"])
l(["1", "print 'Result: ' + str(re.search('.*ss', aString))"])
execGroups(ll, "Match all up to 'ss', greedy")

ll = []; l = ll.append
l(["1", "aString = 'lesson09_regularExpressions.py'"])
l(["1", "print 'Result: ' + str(re.search('.*?ss', aString))"])
execGroups(ll, "Match all up to 'ss', non-greedy")

ll = []; l = ll.append
l(["1", "aString = 'lesson09_regularExpressions.py'"])
l(["1", "m = re.search('(?P<ss>.*ss)', aString)"])
l(["1", "print m.group('ss')"])
l(["1", "print m.start('ss')"])
l(["1", "print m.end('ss')"])
execGroups(ll, "Match all up to 'ss', greedy")

ll = []; l = ll.append
l(["1", "aString = 'lesson09_regularExpressions.py'"])
l(["1", "m = re.search('(?P<ss>.*?ss)', aString)"])
l(["1", "print m.group('ss')"])
l(["1", "print m.start('ss')"])
l(["1", "print m.end('ss')"])
execGroups(ll, "Match all up to 'ss', non-greedy")

ll = []; l = ll.append
l(["B2", "aString = '10.254.0.152   fkamts'"])
l(["B2", "m = re.search('(?P<ip>\d+\.\d+\.\d+\.\d+)', aString)"])
l(["B2", "if m:"])
l(["B2", "    print m.group('ip')"])
l(["B2", "    print m.start('ip')"])
l(["B2", "    print m.end('ip')"])
execGroups(ll, "Parse IP address from /etc/hosts entry")

ll = []; l = ll.append
l(["B2", "aString = ' ## 10.254.0.152   fkamts'"])
l(["B2", "if re.search('^\s*#+', aString):"])
l(["B2", "    print 'It is a comment!'"])
execGroups(ll, "Identify a comment line")

ll = []; l = ll.append
l(["B2", "aString = \"Today's date: 2011 02 20\""])
l(["B2", "if re.search('201[34]', aString):"])
l(["B2", "    print 'It is a match!'"])
execGroups(ll, "Match the last two years")

ll = []; l = ll.append
l(["B2", "aString = \"Today's date: 2011 02 20\""])
l(["B2", "if not re.search('201[34]', aString):"])
l(["B2", "    print 'It is not a match!'"])
execGroups(ll, "Match the last two years")

ll = []; l = ll.append
l(["B2", "aString = 'Student: Valerie,  Grade: D,  Activities: Drugs Videogames'"])
l(["B2", "if not re.search('Grade: [^CDEF],', aString):"])
l(["B2", "    print 'It is not a high-performing student!'"])
execGroups(ll, "Exclude grades that are not A or B")

ll = []; l = ll.append
l(["B2", "rpm = 'TWC-Coredn-13.4.4-20140220090511-RAC-DB.noarch.rpm'"])
l(["B2", "if re.search('TWC-Coredn-[.0-9]+-20\d+-RAC-DB.noarch.rpm', rpm):"])
l(["B2", "    print 'It is a match!'"])
execGroups(ll, "Match an rpm with a generic version and timestamp")

ll = []; l = ll.append
l(["B2", "rpm = 'TWC-Coredn-13.4.4-20140220090511-RAC-DB.noarch.rpm'"])
l(["B2", "if re.search('TWC-Coredn-[.0-9]+-20\d{12}-(RAC-DB|DB-RAC).noarch.rpm', rpm):"])
l(["B2", "    print 'It is a match!'"])
execGroups(ll, "Match old and new formats of an rpm name")

ll = []; l = ll.append
l(["B2", "rpm = 'TWC-Coredn-13.4.4-20140220090511-DB-RAC.noarch.rpm'"])
l(["B2", "if re.search('TWC-Coredn-[.0-9]+-20\d{12}-(RAC-DB|DB-RAC).noarch.rpm', rpm):"])
l(["B2", "    print 'It is a match!'"])
execGroups(ll, "Match old and new formats of an rpm name, alt")

ll = []; l = ll.append
l("Which of these regular expressions will match this line from /etc/hosts? \n \
    If it doesn't match, then what will fix it to match? \n\n \
    line = '# 10.254.0.152    mystrotoolsserver fkamts' \n\n \
    A.  \"\s*#+\s+[.0-9]+\s+mystrotoolsserver$\"  \n\n \
    B.  \"# \d+\.\d+\.\d+\.\d+.*?\s+fkamts$\"  \n\n \
    C.  \"\s#+\s+[.0-9]+\s+.*fkamts$\"  \n\n \
    D.  \"^\s*#+\s+\d+\.\d+\.\d+\.\d+\smystrotoolsserver\sfkamts$\"  \n\n \
    E.  \"^\S+\s+\d+\s+\S+\s+\w+$\"  \n\n \
    E.  All of the above  \n\n \
    F.  None of the above")
presentLesson("Exercise: Which will match?", ll)


