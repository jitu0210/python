# ==========================================================
# PYTHON MATH
# ==========================================================

# ---------- Built-in math functions ----------
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x, y)

print(abs(-7.25))        # absolute (positive) value
print(pow(4, 3))         # 4 to the power of 3 = 64

# ---------- The math module ----------
import math

print(math.sqrt(64))     # square root
print(math.ceil(1.4))    # round UP   -> 2
print(math.floor(1.4))   # round DOWN -> 1
print(math.pi)           # PI constant

# A few more useful ones:
print(math.factorial(5))
print(math.gcd(12, 18))
print(math.isclose(0.1 + 0.2, 0.3))
print(math.log(math.e), math.log10(1000))
print(math.sin(math.pi / 2), math.cos(0))
print(math.inf, math.e)
