#!/usr/bin/python
import os, sys
from subprocess import *

##  Match this: hda

def execCommand(command, exitOnFail=True, expectedRCList=["0"], logfile=None):
    """
    Executes a linux command, capturing its exit code and output.
    Returns a list of this function's return code, the command's
    stdout, the command's stderr, the command's exit code.
    This function's return code is 1 for success, 0 for failure.

    logfile: file handle for log file. Can be None.
    command: The Linux command to execute.
    exitOnFail: True or False. If True, exits script upon failure. Default is True.
    expectedRCList: list of accepted exit codes that do not mean failure. Default is ["0"].
    """
    stdout = ""
    stderr = ""
    cmdAsList = cmd.split()
    p = Popen(cmdAsList, stdout=PIPE, stderr=PIPE, close_fds=True)
    p.wait()
    for line in p.stdout: stdout += line
    for line in p.stderr: stderr += line
    p.stdout.close(); p.stderr.close()
    stdout = stdout.strip(); stderr = stderr.strip()
    rcode = p.returncode

    print str(stdout)

    if str(rcode) in expectedRCList:
        returnCode = 1
    else:
        message = "Command failed.  " + command + ". RC: " + str(rcode) + ".  STDOUT: '" + str(stdout) + "'.  STDERR: " + str(stderr)
        if logfile:
            writeLine(logfile, "Log file", message)
        if exitOnFail:
            print "ERROR: " + message
            sys.exit(1)
        else:
            print "WARN: " + message
            returnCode = 0
    return [returnCode, stdout, stderr, rcode]

cmd = "grep this ./testSubProcess.py"
(returnCode, stdout, stderr, rcode) = execCommand(cmd)

print "\nSuccess: " + str(returnCode)
print "\nrcode  : " + str(rcode)
print "\nstdout : \n" + str(stdout)
print "\nstderr : \n" + str(stderr)

sys.exit(0)
