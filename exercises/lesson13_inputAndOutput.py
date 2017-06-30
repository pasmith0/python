#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Several basic ways exist to get data to and from a script: \n\n\
        Data into a program: \n\
            1. Command line options \n\
            2. File input \n\
            3. Standard input \n\
            4. Interaction with a user \n\
        Data from a program: \n\
            1. File output \n\
            2. Standard output \n\
            3. Interaction with a user")
presentLesson("Script Input and Output", ll, False)

ll = []; l = ll.append
l("'sys.argv' is a list of individual words that comprise the command line. \n\n \
    For example: \n\n\
         >> myProg.py aaa bbb ccc \n\n\
         Internal to myProg.py, sys.argv can be accessed: \n\n\
             import sys            \n\
             for index, arg in enumerate(sys.argv): \n\
                 print str(index) + ': ' + arg  \n\n\
             which prints: \n\
                 0: myProg.py \n\
                 1: aaa \n\
                 2: bbb \n\
                 3: ccc")

l("Several libraries use sys.argv to enforce formatting of command line options. \n \
    Previous lessons have incorporated examples that use the 'optparse.py' library: \n\n\
        # import OptionParser class         \n\
        from optparse import OptionParser      \n\n\
        # Create an instance of the parser     \n\
        parserObj = OptionParser()             \n\n\
        # Define a command line option         \n\
        parserObj.add_option(\"--start\", dest=\"someVar\", type='int', default=1,       \n\
                    help=\"Optional. The first step the script will execute. Prior steps will be skipped. [Default: 1]\")      \n\n\
        parserObj.add_option(\"-c\", dest=\"cSwitch\", default=False, action=\"store_true\", \n\
                    help=\"Optional. Use to be prompted for other option choices. [Default: False]\") \n\n\
        # Parse the command line      \n\
        (options, args) = parserObj.parse_args()      \n\n\
        'options.someVar' will hold either the default value or the user value. \n\
        'options.cSwitch' will either be True or False")
presentLesson("Command line options", ll)

ll = []; l = ll.append
l("File input and output--reading and writing to files--is similar to other languages: \n\n\
        1. A file must be opened. Once opened, the file handle is an object. \n\
        2. Files are opened for \n\
               'read'   -- access the file contents \n\
               'write'  -- wipe out the file and create new contents \n\
               'append' -- add lines to the existing file contents \n\
               or some combination. \n\
        3. Files opened for reading can be read a line at a time or all at once. \n\
        4. Files are written a line at a time.  \n\
        5. Files should be closed when operations on them complete, \n\
           though the language and/or the OS does handle it when the script completes.")

l("\n     File Access Modes  \n\n\
            Mode     Meaning      Format    Description \n\
            ----     -------      ------    -----------\n\
            r        read only    text      From beginning of the file. This is the default mode. \n\
            rb       read only    binary    From beginning of the file. This is the default mode. \n\
            r+       read/write   text      From beginning of the file.  \n\
            rb+      read/write   binary    From beginning of the file.  \n\
            w        write only   text      Overwrites the file, if it exists, else creates a new file for writing. \n\
            wb       write only   binary    Overwrites the file, if it exists, else creates a new file for writing. \n\
            w+       write/read   text      Overwrites the existing file, if it exists, else creates a new file for reading and writing. \n\
            wb+      write/read   binary    Overwrites the existing file, if it exists, else creates a new file for reading and writing. \n\
            a        append       text      Appends to the end of the file, if it exists, else it creates a new file for writing. \n\
            ab       append,      binary    Appends to the end of the file, if it exists, else it creates a new file for writing. \n\
            a+       append/read  text      Appends to the end of the file, if it exists, else it creates a new file for reading and writing. \n\
            ab+      append/read  binary    Appends to the end of the file, if it exists, else it creates a new file for reading and writing.")

l("File read example: \n\n\
        oldMASVersionFile = \"/home/mystro/upgrade/oldMASVersion.txt\" \n\
        try: \n\
            oldVerFileObj = open(oldMASVersionFile,'r') \n\
        except Exception, e: \n\
            print \"ERROR: Failure opening file '\" + oldMASVersionFile + \"'. Error: \" + str(e)  \n\
            sys.exit(1) \n\n\
        try:  \n\
            oldVersion = oldVerFileObj.readline() \n\
        except Exception, e:  \n\
            print \"ERROR: Failure reading file, '\" + filename + \"'. Error: \" + str(e) \n\
            sys.exit(1) \n\n\
        try:  \n\
            oldVerFileObj.close()  \n\
        except Exception, e:  \n\
            print \"WARN: Failure closing file '\" + oldMASVersionFile + \"'. Error: \" + str(e) \n\
            pass")

l("File write example: \n\n\
        logfilename = \"/home/mystro/upgrade/logs/log_TWCRpmUpgrade-rpms-\" + now + \".txt\" \n\
        try:  \n\
            logObj = open(logfilename,'w')  \n\
        except Exception, e: \n\
            print \"ERROR: Failure opening file '\" + logfilename + \"'. Error: \" + str(e)  \n\
            sys.exit(1)  \n\n\
        try:  \n\
            logObj.write(line)  \n\
        except Exception, e:  \n\
            print \"ERROR: Failure writing to file, '\" + logfilename + \"'. Error: \" + str(e)   \n\
            sys.exit(1)  \n\n\
        try:  \n\
            logObj.close()  \n\
        except Exception, e:  \n\
            print \"WARN: Failure closing file '\" + logfilename + \"'. Error: \" + str(e) + \". Continuing...\"   \n\
            pass")
presentLesson("File input and output (I/O)", ll)

ll = []; l = ll.append
l("Standard Input (stdin) is best accessed as a file:  \n\n\
         >> cat notes.txt | myProg.py aaa bbb ccc \n\n\
         Internal to myProg.py: \n\n\
         import sys \n\
         for index, arg in enumerate(sys.argv): \n\
             print str(index) + \": \" + arg  \n\n\
         data = sys.stdin.readlines() \n\
         print \"Counted\", len(data), \"lines.\"  \n\
         which prints: \n\
             0: myProg.py \n\
             1: aaa \n\
             2: bbb \n\
             3: ccc \n\
             Counted 27 lines.")

l("Note that this example read the entire contents of stdin ('readlines'). \n \
    Also note that stdin did not have to be opened or closed explicitly.")

l("Writing to Standard Output (stdout) should be familiar by now. 'print' does this. \n \
    This code will echo stdin to stdout a line at a time: \n\n\
        import sys \n\
        line = sys.stdin.readline()  \n\
        # Continues until EOF, which is an empty string  \n\
        while line:  \n\
            print line,                    # Thru 2.7, the comma continues the print on the same line to avoid double newlines \n\
            line = sys.stdin.readline()")
presentLesson("Standard Input (stdin) and Output (stdout)", ll)

ll = []; l = ll.append
l("Interactive programs seek keyboard input from a user and can use that data to carry on the interaction or simply process the data.")
l("Python has a built-in function, 'raw_input' to form the basis of complicated routines that prompt users and validate input: \n\n\
        userResponse = raw_input(\"   Enter response: \") \n\
        print \"You can't mean that gorillas eat \" + userResponse + \"!!\" \n\n\
        >>   Enter response: ponies \n\
        You can't mean that gorillas eat ponies!!!")

presentLesson("Interaction with a user", ll)

ll = []; l = ll.append
presentLesson("More examples: \n\n\
    example13_commandLine.py \n\
    example13_fileIO.py \n\
    example13_standardInput.py \n\
    example13_userInteraction.py", ll)


