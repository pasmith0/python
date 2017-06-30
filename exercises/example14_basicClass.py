#!/usr/bin/python
import sys

class Pencil:
    leadColor  = 'grey'
    paintColor = 'yellow'
    hardness   = '2'
    length     = 7
    usageTime  = 0

    def __init__(self, leadColor, paintColor, hardness, length):
        self.leadColor  = leadColor
        self.paintColor = paintColor
        self.hardness   = hardness
        self.length     = length

    def incrementUsageTime(self, time):
        # time is in minutes
        self.usageTime += time
        # length decreases with time used
        self.length -= time * 0.005

pencilObj = Pencil('red', 'red', '6', 7)
pencilObj.incrementUsageTime(10)
print 'Pencil length is now: ' + str(pencilObj.length) + ' inches.'
pencilObj.incrementUsageTime(15)
print 'Pencil length is now: ' + str(pencilObj.length) + ' inches.'
pencilObj.incrementUsageTime(8)
print 'Pencil length is now: ' + str(pencilObj.length) + ' inches.'

sys.exit(0)
