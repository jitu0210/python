# ==========================================================
# __call__
# ==========================================================
# __call__ makes an object callable like a function: obj()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)
print(double(5))        # 10
print(triple(5))        # 15
print(callable(double)) # True

# Useful for objects that remember state between calls:
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

c = Counter()
c(); c()
print(c())              # 3
