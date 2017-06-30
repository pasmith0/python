#!/usr/bin/python
import os, sys, re
from optparse import OptionParser

def execCommand(command, exitOnFail=True, expectedRCList=["0"]):
    """
    Executes a linux command, capturing its exit code and output.
    Returns a list of this function's return code, the command's
    stdout, the command's stderr, the command's exit code.
    This function's return code is 1 for success, 0 for failure.

    command: The Linux command to execute.
    exitOnFail: True or False. If True, exits script upon failure. Default is True.
    expectedRCList: list of accepted exit codes that do not mean failure. Default is ["0"].
    """
    logCmd = True
    m = re.search('echo \".*?\" \| (?P<trueCmd>.*)', command)
    if m: 
        loggedCmd = "echo <password> | " + m.group('trueCmd')
    elif not command.startswith("echo"):
        loggedCmd = command
    else:
        logCmd = False

    if logCmd:
        print "\n>> " + loggedCmd

    cmd = command + "; echo $?"
    stdout = stderr = ""
    stdinFile, stdoutFile, stderrFile = os.popen3(cmd)
    for line in stdoutFile: stdout += line
    for line in stderrFile: stderr += line
    stdinFile.close(); stdoutFile.close(); stderrFile.close()
    stdout = stdout.strip(); stderr = stderr.strip()

    # Strip digital exit code from end of stdout
    pos = -1
    while stdout[pos].isdigit():
        rcode = int(stdout[pos:])
        pos = pos - 1
        if abs(pos) > len(stdout): break
    if not abs(pos) > len(stdout):
        pos = pos + 1
    stdout = stdout[:pos].strip()
    print str(stdout)

    if str(rcode) in expectedRCList:
        returnCode = 1
    else:
        print "Command failed.  " + loggedCmd + ". RC: " + str(rcode) + ".  STDOUT: '" + str(stdout) + "'.  STDERR: " + str(stderr)
        if exitOnFail:
            print "ERROR: " + message
            sys.exit(1)
        else:
            print "WARN: " + message
            returnCode = 0

    return [returnCode, stdout, stderr, rcode]


parserObj = OptionParser()
# Establish some command line options

parserObj.add_option("--file", dest="fileName", default="debtors.txt", type='string', 
            help="Optional: Name of debtors file. [Default: debtors.txt]")

(options, args) = parserObj.parse_args()
dataFilename = options.fileName

rc = execCommand("test -e " + dataFilename, expectedRCList=["0", "1"])
if int(rc[3]):
    print "File does not exist: " + dataFilename
    sys.exit(1)

# Read in the debtors file
try:
    fh = open(dataFilename, 'r')
    print "Opened file for reading: " + dataFilename + "."
except Exception, e:
    print "Error opening file, " + dataFilename + ", for reading. Error: " + str(e)
    sys.exit(1)

try:
    fh2 = open('aging2011.txt', 'w')
    print "Opened file for writint: aging2011.txt"
except Exception, e:
    print "Error opening file, aging2011.txt. Error: " + str(e)
    sys.exit(1)


for line in fh.readlines():
    m = re.search(",\s+(?P<year>\d{4})\d+$", line)
    if not m:
        print "Bad record: " + line
    elif int(m.group('year')) < 2012:
        if not re.search("\n$", line):
            line = str(line) + "\n"
        fh2.write(line)
        print "Wrote line to file: " + line
    else:
        print "Not writing line: " + line

try:
    fh.close()
except Exception, e:
    print "Error closing file, " + dataFilename + ". Error: " + str(e)

try:
    fh2.close()
except Exception, e:
    print "Error closing file, aging2011.txt, Error: " + str(e)

sys.exit(0)
