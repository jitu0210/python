# ==========================================================
# COPY DICTIONARIES
# ==========================================================
# dict2 = dict1 only creates a REFERENCE - both names point to the same dict.
dict1 = {"a": 1}
dict2 = dict1
dict1["b"] = 2
print(dict2)          # {'a': 1, 'b': 2}

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# ---------- copy() ----------
mydict = car.copy()
print(mydict)

# ---------- dict() ----------
mydict = dict(car)
print(mydict)

car["year"] = 2025
print(car["year"], mydict["year"])   # the copy is unchanged
