# ==========================================================
# PYTHON __init__() METHOD
# ==========================================================
# All classes have a built-in method __init__(), which runs automatically
# whenever a new object is created. Use it to set the object's values.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)
print(p1.name)
print(p1.age)

# ---------- Why use __init__()? ----------
# Without it, you'd have to set attributes manually on every object:
class PersonNoInit:
    pass

p = PersonNoInit()
p.name = "Tobias"
p.age = 25
print(p.name, p.age)
# __init__ makes sure every object starts with the data it needs.

# ---------- Default values ----------
class Person2:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

print(Person2("Emil").age)        # 18 (default)
print(Person2("Linus", 30).age)   # 30

# ---------- Multiple parameters ----------
class Car:
    def __init__(self, brand, model, year, color="black"):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

c = Car("Ford", "Mustang", 1964, "red")
print(c.brand, c.model, c.year, c.color)
