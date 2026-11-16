# ==========================================================
# PYTHON BOOLEANS
# ==========================================================
# Booleans represent one of two values: True or False.

# ---------- Boolean values ----------
# Comparing values returns a Boolean:
print(10 > 9)    # True
print(10 == 9)   # False
print(10 < 9)    # False

# In an if statement:
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# ---------- Evaluate values and variables ----------
print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15
print(bool(x), bool(y))

# ---------- Most values are True ----------
# Any string except "", any number except 0, any non-empty collection.
print(bool("abc"), bool(123), bool(["apple", "cherry"]))

# ---------- Some values are False ----------
print(bool(False), bool(None), bool(0), bool(""),
      bool(()), bool([]), bool({}))

# An object whose class defines __len__ returning 0 is also False:
class MyClass:
    def __len__(self):
        return 0

print(bool(MyClass()))

# ---------- Functions can return a Boolean ----------
def my_function():
    return True

if my_function():
    print("YES!")
else:
    print("NO!")

# Built-in functions that return Booleans, e.g. isinstance():
x = 200
print(isinstance(x, int))
