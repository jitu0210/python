# ==========================================================
# PYTHON MAGIC METHODS (dunder methods)
# ==========================================================
# Magic methods have double underscores at the start and end (__init__).
# Python calls them automatically for built-in operations:
#
#   __init__      object creation          Point(1, 2)
#   __str__       print() / str()          print(p)
#   __repr__      repr() / developer view  repr(p)
#   __eq__        ==                       p1 == p2
#   __lt__        <                        p1 < p2
#   __add__       +                        p1 + p2
#   __len__       len()                    len(obj)
#   __contains__  in                       x in obj
#   __call__      calling like a function  obj()
#
# Each has its own file in this folder.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

a = Point(1, 2)
b = Point(3, 4)
print(a + b)
print(a == Point(1, 2))

# See all magic methods an object supports:
print([m for m in dir(a) if m.startswith("__")][:12], "...")
