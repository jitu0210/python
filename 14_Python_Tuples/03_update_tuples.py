# ==========================================================
# UPDATE TUPLES
# ==========================================================
# Tuples are unchangeable (immutable), but there are workarounds.

# ---------- Change values: convert to list and back ----------
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# ---------- Add items ----------
# 1) Convert to a list:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# 2) Add a tuple to a tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# ---------- Remove items ----------
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# del removes the whole tuple:
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)   # NameError
