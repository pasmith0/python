#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("All programming amounts to tayloring code to accomplish alogrithms.")
l("And code appears in 'blocks' of essentially three types: Sequences, Selections and Repetitive Loops.")
l("A fourth, derivative block, is the subroutine.")
presentLesson("The Four Code Blocks of Programming", ll, False)

ll = []; l = ll.append
l("A sequence block is a series of commands issued in order to accomplish some task.")
l("Sequence Example:\n\n\
        # Add up donations  \n\
        donation1 = 12.50   \n\
        donation2 = 45.00   \n\
        donation3 = 15.00   \n\
        donation4 = 38.64   \n\n\
        totalDonations = donation1 + donation2 + donation3 + donation4  \n\
        print 'Total donations: ' + str(totalDonations) \n\n\
   Output: \n\n\
   Total donations: 111.14")
presentLesson("Sequence Blocks", ll)

ll = []; l = ll.append
l("A Selection block uses comparisons and/or conditional evaluations to determine which sequences to execute.")
l("Selection Example:\n\n\
        # Print donations larger than $20  \n\
        donation1 = 12.50   \n\
        donation2 = 45.00   \n\
        donation3 = 15.00   \n\
        donation4 = 38.64   \n\n\
        # Initialize total  \n\
        totalDonationsOver20 = 0 \n\
        if donation1 > 20:  \n\
            print 'Another donation over $20!' \n\
            totalDonationsOver20 += donation1    # also '-=' '*=' '/=' '**=', ... \n\
        if donation2 > 20:  \n\
            print 'Another donation over $20!' \n\
            totalDonationsOver20 += donation2  \n\
        if donation3 > 20:  \n\
            print 'Another donation over $20!' \n\
            totalDonationsOver20 += donation3  \n\
        if donation4 > 20:  \n\
            print 'Another donation over $20!' \n\
            totalDonationsOver20 += donation4  \n\n\
        print 'Total donations over $20: ' + str(totalDonationsOver20) \n\n\
   Output: \n\n\
   Another donation over $20!  \n\
   Another donation over $20!  \n\
   Total donations over $20: 83.64")
presentLesson("Seletion Blocks", ll)

ll = []; l = ll.append
l("A Repetitive block executes a block of code over and again until some conditional check stops it.")
l("Repetition Example: While Loop\n\n\
        # Add 5 to a number for 6 seconds  \n\
        myNumber = 23                      \n\
        start = time.time()      \n\
        elapsed = 0 \n\n\
        # The while loop contains a condition or a 'test' \n\
        while elapsed <= 6:                \n\
            myNumber += 5                  \n\
            elapsed = time.time() - start  \n\
        print 'My number ended up as: ' + str(myNumber) \n\n\
   Output: \n\n\
   My number ended up as: 61181538")
presentLesson("Repetitive Blocks: While Loop", ll)

ll = []; l = ll.append
l("Repetition Example: For Loop\n\n\
        # Add 5 to a number 6 times  \n\
        myNumber = 23                      \n\n\
        # The for loop executes until it's out of input \n\
        # This use of the range function returns 0 thru 5 \n\
        for repetition in range(6):        \n\
            myNumber += 5                  \n\
        print 'My number ended up as: ' + str(myNumber) \n\n\
   Output: \n\n\
   My number ended up as: 53")
presentLesson("Repetitive Blocks: For Loop", ll)

ll = []; l = ll.append
l("Subroutines (aka functions, methods, procedures...) make code reusable within the same program and in other programs.")
l("Subroutine Example:\n\n\
        # Subroutine to increment by a given amount \n\
        def incrementNumber(numberIn, amount): \n\
            return numberIn + amount       \n\n\
        # Add 5 to a number for 6 seconds  \n\
        myNumber = 23                      \n\
        start = time.time()      \n\
        elapsed = 0  \n\
        while elapsed <= 6:                \n\
            myNumber = incrementNumber(myNumber, 5)  \n\
            elapsed = time.time() - start  \n\
        print 'My number ended up as: ' + str(myNumber) \n\n\
   Output: \n\n\
   My number ended up as: 42744218")
presentLesson("Subroutines", ll)

ll = []; l = ll.append
l("\n\     Write a program that calculates the volume of a cube, sphere or pyramid, \n\     given the necessary data. \n\n\     1. Write a sequence that calculates each. \n\n\
     2. Write a selection that calculates each based on a condition. \n\n\
     3. Write a subroutine that can be used repeatedly. \n\n\
     4. Write a loop that calculates the volume of a cube for lengths from 1 to 10 using the subroutine. \n\n\n\
     Volumes: \n\n\
     Cube:     length**3 \n\
     Sphere:   (4/3) * pi * radius**3    [ alt:  4 * pi * radius**3 / 3 ] \n\
     Pyramid:  (length**2 * height) / 3 \n\n")
presentLesson("Exercise: Code Blocks", ll)





