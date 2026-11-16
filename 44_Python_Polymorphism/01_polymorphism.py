# ==========================================================
# PYTHON POLYMORPHISM
# ==========================================================
# Polymorphism = "many forms": the same method/function name used on
# different types.

# ---------- Function polymorphism ----------
# len() works on many types:
print(len("Hello World!"))                       # string
print(len(("apple", "banana", "cherry")))        # tuple
print(len({"brand": "Ford", "model": "Mustang"}))# dict

# ---------- Class polymorphism ----------
# Different classes with methods of the same name:
class Car:
    def __init__(self, brand, model):
        self.brand, self.model = brand, model
    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand, self.model = brand, model
    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand, self.model = brand, model
    def move(self):
        print("Fly!")

for x in (Car("Ford", "Mustang"), Boat("Ibiza", "Touring 20"), Plane("Boeing", "747")):
    x.move()

# ---------- Inheritance class polymorphism ----------
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")

class Car2(Vehicle):
    pass                       # uses Vehicle.move()

class Boat2(Vehicle):
    def move(self):            # overrides move()
        print("Sail!")

class Plane2(Vehicle):
    def move(self):
        print("Fly!")

for x in (Car2("Ford", "Mustang"), Boat2("Ibiza", "Touring 20"), Plane2("Boeing", "747")):
    print(x.brand, x.model, end=": ")
    x.move()
