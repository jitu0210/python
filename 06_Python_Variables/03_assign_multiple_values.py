# ==========================================================
# ASSIGN MULTIPLE VALUES
# ==========================================================

# ---------- Many values to multiple variables ----------
# The number of variables must match the number of values.
x, y, z = "Mango", "Grape", "Guava"
print(x)
print(y)
print(z)

# ---------- One value to multiple variables ----------
x = y = z = "Mango"
print(x)
print(y)
print(z)

# ---------- Unpack a collection ----------
# Values in a list / tuple can be extracted into variables (unpacking).
fruits = ["mango", "grape", "guava"]
x, y, z = fruits
print(x)
print(y)
print(z)
