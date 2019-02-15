# Def
# Class - a template
# Object - a particular instance of a class
# Constructor - code that runs when a object is created
# Attribute - a variable within a class
# Method - a function within a class
# Inheritance - the ability to extend a class to make a new class


# **type()** return the data type
# **dir()** lists capabilities: ones with underlines are used by Python itself
# the rest are operations that the object can perform (including attribute)


# Example 1
# The "self" typically used for  within a class to
# refer to the instance in which the method is being called

class PartyAnimal:
    x = 0

    def party(self):
        self.x += 1
        print('So far', self.x)


an = PartyAnimal()
an.party()
an.party()
an.party()


# Example 2
# Constructor: In object oriented programming,
#              it is a special block of statements called when an object is created.
# Instances: we can create many objects - the class is the template for the object
#            we can store each distinct object in its own variable
#            we call this having multiple instance of the same class
#            each instance has its own copy of the instance variables

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)


e1 = PartyAnimal("Sally")
e1.party()

e2 = PartyAnimal("Jim")
e2.party()
e2.party()  # We have two independent instances here e1 & e2


# Example 3
# Inheritance - another form of store and reuse
#               Subclasses are more specialized versions of a class,
#               which inherit attributes and behaviors from their parent classes,
#               and can introduce their own

# FootballFan() is a class extends PartyAnimal()
# It has all the capabilities of PartyAnimal and more


class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points += 7
        self.name = "Cute " + self.name
        self.party()
        print(self.name, "points", self.points)


e3 = FootballFan("Mos")
e3.touchdown()
