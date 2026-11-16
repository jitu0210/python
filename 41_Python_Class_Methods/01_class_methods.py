# ==========================================================
# PYTHON CLASS METHODS
# ==========================================================
# Methods are functions that belong to a class/object.

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

# ---------- Methods with parameters ----------
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

# ---------- Methods that change properties ----------
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show(self):
        print(f"{self.owner}: {self.balance}")

acc = Account("Ravi")
acc.deposit(500)
acc.show()

# ---------- The __str__() method ----------
# Controls what is shown when the object is printed.
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

print(Person2("Tobias", 36))

# ---------- @classmethod and @staticmethod ----------
class Pizza:
    count = 0

    def __init__(self, topping):
        self.topping = topping
        Pizza.count += 1

    @classmethod                 # receives the CLASS (cls), not the object
    def margherita(cls):
        return cls("tomato & mozzarella")

    @staticmethod                # receives neither - a plain helper function
    def is_valid_size(size):
        return size in ("S", "M", "L")

p = Pizza.margherita()
print(p.topping, "| pizzas made:", Pizza.count)
print(Pizza.is_valid_size("M"))

# ---------- Delete methods ----------
class Temp:
    def hello(self):
        print("hello")

del Temp.hello
# Temp().hello()   # AttributeError
