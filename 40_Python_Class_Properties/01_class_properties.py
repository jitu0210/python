# ==========================================================
# PYTHON CLASS PROPERTIES
# ==========================================================
# Properties (attributes) are the variables that belong to a class/object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

# ---------- Access properties ----------
print(p1.name, p1.age)

# ---------- Modify properties ----------
p1.age = 40
print(p1.age)

# ---------- Delete properties ----------
del p1.age
# print(p1.age)   # AttributeError

# ---------- Class properties vs instance properties ----------
#   Instance properties - defined in __init__ with self, unique per object
#   Class properties    - defined directly in the class, SHARED by all objects
class Dog:
    species = "Canis familiaris"      # class property

    def __init__(self, name):
        self.name = name              # instance property

d1 = Dog("Buddy")
d2 = Dog("Max")
print(d1.name, d1.species)
print(d2.name, d2.species)

# ---------- Modifying class properties ----------
Dog.species = "Wolf-ish"              # change for ALL objects
print(d1.species, d2.species)

# ---------- Add new properties ----------
d1.age = 3                            # only d1 gets this property
print(d1.age)
print(hasattr(d2, "age"))             # False
