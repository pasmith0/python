#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("Python is a high-level programming language, meaning it is not a low-level, machine language.")
l("There are two types of programming languages: interpreted and compiled.")
l("Computers can only execute object code, rather than the source code we produce.")
l("Interpreted languages are converted to object code by an interpreter at run time.")
l("Compiled languages are converted to object code by a compiler just once, \n \
    and the compiled executable can run many times without translation. \n \
    Execution speeds far exceed those of interpreted code.")
l("The ability to change a program and then run it immediately is an advantage of interpreted languages.")
l("Many script languages like Python are something in between.\n \
    They pre-compile source code into byte code, which is then interpreted to object code at run time.\n \
    Python precompiles files that load many standard libraries, so that loading (importing) such files goes quicker, \n \
    but other than that Python is interpreted. You'll see '.pyc' files created for files that you import into programs.")
l("Even though Python and other interpreted languages execute a hundred times slower than C++,\n \
    many programs don't require such speed, and Python takes far less time and fewer lines to program\n \
    saving substantially on development costs.")
presentLesson("What is Python?", ll, False)

ll = []; l = ll.append
l("Official Python is written in 'C++' according to specifications in the PEP documents.\n \
    So-called, CPython, it has the highest compatibility with written standards. \n \
    It's also the best at supporting C extensions to Python.")
l("But there are other Pythonic interpreters. Jython is Python written in Java and executed by the JVM. \n \
    It serves best when Java libraries and execution of Java within Python is desired. \n \
    Its implementation lags CPython by several releases.")
l("IronPython is an implementation of Python for the .NET framework. It can use both Python and .NET framework libraries, \n \
    and can also expose Python code to other languages in the .NET framework.")
l("PyPy aims for maximum compatibility with the reference CPython implementation while improving performance.\n \
    On a suite of benchmarks, it's currently over 5 times faster than CPython through version 2.7.")
l("IPython is a command shell for interactive computing in multiple programming languages, originally developed for the Python programming language, \n \
    that offers enhanced introspection, rich media, additional shell syntax, tab completion, and rich history. \n \
    IPython currently provides the following features: \n\n \
        Powerful interactive shells (terminal and Qt-based).  \n \
        A browser-based notebook with support for code, text, mathematical expressions, inline plots and other rich media. \n \
        Support for interactive data visualization and use of GUI toolkits.  \n \
        Flexible, embeddable interpreters to load into ones own projects.   \n \
        Easy to use, high performance tools for parallel computing.  \n\n \
    The IPython Notebook is a web-based interactive computational environment where you can combine \n \
    code execution, text, mathematics, plots and rich media into a single document.")
presentLesson("Python Projects and Interpreters", ll)

ll = []; l = ll.append
l("Python is executed through the 'python' command in one of three ways.")
l("The Python shell allows you to interact with the interpreter. \n\
        Type 'python' at the command line to enter the Python shell. \n\
        Type 'print \"Hello, world!\"' \n\n \
            ]$ python \n \
            >>> print \"Hello, world!\" \n \
            Hello, world! \n \
            >>>")
l("A script with a '.py' extension can be executed by typing 'python' at the command line followed by the script name. \n\
        Create a file with a name that you choose ('myprog.py') with one line: 'print \"Hello, world!\"' \n\
        Execute: /usr/bin/python <your program> \n\n \
            ]$ /usr/bin/python myprog.py \n \
            Hello, world! \n \
            ]$")
l("To execute as 'python myprog.py', the environment variable PATH must contain the directory containg the Python executable.")
l("A script with a '.py' extension can also be executed without invoking the interpreter through use of the hash-bang line. \n \
    The OS shell recognizes this first line of code and invokes the interpreter: \n\n \
        #!/usr/bin/python \n\n\
        Insert that line as the first line of your program, then execute your program: \n\n \
            ]$ ./myprog.py \n \
            Hello, world! \n \
            ]$")
presentLesson("Executing Python", ll)

ll = []; l = ll.append
l("What goes on in a program?")
l("   >> " + underlineText + "Input and/or Output" + normalText + ":           Command line options\n\
                                          Reading and writing of files\n\
                                          User interaction with the script\n\
                                          Using Standard Input and Output")
l("   >> " + underlineText + "Variable Assignment" + normalText + ":           =")
l("   >> " + underlineText + "Math" + normalText + ":                          +, -, *, /, //, %, **")
l("   >> " + underlineText + "Comparisons" + normalText + ":                   <, >, ==, !=, not, and, or")
l("   >> " + underlineText + "Conditional Execution" + normalText + ":         if-elif-else")
l("   >> " + underlineText + "Containers and their methods" + normalText + ":  strings \n\
                                          lists and tuples \n\
                                          dictionaries \n\
                                          custom-written")
l("   >> " + underlineText + "Repetitive Execution" + normalText + ":          for and while loops")
l("   >> " + underlineText + "Reusable Code" + normalText + ":                 functions and class objects")
l("   >> " + underlineText + "Exception Handling" + normalText + ":            try-except")
l("   >> " + underlineText + "Comments" + normalText + ":                      single-line, multi-line, inline, docstrings")
presentLesson("Major Programming Operations", ll)

ll = []; l = ll.append
l("http://docs.python.org/release/2.3.5/tut/tut.html")
l("http://docs.python.org/2.7/tutorial/index.html")
l("http://docs.python.org/3.3/tutorial")
l("http://interactivepython.org/courselib/static/thinkcspy/toc.html")
l("http://www.tutorialspoint.com/python/python_functions.htm")
presentLesson("Online Tutorials", ll)

ll = []; l = ll.append
l("http://mystropedia.corp.mystrotv.com/display/MBO/Scripting+Best+Practices")
l("www.python.org/dev/peps/pep-0008   (PEP 8 - Style Guide for Python code)  [PEP = Python Enhancement Proposal]")
l("python.net/~goodger/projects/pycon/2007/idiomatic/handout.html")
presentLesson("Scripting Best Practices Guidelines", ll)

ll = []; l = ll.append
l("http://docs.python.org/2/reference/datamodel.html#special-method-names")
presentLesson("Python special functions", ll)

ll = []; l = ll.append
l("http://www.vogella.com/tutorials/Python/article.html\n")
presentLesson("Python Development with PyDev and Eclipse tutorial", ll)

