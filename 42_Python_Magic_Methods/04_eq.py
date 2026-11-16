# ==========================================================
# __eq__
# ==========================================================
# __eq__ defines what == means for your objects.
# Without it, == checks if both are the SAME object.

class Plain:
    def __init__(self, x):
        self.x = x

print(Plain(1) == Plain(1))     # False - different objects

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

print(Point(1, 2) == Point(1, 2))   # True
print(Point(1, 2) == Point(2, 1))   # False
print(Point(1, 2) != Point(2, 1))   # True (!= uses __eq__ automatically)
print(Point(1, 2) == "text")        # False
