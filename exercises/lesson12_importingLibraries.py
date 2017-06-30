#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("It's useful to bundle libraries of related variables and functions into a single file.\n \
    For instance, all functions for searching strings and matching patterns in strings \n \
    using regular expressions can be put in a library called 're.py'. \n \
    Only when those functions are needed do you incur the overhead of importing the file into your program.")

l("There are many libraries and many library authors, so naturally some will use the same variable and function names. \n \
    How does one function not overwrite another by the same name? \n\n \
    >> Each imported library has it's own namespace. \n\n \
    So, funcA in libraryX.py and funcA in libraryZ.py each have a different namespace, which is the library file's name. \n \
    Note that library files have '.py' extensions, but that extension is omitted in the import statement. \n\n\
         For example: \n\n\
             import libraryX, libraryZ \n\n\
             output = libraryX.funcA() \n\n\
         It wouldn't work without preceding the function with its namespace: \n\n\
             import libraryX, libraryZ \n\n\
             output = funcA() \n\n\
             NameError: name 'funcA' is not defined\n")

l("To import a library into the script's own local namespace requires two things: \n\n \
       A. The knowledge that the function names within the library will not collide with functions from other libraries \n\n \
       B. The alternate version of the import command: \n\n\
             from libraryZ import funcA  \n\n\
             output = funcA() \n\n\
             Now that works just fine.\n")

l("The last example only imported a selected function from libraryZ.py. \n \
    The 'from...import...' version uses globs to determine what is imported. \n \
    To import everything from libraryZ: \n\n\
             from libraryZ import * \n")

l("Libraries also import the libraries they need, so sometimes there is a chain of imports that lead to a script.")

l("But where does import find libraries? The PYTHONPATH environment variable must contain the needed directories.\n\n")

presentLesson("Importing libraries", ll, False)

