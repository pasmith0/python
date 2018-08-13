#!/usr/bin/python

from classLibrary import *

ll = []; l = ll.append
l("As the name implies, Object-Oriented Programming, OOP, is a strategy for organizing code \n \
    by grouping variables and functions related to 'things' into identifiable objects.")

l("For example, an invoice might be a thing that has associated variables, called attributes, \n \
    and a group of functions related to invoices, that are referred to as methods.")

l("By defining the attributes and methods related to invoices in a 'class', a new invoice \n \
    can be created in a program as easily as 'myInvoice = Invoice()', at which point the attributes \n \
    and methods of invoice can be invoked like this:  \n\n\
           myInvoice = Invoice()      \n\
           myInvoice.totalAmt = 47.50 \n\
           myInvoice.postInvoice()")

l("Essentially all Python built-in functionality involves objects, so much of what has been \n \
    described thus far are examples of using objects. \n \
    For example: list, string and dictionary objects all have methods we've used. \n\n\
           myList = []    \n\
           myList.append('aaa')  \n\
           myString = 'Mary had a little lamb...' \n\
           if myString.startswith('Mary'): ...")

l("OOP has three basic tenants, each of which must be implemented in some way for a language to be object-oriented: \n\n\
           1.  Encapsulation:  the attributes and methods of a 'thing' combine in a class \n\n\
           2.  Polymorphism:   multiple methods can receive the same name and perform related tasks in dissimilar ways \n\n\
           3.  Inheritance:    a class can build hierarchically on another class or classes")

presentLesson("Object-Oriented Programming", ll, False)


ll = []; l = ll.append
l("In Python, objects are instances of classes, and a class encapsulates attributes and methods \n \
    and can inherit the attributes and methods of other, baser, classes. \n \
    For example: \n\n\
           There can be a class called 'Dog' that has attributes and functionality related to dogs. \n\n\
           The class, Dog, can inherit from 'Mammal', which in turn can inherit from the class 'Animal'. \n\n\
           'Buster' might be an instance of 'Dog'. 'Dog' is a class, so 'Buster' is an object instance of that class.")

l("Here's an example of a class, showing attributes and methods: \n\n\
           class Pencil:                 \n\
               leadColor  = 'grey'       \n\
               paintColor = 'yellow'     \n\
               hardness   = '2'          \n\
               length     = 7            \n\
               usageTime  = 0            \n\n\
               def __init__(self, leadColor, paintColor, hardness, length):     # constructor  \n\
                   self.leadColor  = leadColor        \n\
                   self.paintColor = paintColor       \n\
                   self.hardness   = hardness         \n\
                   self.length     = length           \n\n\
               def incrementUsageTime(self, time):    \n\
                   # time is in minutes               \n\
                   self.usageTime += time             \n\
                   # length decreases with time used  \n\
                   self.length -= time * 0.005        \n\n\
           pencilObj = Pencil('red', 'red', '6', 7)   \n\
           pencilObj.incrementUsageTime(10)           \n\
           print 'Pencil length is now: ' + str(pencilObj.length) + ' inches.' \n\
           pencilObj.incrementUsageTime(15)                                    \n\
           print 'Pencil length is now: ' + str(pencilObj.length) + ' inches.' \n\
           pencilObj.incrementUsageTime(8)                                     \n\
           print 'Pencil length is now: ' + str(pencilObj.length) + ' inches.' \n\n\
           Pencil length is now: 6.95 inches.\n\
           Pencil length is now: 6.875 inches.\n\
           Pencil length is now: 6.835 inches.\n")

l("Here's an example of a class that inherits from another class. \n \
    Note that in this case, the base class, Animal, expects the 'talk' method to be overriden. \n \
    That becomes an example of polymorphism - 'talk' implemented in many ways: \n\n\
            class Animal:                \n\
                def __init__(self, name):    # Constructor of the class  \n\
                    self.name = name     \n\
                def talk(self):              # Abstract method, defined by convention only  \n\
                    raise NotImplementedError('Subclass must implement abstract method')    \n\n\
            class Cat(Animal):               # Inherits Animal class Constructor and attributes \n\
                def talk(self):          \n\
                    return 'Meow!'       \n\n\
            class Dog(Animal):               # Inherits Animal class Constructor and attributes  \n\
                def talk(self):          \n\
                    return 'Woof! Woof!' \n\n\
            animalList = [Cat('Missy'),     \n\
                          Dog('Lassie'),    \n\
                          Animal('Igor'),   \n\
                         ]                  \n\n\
            for animal in animalList:       \n\
                try:                     \n\
                    print(animal.name + ': ' + animal.talk())   \n\
                except NotImplementedError, e:                  \n\
                    print 'Exception found: ' + str(e)   \n\n\
            Missy: Meow!  \n\
            Lassie: Woof! Woof!   \n\
            Exception found: Subclass must implement abstract method")

