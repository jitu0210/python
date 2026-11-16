# ==========================================================
# PYTHON NUMBERS
# ==========================================================
# There are three numeric types: int, float, complex
x = 1      # int
y = 2.8    # float
z = 1j     # complex
print(type(x), type(y), type(z))

# ---------- Int ----------
# Whole number, positive or negative, without decimals, unlimited length
x = 1
y = 35656222554887711
z = -3255522
print(x, y, z)

# ---------- Float ----------
# Number with one or more decimals
x = 1.10
y = 1.0
z = -35.59
print(x, y, z)

# Floats can be scientific numbers with "e" = power of 10
x = 35e3      # 35000.0
y = 12E4      # 120000.0
z = -87.7e100
print(x, y, z)

# ---------- Complex ----------
# Written with "j" as the imaginary part
x = 3 + 5j
y = 5j
z = -5j
print(x, y, z)

# ---------- Type conversion ----------
x = 1
y = 2.8
z = 1j
a = float(x)    # int -> float
b = int(y)      # float -> int (decimals are cut off)
c = complex(x)  # int -> complex
print(a, b, c)
# You cannot convert complex numbers into another number type.

# ---------- Random number ----------
# Python has a built-in module called random:
import random
print(random.randrange(1, 10))
