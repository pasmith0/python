#!/usr/bin/python
import sys

class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError('Subclass must implement abstract method')

class Cat(Animal):               # Inherits Animal class Constructor and attributes
    def talk(self):
        return 'Meow!'

class Dog(Animal):               # Inherits Animal class Constructor and attributes
    def talk(self):
        return 'Woof! Woof!'

animalList = [Cat('Missy'),
              Dog('Lassie'),
              Animal('Igor'),
             ]

for animal in animalList:
    try:
        print(animal.name + ': ' + animal.talk())
    except NotImplementedError, e:
        print 'Exception found: ' + str(e)

sys.exit(0)
