import sys, os, re

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
    cmd = command + "; echo $?"
    stdout = ""
    stderr = ""
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

def writeLine(fileObj, filename, line):
    """
    Writes a line to an open file. Exits the script upon failure.
    Returns 1 for success, exits script upon failure.

    fileObj: file handle to be written
    fileName: associated file name, used for message output.
    """
    if fileObj:
        try:
            fileObj.write(line)
        except Exception, e:
            print "ERROR: Failure writing to file, '" + filename + "'. Error: " + str(e)
            sys.exit(1)
    return 1

def lastLine(inString):
    """
    Returns the last non-empty line in the input string.
    """
    outLine = ""
    for line in inString.strip().splitlines():
        if line.strip():
            outLine = line.strip()
    return outLine

def printAndLog(logfile, message):
    writeLine(logfile, "", "\n" + message)
    print message
    return True

def echoCmd(command,logfile):
    writeLine(logfile, "", "\n" + "="*60)
    printAndLog(logfile, "\nexecuting " + command)
    writeLine(logfile, "", "\n" + "="*60)
    writeLine(logfile, "", "\n")

def echoInfo(rpm,action,logfile):
    writeLine(logfile, "", "\n")
    writeLine(logfile, "", "\n" + "="*60)
    printAndLog(logfile, "\n" + action + " " + rpm)
    writeLine(logfile, "", "\n" + "="*60)
    writeLine(logfile, "", "\n")

def execCmd(logfile, command, exitOnFail=True, expectedRCList=["0"]):
    """
    Wraps execCommand function call.
    Determine whether the command contains a password or is an ordinary echo statement,
    or is some other regular type of statement in order to display, or not, the command.
    Then execute execCommand by passing all input parms to it.
    Returns the outcome of execCommand.

    logfile: file handle for log file. Can be None.
    command: The Linux command to execute.
    exitOnFail: True or False. If True, exits script upon failure. Default is True.
    expectedRCList: list of accepted exit codes that do not mean failure. Default is ["0"].
    """
    logCmd = True
    m = re.search('echo \".*?\" \| (?P<trueCmd>.*)', command)
    if m: 
        loggedCmd = "echo <password> | " + m.group('trueCmd')
    elif command.startswith("echo"):
        if re.search("echo\s+\$", command):
            loggedCmd = command
        else:
            logCmd = False
    else:
        loggedCmd = command

    if logCmd:
        print "\n>> " + loggedCmd
        if logfile:
            writeLine(logfile, "Log file", "\n\n>> " + loggedCmd + "\n")
    return execCommand(command, exitOnFail=exitOnFail, expectedRCList=expectedRCList, logfile=logfile)
