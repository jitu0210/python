# ==========================================================
# PYTHON INHERITANCE
# ==========================================================
# Inheritance lets a class take all the methods and properties of another.
#   Parent (base) class  - the class being inherited from
#   Child (derived) class - the class that inherits

# ---------- Create a parent class ----------
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

# ---------- Create a child class ----------
class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()            # inherited from Person

# ---------- Add __init__() to the child ----------
# The child's __init__ OVERRIDES the parent's. To keep the parent's
# behaviour, call it explicitly:
class Student2(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

# ---------- super() ----------
# super() refers to the parent without naming it:
class Student3(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year          # add a property

    def welcome(self):                      # add a method
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)

x = Student3("Mike", "Olsen", 2019)
print(x.graduationyear)
x.welcome()

# A child method with the same name as a parent method overrides it.
print(isinstance(x, Person), issubclass(Student3, Person))
