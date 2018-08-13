import sys, os, re
import warnings
warnings.simplefilter("ignore", DeprecationWarning)

class Logging:
    logFH = None

    def __init__(self, logfile):
        self.logfile = logfile
        # open log file, set file handle
        self.openFile()

    def __del__(self):
        self.closeFile()
        
    def openFile(self):
        try:
            self.logFH = open(self.logfile, "w")
            print "Opened log file, " + self.logfile
            return True
        except Exception:
            self.logFile = None
            print "Exception opening log file, " + str(self.logfile)
            print "Details:\n" + str(sys.exc_info()[0])
            return False

    def closeFile(self):
        self.logFH.close()

    def writeFile(self, line):
        if self.logFH:
            try:
                self.logFH.write(line)
            except Exception, e:
                print "ERROR: Failure writing to file, '" + self.logfile + "'. Error: " + str(e)
                sys.exit(1)
            return True
        return False

    def printAndLog(self, message):
        print message
        return self.writeFile("\n" + message)


class LinuxCommand:
    logObj = None

    def __init__(self, logObj):
        self.initVars()
        self.logObj = logObj

    def initVars(self):
        self.command    = None
        self.cmd        = None
        self.loggedCmd  = None
        self.exitOnFail = True
        self.logCmd     = None
        self.expectedRCList = [0]
        self.result     = None
        self.stdout     = None
        self.stderr     = None
        self.rcode      = None

    def logCommand(self, line):
        if self.logCmd:
            print "\n>> " + self.loggedCmd
            if self.logObj:
                self.logObj.writeFile(line + "\n")

    def execute(self):
        self.logCommand("\n\n>> " + self.loggedCmd)
        cmd = self.command + "; echo $?"
        self.stdout = ""
        self.stderr = ""
        stdinFile, stdoutFile, stderrFile = os.popen3(cmd)
        for line in stdoutFile: self.stdout += line
        for line in stderrFile: self.stderr += line
        stdinFile.close(); stdoutFile.close(); stderrFile.close()
        self.stdout = self.stdout.strip(); self.stderr = self.stderr.strip()

        # Strip digital exit code from end of stdout
        pos = -1
        while self.stdout[pos].isdigit():
            self.rcode = int(self.stdout[pos:])
            pos = pos - 1
            if abs(pos) > len(self.stdout): break
        if not abs(pos) > len(self.stdout):
            pos = pos + 1
        self.stdout = self.stdout[:pos].strip()
        print str(self.stdout)

        if self.rcode in self.expectedRCList:
            self.result = 1
        else:
            message = "Command failed.  " + self.command + ". RC: " + str(rcode) + ".  STDOUT: '" + str(self.stdout) + "'.  STDERR: " + str(self.stderr)
            if self.exitOnFail:
                self.logObj.printAndLog("ERROR: " + message)
                sys.exit(1)
            else:
                self.logObj.printAndLog("WARN: " + message)
                self.result = 0
        return self.result

    def sudoCmd(self, command, password):
        self.initVars()
        self.logCmd    = True
        self.command   = command
        self.cmd       = 'echo "' + password.strip() + '" | sudo -S ' + command
        self.loggedCmd = "echo <password> | sudo -S " + command
        return self.execute()

    def execCmd(self, command):
        self.initVars()
        self.logCmd    = True
        self.command   = command
        self.cmd       = command
        self.loggedCmd = command
        if command.startswith("echo"):
            if re.search("echo\s+\$", command):
                self.loggedCmd = command
            else:
                self.logCmd = False
        else:
            self.loggedCmd = command
        return self.execute()




