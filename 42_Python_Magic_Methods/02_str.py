# ==========================================================
# __str__
# ==========================================================
# __str__ returns a readable string for the object.
# Used by print() and str().

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Emil", 36)
print(p)               # <__main__.Person object at 0x...>  - not useful

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

p = Person2("Emil", 36)
print(p)               # Emil is 36 years old
print(str(p))
print(f"Info: {p}")    # f-strings use __str__ too
