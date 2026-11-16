# ==========================================================
# ACCESS DICTIONARY ITEMS
# ==========================================================
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# ---------- By key ----------
print(car["model"])
print(car.get("model"))          # get() - returns None instead of an error
print(car.get("color"))          # None
print(car.get("color", "n/a"))   # default value

# ---------- Get keys ----------
x = car.keys()
print(x)
# The keys view is LIVE - it updates when the dictionary changes:
car["color"] = "white"
print(x)

# ---------- Get values ----------
y = car.values()
print(y)
car["year"] = 2020
print(y)                         # also live

# ---------- Get items (key, value) pairs ----------
z = car.items()
print(z)

# ---------- Check if a key exists ----------
if "model" in car:
    print("Yes, 'model' is one of the keys")