presentLesson("Python Classes", ll)

ll = []; l = ll.append
l("Note that most objects are mutable, meaning values of attributes can change. \n\n\
         myObj.attr1 = newValue")
l("Objects can be compared for equality. \n\n\
         if myObj1 == myObj2: \n\n \
    That will test true if the variables myObj1 and myObj2 refer to the same object in memory. In other words, they must be aliases. \n\n\
         myObj2 = myObj1 \n\n\
         if myObj1 == myObj2: \n\
             print 'Yes, they are aliases!' \n\n\
         if myObj1 is myObj2:   # An alternative syntax for objects \n\
             print 'Yes, they is each other'")
l("To make a copy of an object, so that there really are two identical objects, but not aliases, \n \
    use the copy module: \n\n\
         import copy \n\
         myObj2 = copy.copy(myObj1)")

l("Objects can be passed as parameters to functions, returned from functions and can be stored in lists, tuples and dictionaries.")
presentLesson("Class Operations", ll)

ll = []; l = ll.append
l("Methods like '__init__' have special meanings to Python. \n \
    For a list of such functions and their meanings and uses, consult: \n\n\
          Python special functions: \n\n\
              http://docs.python.org/2/reference/datamodel.html#special-method-names")
presentLesson("Python Special Methods", ll)

ll = []; l = ll.append
l("Once a class has been defined, additional attributes and methods can be added to it. \n \
    Once an object has been 'instantiated,' more attributes and methods can be added to it as well.")

l("When a class is altered, the changes take place for all existing instances of the class. \n \
    Example of adding an attribute and a method to a defined class: \n\n\
           class Pencil:                 \n\
               leadColor  = 'grey'       \n\
               paintColor = 'yellow'     \n\
               hardness   = '2'          \n\
               length     = 7            \n\
               usageTime  = 0            \n\
               usageRate  = 0.005        \n\n\
               def __init__(self, leadColor, paintColor, hardness, length):     # constructor  \n\
                   self.leadColor  = leadColor        \n\
                   self.paintColor = paintColor       \n\
                   self.hardness   = hardness         \n\
                   self.length     = length           \n\n\
               def incrementUsageTime(self, time):    \n\
                   # time is in minutes               \n\
                   self.usageTime += time             \n\
                   # length decreases with time used  \n\
                   self.length -= time * self.usageRate  \n\n\
           # Make an instance of class, Pencil        \n\
           pencilObj = Pencil('red', 'red', '6', 7)   \n\n\
           def adjustLengthForHardness(self):         \n\
               self.length -= self.length * int(self.hardness) * self.hardnessFactor   \n\n\
           # Add attribute and method to defined class \n\
           Pencil.hardnessFactor = 0.001              \n\
           Pencil.adjustLengthForHardness = adjustLengthForHardness   \n\n\
           print 'Old length: ' + str(pencilObj.length)  \n\
           pencilObj.adjustLengthForHardness()   \n\
           print 'New length: ' + str(pencilObj.length) \n\n\
           Old length: 6.95 \n\
           New length: 6.9083")

l("When attributes and methods are added to an instance of a class, only that instance is affected. \n \
    Example of adding an attribute and a method to an existing instance of a class: \n\n\
          import types    \n\n\
          class Animal:      \n\
              def __init__(self, name):    # Constructor of the class  \n\
                  self.name = name                                     \n\
              def talk(self):              # Abstract method, defined by convention only  \n\
                  raise NotImplementedError('Subclass must implement abstract method')   \n\
              def food(self):   \n\
                  raise NotImplementedError('Subclass must implement abstract method')    \n\n\
          class Cat(Animal):               # Inherits Animal class Constructor and attributes \n\
              def talk(self):          \n\
                  return 'Meow!'       \n\n\
          oscar  = Cat('Oscar')        \n\
          marble = Cat('Marble')       \n\n\
          def catFood(self):           \n\
              return self.favoriteFood \n\n\
          setattr(oscar, 'favoriteFood', 'kibble')  \n\
          oscar.food = types.MethodType( catFood, oscar ) \n\
          print 'Oscar  eats: ' + oscar.food()  \n\
          print 'Marble eats: ' + marble.food()  \n\n\
          Oscar  eats: kibble   \n\
          NotImplementedError: Subclass must implement abstract method")

