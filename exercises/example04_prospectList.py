#!/usr/bin/python
import os, sys

# List Exercise Two
# =================
# In a script:
#   Initialize an array called "prospectList"
#   Append to prospectList the names:  
#     "Bill Gates", "Steve Jobs", "Jim Carrey", "Steve Wazniak", "Bob Barker", "Mark Zuckerberg", "Shannen Doherty", "Paul Allen"
#   Initialize another list called "rejectList"
#   Append to rejectList the names: "Jim Carrey", "Bob Barker", "Shannen Doherty"
#   Manipulate these lists so that you can easily remove the rejects from the prospects and end up with a "hireList".


prospectList = []
prospectList.append("Bill Gates")
prospectList.append("Steve Jobs")
prospectList.append("Jim Carrey")
prospectList.append("Steve Wazniak")
prospectList.append("Bob Barker")
prospectList.append("Mark Zuckerberg")
prospectList.append("Shannen Doherty")
prospectList.append("Paul Allen")

rejectList = []
rejectList.append("Jim Carrey")
rejectList.append("Bob Barker")
rejectList.append("Shannen Doherty")

# Method 1
hireList = list(prospectList)
for reject in rejectList:
    if reject in hireList:
        hireList.remove(reject)
print "Method 1 hire list: " + str(hireList)

# Method 2
hireList = []
for prospect in prospectList:
    if prospect not in rejectList: 
        hireList.append(prospect)
print "Method 2 hire list: " + str(hireList)
 
sys.exit(0)
