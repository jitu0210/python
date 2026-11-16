# ==========================================================
# PYTHON INNER CLASSES
# ==========================================================
# An inner (nested) class is a class defined inside another class.
# Use it to group classes that only make sense together.

class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "Inner Class"

        def display(self):
            print("This is the inner class")

outer = Outer()
print(outer.name)

# ---------- Accessing the inner class from outside ----------
inner = Outer.Inner()
inner.display()
print(inner.name)

# ---------- Accessing the outer class from the inner class ----------
# The inner class has no automatic link to an outer OBJECT - pass it in:
class Outer2:
    def __init__(self):
        self.name = "Emil"

    class Inner:
        def __init__(self, outer):
            self.outer = outer

        def display(self):
            print("Outer name:", self.outer.name)

o = Outer2()
i = o.Inner(o)
i.display()

# ---------- Practical example ----------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "Off"

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "Off"
            print("Engine stopped")

    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()

# ---------- Multiple inner classes ----------
class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()

    class CPU:
        def process(self):
            print("Processing data...")

    class RAM:
        def store(self):
            print("Storing data...")

pc = Computer()
pc.cpu.process()
pc.ram.store()
