# ==========================================================
# PYTHON CLASSES / OBJECTS
# ==========================================================
# Almost everything in Python is an object, with properties and methods.
# A class is an object constructor - a "blueprint" for creating objects.

# ---------- Create a class ----------
class MyClass:
    x = 5

print(MyClass)

# ---------- Create an object ----------
p1 = MyClass()
print(p1.x)

# ---------- Delete an object ----------
p2 = MyClass()
del p2
# print(p2)   # NameError

# ---------- Multiple objects ----------
# Each object is independent:
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
p2.x = 10
print(p1.x, p2.x, p3.x)

# ---------- The pass statement ----------
# A class definition cannot be empty:
class Person:
    pass