l("If you just need to store data related to an object and later reuse it, Python makes it simple to do: \n\n\
           class Pencil:                 \n\
               leadColor  = 'grey'       \n\
               paintColor = 'yellow'     \n\
               hardness   = '2'          \n\
               length     = 7            \n\
               usageTime  = 0            \n\
               usageRate  = 0.005        \n\n\
               def __init__(self, leadColor, paintColor, hardness, length):     # constructor  \n\
                   self.leadColor  = leadColor        \n\
                   self.paintColor = paintColor       \n\
                   self.hardness   = hardness         \n\
                   self.length     = length           \n\n\
               def incrementUsageTime(self, time):    \n\
                   # time is in minutes               \n\
                   self.usageTime += time             \n\
                   # length decreases with time used  \n\
                   self.length -= time * self.usageRate  \n\n\
           pencilObj = Pencil('red', 'red', '6', 7)   \n\n\
           pencilObj.maker = 'Office Depot'           \n\
           ...                                        \n\
           if pencilObj.maker == 'Office Depot':      \n\
               pencilObj.usageRate = 0.004")

presentLesson("Extending An Object's Attributes and Methods", ll)

ll = []; l = ll.append
l("Objects that will no longer be used, like variables that will no longer be referenced, get detected and removed from memory \n \
    at intervals as a program runs. This keeps memory from being cluttered. \n \
    If you want to speed garbage collection along, delete objects you don't intend to keep using with 'del':\n\n\
            del myObj")
presentLesson("Garbage Collection", ll)

ll = []; l = ll.append
l("While it can be handy to use global variables, and some languages make all variables global in scope, \n \
    good modular coding technique seeks to reduce dependency on global variables to zero. \n \
    Nonetheless, some believe that as long as it's in a class, it must conform to high standards. \n \
    >>>   It ain't so!   <<<")
l("Specifically, the attributes defined in a class are always available for use, even when no instance of that class exists. \n \
    The class itself is a namespace. \n\n\
        For example: \n\n\
            class Animal:       \n\
                lifespan = 12   \n\n\
            Animal.lifespan = 34 \n\n\
            print 'Lifespan is: ' + str(Animal.lifespan) \n\n\
            Lifespan is: 34")

l("Such use of classes creates a non-OOP abuse of the syntax. \n \
    Here's another example that seems better, but really isn't: \n\n\
            class Animal:       \n\
                animalCount = 0   \n\
                def __init__(self, name):    # Constructor of the class \n\
                    self.name = name   \n\
                    Animal.animalCount += 1 \n\
                def talk(self):              # Abstract method, defined by convention only  \n\
                    raise NotImplementedError('Subclass must implement abstract method') \n\n\
            class Cat(Animal):               # Inherits Animal class Constructor and attributes \n\
                def talk(self):     \n\
                    return 'Meow!'  \n\n\
            class Dog(Animal):               # Inherits Animal class Constructor and attributes  \n\
                def talk(self):     \n\
                    return 'Woof! Woof!' \n\n\
            animalList = [Cat('Missy'),  \n\
                          Dog('Lassie'),  \n\
                          Dog('Killer'),  \n\
                         ]  \n\n\
            print 'Animal count is: ' + str(Animal.animalCount) \n\n\
            Animal count is: 3")

l("It is far better to track the number of Animal instances in the external code. \n \
    What would happen if the line 'Animal.animalCount += 1' changed to 'self.animalCount += 1' ?")
presentLesson("Using Classes For Global Variables", ll)

ll = []; l = ll.append
l("\n\     Write a program that determines the center point of a rectangle, \n\     given the length, width and lower-left corner point of the rectangle. \n\n\        Devise and use classes for the following: \n\n\
             1. A point \n\
                    include x and y coordinates \n\
                    a method for the formatted print of the point \n\
                    a method to calculate the distance of the point from the origin \n\
             2. A rectangle. \n\
                    include the length, width, and corner point as attributes \n\
                    a method to find the x-coord of the central point of the rectangle \n\
                    a method to find the y-coord of the central point of the rectangle \n\
                    a method to determine and report the central point \n\
                    a method to report the distance of the central point from the origin")
presentLesson("Exercise: Classes and Objects", ll)

ll = []; l = ll.append
execGroups(ll, "More examples are in example14_*.py")
















