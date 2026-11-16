# ==========================================================
# PYTHON CASTING
# ==========================================================
# Python is object-oriented: data types are classes.
# Casting is done with constructor functions:
#   int()   - builds an int from an int, a float (removes decimals),
#             or a string that holds a whole number
#   float() - builds a float from an int, float, or a numeric string
#   str()   - builds a string from strings, ints, floats and more

# Integers
x = int(1)     # 1
y = int(2.8)   # 2
z = int("3")   # 3
print(x, y, z)

# Floats
x = float(1)      # 1.0
y = float(2.8)    # 2.8
z = float("3")    # 3.0
w = float("4.2")  # 4.2
print(x, y, z, w)

# Strings
x = str("s1")  # 's1'
y = str(2)     # '2'
z = str(3.0)   # '3.0'
print(x, y, z)

# A string that is not a number cannot become an int:
try:
    int("abc")
except ValueError as e:
    print("ValueError:", e)
