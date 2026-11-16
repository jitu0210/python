# ==========================================================
# PYTHON self PARAMETER
# ==========================================================
# `self` is a reference to the CURRENT instance of the class.
# It is used to access the object's attributes and methods.
# It must be the first parameter of every instance method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()          # Python passes p1 as self automatically

# ---------- Why self? ----------
# Without self, methods could not tell WHICH object's data to use.
p2 = Person("Tobias", 30)
p2.greet()

# ---------- Accessing properties with self ----------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(self.brand + " " + self.model)

Car("Toyota", "Corolla").display()

# ---------- Calling other methods with self ----------
class Calculator:
    def add(self, a, b):
        return a + b

    def add_and_double(self, a, b):
        return self.add(a, b) * 2

print(Calculator().add_and_double(2, 3))

# ---------- self is just a convention ----------
# You can name it anything (but please don't - always use self):
class Weird:
    def __init__(this, name):
        this.name = name

    def show(abc):
        print("Name:", abc.name)

Weird("Linus").show()
