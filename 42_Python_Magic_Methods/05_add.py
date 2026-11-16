# ==========================================================
# __add__
# ==========================================================
# __add__ defines what + does for your objects.

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"Rs {self.amount}"

a = Money(100)
b = Money(250)
print(a + b)            # Rs 350

# Related operator methods:
#   __sub__  -     __mul__  *     __truediv__  /
#   __floordiv__ //   __mod__ %   __pow__ **
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Vector(self.x - o.x, self.y - o.y)

    def __mul__(self, n):
        return Vector(self.x * n, self.y * n)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v = Vector(2, 3)
w = Vector(1, 1)
print(v + w, v - w, v * 3)
