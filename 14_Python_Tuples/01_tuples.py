# ==========================================================
# PYTHON TUPLES
# ==========================================================
# A tuple stores multiple items in one variable, using round brackets.
# Tuples are ORDERED and UNCHANGEABLE and ALLOW DUPLICATES.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Duplicates allowed:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# ---------- Tuple length ----------
print(len(thistuple))

# ---------- Tuple with ONE item ----------
# You need a trailing comma, otherwise it is not a tuple:
thistuple = ("apple",)
print(type(thistuple))   # tuple
thistuple = ("apple")
print(type(thistuple))   # str!

# ---------- Data types ----------
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
print(tuple1, tuple2, tuple3, tuple4)

# ---------- type() ----------
print(type(tuple1))

# ---------- tuple() constructor ----------
thistuple = tuple(("apple", "banana", "cherry"))   # double round brackets
print(thistuple)
