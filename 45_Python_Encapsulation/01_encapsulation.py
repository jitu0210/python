# ==========================================================
# PYTHON ENCAPSULATION
# ==========================================================
# Encapsulation = bundling data and methods together, and protecting the
# data from being changed directly from outside.

# ---------- Private properties ( __name ) ----------
# Two underscores make a property private (name-mangled by Python).
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age          # private

p1 = Person("Emil", 25)
print(p1.name)
# print(p1.__age)                # AttributeError

# ---------- Getter / setter methods ----------
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:               # validation!
            self.__age = age
        else:
            print("Age must be positive")

p = Person2("Tobias", 25)
print(p.get_age())
p.set_age(26)
print(p.get_age())
p.set_age(-5)

# ---------- Why encapsulation? ----------
# - protects data from invalid values
# - lets you change the inner details without breaking other code
# - controls how data is read and written
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(2000)
print(acc.get_balance())

# ---------- Protected properties ( _name ) ----------
# One underscore = "internal use" by convention. Python does not block it.
class Person3:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

print(Person3("Linus", 50000)._salary)   # works, but you shouldn't

# ---------- Private methods ----------
class Calculator:
    def __validate(self, n):
        return isinstance(n, (int, float))

    def add(self, a, b):
        if self.__validate(a) and self.__validate(b):
            return a + b
        return None

print(Calculator().add(5, 3))

# ---------- Name mangling ----------
# __age actually becomes _Person__age - private by convention, not truly hidden.
print(p1._Person__age)

# ---------- @property - Pythonic getters/setters ----------
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self.__celsius = value

t = Temperature(25)
t.celsius = 30           # uses the setter
print(t.celsius)         # uses the getter
