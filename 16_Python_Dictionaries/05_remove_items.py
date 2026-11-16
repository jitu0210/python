# ==========================================================
# REMOVE DICTIONARY ITEMS
# ==========================================================

# ---------- pop() - remove by key ----------
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.pop("model")
print(car)

# ---------- popitem() - remove the LAST inserted item ----------
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.popitem()
print(car)

# ---------- del - remove by key ----------
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
del car["model"]
print(car)

# del can delete the whole dictionary:
del car
# print(car)   # NameError

# ---------- clear() - empty the dictionary ----------
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.clear()
print(car)     # {}
