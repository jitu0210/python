# ==========================================================
# CHANGE DICTIONARY ITEMS
# ==========================================================
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# ---------- Change a value by its key ----------
car["year"] = 2018
print(car)

# ---------- update() ----------
# Updates the dictionary with items from another dict / iterable of pairs
car.update({"year": 2020})
print(car)
