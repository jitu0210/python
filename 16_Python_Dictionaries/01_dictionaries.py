# ==========================================================
# PYTHON DICTIONARIES
# ==========================================================
# Dictionaries store data values in key:value pairs.
# They are ORDERED (Python 3.7+), CHANGEABLE, and do NOT allow duplicate keys.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# ---------- Dictionary items ----------
print(thisdict["brand"])

# ---------- Duplicates not allowed ----------
# A repeated key overwrites the earlier value:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print(thisdict)

# ---------- Length ----------
print(len(thisdict))

# ---------- Values can be of any type ----------
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))

# ---------- dict() constructor ----------
thisdict = dict(name="Ravi", age=36, country="India")
print(thisdict)
