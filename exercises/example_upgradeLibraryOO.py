#!/usr/bin/python
from upgradeLibraryOO import *

logObj = Logging('ccc')
lc     = LinuxCommand(logObj)

if lc.execCmd("ls -l"):
    print "success"
else:
    print "failure"

for y in str(lc.stdout).splitlines():
    print y
sys.exit(0)
