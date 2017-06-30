#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Programs often need information obtained from the local OS shell, using shell commands. \n \
    Python's facilites for executing system commands has been evolving; \n \
    so, different means exist in Python 2.6 than in Python 2.3.5.")

l("The most basic way to execute a command, os.system(), only returns the command's exit code: \n\n\
        import os            \n\
        cmd = 'ls -l *.txt'  \n\n\
        if os.system(cmd):   \n\
            print 'failed!'  \n\
        else:                \n\
            print 'succeeded' \n\n\
        rc = os.system(cmd)  \n\
        if rc in [...]: ...  \n\n \
    The command output goes to stdout and stderr, so you'd have to open those files to retrieve it.\n\n \
    The command may also be a script or other executable program.")

l("Note that 'os' library has many other useful functions. \n \
    In fact in order to change directories in a Python script, you must use os.chdir(...): \n\n\
        os.chdir('/usr/local/mystro/conf') \n\n \
    A call to os.system('cd /usr/local/mystro/conf') has no effect because it executes in a subshell, not the current shell.")

l("The Python 2.3.5 ways to get the file objects for stdout and stderr, but not the exit code! \n\n\
         os.popen2(cmd[, mode[, bufsize]])   \n\
            Execute cmd as a sub-process and return the file objects (child_stdin, child_stdout). \n\n\
         os.popen3(cmd[, mode[, bufsize]])   \n\
            Execute cmd as a sub-process and return the file objects (child_stdin, child_stdout, child_stderr). \n\n\
         os.popen4(cmd[, mode[, bufsize]])   \n\
            Execute cmd as a sub-process and return the file objects (child_stdin, child_stdout_and_stderr).\n\n\
         Note that commands are executed as a subprocess, so you can't get the exit code after these calls.")

l("An example using os.popen3(): \n\n\
        cmd = 'ls -l *.txt'  \n\
        stdout = \"\"    \n\
        stderr = \"\"    \n\
        stdinFile, stdoutFile, stderrFile = os.popen3(cmd)  \n\
        for line in stdoutFile: stdout += line              \n\
        for line in stderrFile: stderr += line              \n\
        stdinFile.close()          \n\
        stdoutFile.close()         \n\
        stderrFile.close()         \n\
        stdout = stdout.strip()    \n\
        stderr = stderr.strip()")

l("What about the exit code? Fortunately, there's an easier way: the commands library. \n \
    It lumps stderr with stdout, but sometimes that's what you need. \n\n\
        import commands                \n\
        cmd = 'ls -l *.txt'  \n\
        rc, output = commands.getstatusoutput(cmd)  \n\n\
        print 'Return Code: ' + str(rc)             \n\
        for line in output.splitlines():            \n\
            print line                              \n\n\
        Return Code: 0 \n\
        -rw-rw-r--  1 E176912 E176912 181 Feb 28 15:42 debtors.txt   \n\
        -rw-rw-r--  1 E176912 E176912 828 Jan  9 09:09 notes.txt")

presentLesson("Executing System Commands", ll, False)

ll = []; l = ll.append
l("Prior to Python 2.6, it got pretty complicated to actually get the exit code plus separate stdout and stderr. \n \
    Here's how I manage it in a function that works equally well in 2.3.5 and 2.6: \n\n\
        def execCommand(command, exitOnFail=True, expectedRCList=[\"0\"], logfile=None): \n\
            \"\"\" \n\
            Executes a linux command, capturing its exit code and output.  \n\
            Returns a list of this function's return code, the command's   \n\
            stdout, the command's stderr, the command's exit code.         \n\
            This function's return code is 1 for success, 0 for failure.   \n\n\
            logfile: file handle for log file. Can be None.                \n\
            command: The Linux command to execute.                         \n\
            exitOnFail: True or False. If True, exits script upon failure. Default is True. \n\
            expectedRCList: list of accepted exit codes that do not mean failure. Default is [\"0\"]. \n\
            \"\"\" \n\
            cmd = command + \"; echo $?\"     \n\
            stdout = \"\"                       \n\
            stderr = \"\"                       \n\
            stdinFile, stdoutFile, stderrFile = os.popen3(cmd)   \n\
            for line in stdoutFile: stdout += line               \n\
            for line in stderrFile: stderr += line               \n\
            stdinFile.close(); stdoutFile.close(); stderrFile.close()   \n\
            stdout = stdout.strip(); stderr = stderr.strip()     \n\n\
            # Strip digital exit code from end of stdout  \n\
            pos = -1                                 \n\
            while stdout[pos].isdigit():             \n\
                rcode = int(stdout[pos:])            \n\
                pos = pos - 1                        \n\
                if abs(pos) > len(stdout): break     \n\
            if not abs(pos) > len(stdout):           \n\
                pos = pos + 1                        \n\
            stdout = stdout[:pos].strip()            \n\
            print str(stdout)                        \n\n\
            if str(rcode) in expectedRCList:         \n\
                returnCode = 1                       \n\
            else:                                    \n\
                message = \"Command failed.  \" + command + \". RC: \" + str(rcode) + \".  STDOUT: '\" + str(stdout) + \"'.  STDERR: \" + str(stderr)  \n\
                if logfile:                          \n\
                    writeLine(logfile, \"Log file\", message)  \n\
                if exitOnFail:                       \n\
                    print \"ERROR: \" + message      \n\
                    sys.exit(1)                      \n\
                else:                                \n\
                    print \"WARN: \" + message       \n\
                    returnCode = 0                   \n\
            return [returnCode, stdout, stderr, rcode]")

presentLesson("Works for Python 2.3.5 and Python 2.6", ll)

ll = []; l = ll.append
l("Beginning with Python 2.4 and additions in 2.5, 2.6 and 2.7, the move was made to the 'subprocess' module. \n \
    There are a number of functions and optional ways to process using that library, but to execute a command for Python 2.6 \n \
    and get the return code, stdout and stderr, this way is clean: \n\n\
            stdout = \"\"                            \n\
            stderr = \"\"                            \n\
            cmdAsList = cmd.split()     # Expects each 'word' of command as a list element  \n\
            p = Popen(cmdAsList, stdout=PIPE, stderr=PIPE, close_fds=True)   # Opens pipes to stderr and stdout. We just close them after use. \n\
            p.wait()                    # Waits for command to complete, and sets return code  \n\
            for line in p.stdout: stdout += line     \n\
            for line in p.stderr: stderr += line     \n\
            p.stdout.close(); p.stderr.close()       \n\
            stdout = stdout.strip(); stderr = stderr.strip()   \n\
            rcode = p.returncode")

l("See an example of the execCommand function using this Python 2.6 subprocess option: example15_subprocess.py")

presentLesson("Works for Python 2.6", ll)

