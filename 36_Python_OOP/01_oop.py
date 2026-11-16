# ==========================================================
# PYTHON OOP (Object-Oriented Programming)
# ==========================================================
# OOP organises code around OBJECTS that bundle data (attributes)
# and behaviour (methods).
#
# Advantages:
#   - gives programs a clear structure
#   - keeps code DRY (Don't Repeat Yourself) - easier to maintain
#   - makes it easy to reuse code
#   - lets you build complex programs from simple pieces
#
# Classes and objects:
#   A CLASS is a template/blueprint.  An OBJECT is an instance of it.
#
#   class: Fruit       -> objects: Apple, Banana, Mango
#   class: Car         -> objects: Volvo, Audi, Toyota
#
# Each object gets the class's variables and functions.
#
# The four pillars covered in the next folders:
#   Classes/Objects, Inheritance, Polymorphism, Encapsulation

class Fruit:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print("This is a", self.name)

apple = Fruit("Apple")
banana = Fruit("Banana")
apple.describe()
banana.describe()
