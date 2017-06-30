#!/usr/bin/python
import os, sys

# Exercise:
# kidsDict = { "Adams": ['John', 'Sue'], "Brown": ['Jennifer'], "Crow": ['Heidi", "Paul", "Betty"]}
# kidsDict["Douglas"] = ['Frank', 'Tom', 'Cheryl']
# kidsDict["Jackson"] = ['Marie', 'Shakira', 'Chuck']
# add more
# rsvpList = ['Douglas', 'Crow', 'Jackson']   # Extend, but not ALL will attend
# veganList = ['Paul Crow', 'Sue Adams', 'Shakira Jackson']
# glutenFreeList = ['Heidi Crow', 'Shakira Jackson']
# From these dicts and lists, determine how many lunches are needed for attending children of these different kinds: 
#    meat, meat-gluten free, veggie, veggie-gluten free.


kidsDict = { "Adams": ['John', 'Sue'], "Brown": ['Jennifer'], "Crow": ["Heidi", "Paul", "Betty"]}
kidsDict["Douglas"] = ['Frank', 'Tom', 'Cheryl']
kidsDict["Jackson"] = ['Marie', 'Shakira', 'Chuck']

rsvpList = ['Douglas', 'Crow', 'Jackson']

veganList = ['Paul Crow', 'Sue Adams', 'Shakira Jackson']

glutenFreeList = ['Heidi Crow', 'Shakira Jackson']

mealCountDict = { "meat":0, "meat-glutenFree":0, "veggie":0, "veggie-glutenFree":0 }

for rsvp in rsvpList:
    for kid in kidsDict[rsvp]:
        fullname = kid + " " + rsvp
        if fullname in veganList:
            key = "veggie"
        else:
            key = "meat"
        if fullname in glutenFreeList:
            key += "-glutenFree"
        mealCountDict[key] += 1

print "Meat               : " + str(mealCountDict["meat"])
print "Meat,   gluten free: " + str(mealCountDict["meat-glutenFree"])
print "Veggie             : " + str(mealCountDict["veggie"])
print "Veggie, gluten free: " + str(mealCountDict["veggie-glutenFree"])


# Alternative that also reports on which kid gets which lunch

mealTypeList = ["meat", "meat-glutenFree", "veggie", "veggie-glutenFree"]

# Initialize mealDict counts and report on allocation to recipients
# Uses a dictionary of dictionaries
mealDict = {}
for mealType in mealTypeList:
    mealDict[mealType] = {}
    mealDict[mealType]['count'] = 0
    mealDict[mealType]['recipient'] = []

for rsvp in rsvpList:
    for kid in kidsDict[rsvp]:
        fullname = kid + " " + rsvp
        if fullname in veganList:
            key = "veggie"
        else:
            key = "meat"
        if fullname in glutenFreeList:
            key += "-glutenFree"
        mealDict[key]['count'] += 1
        mealDict[key]['recipient'].append(fullname)

print "\n\nCounts of each meal needed:\n"
for mealType in mealTypeList:
    print mealType.ljust(20) + " : " + str(mealDict["meat"]['count'])

print "\n\nMeal Alloocation:\n"
for mealType in mealTypeList:
    for recipient in mealDict[mealType]['recipient']:
        print recipient.ljust(20) + " : " + mealType
print

sys.exit(0)








