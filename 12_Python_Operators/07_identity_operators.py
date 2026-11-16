# ==========================================================
# IDENTITY OPERATORS
# ==========================================================
# Identity operators compare OBJECTS: are they the very same object
# in memory? (Not just equal values.)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)      # True  - z is the same object as x
print(x is y)      # False - same content, but different objects
print(x == y)      # True  - == compares the VALUES

print(x is not z)  # False
print(x is not y)  # True

# ---------- Difference between is and == ----------
#   ==  checks if the values are equal
#   is  checks if both refer to the same object
# Use `is` mainly for None:
value = None
print(value is None)
