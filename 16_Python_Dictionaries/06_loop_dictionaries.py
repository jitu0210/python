# ==========================================================
# LOOP DICTIONARIES
# ==========================================================
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Keys (the default)
for x in car:
    print(x)

# Values by key
for x in car:
    print(car[x])

# values()
for x in car.values():
    print(x)

# keys()
for x in car.keys():
    print(x)

# Both keys and values with items()
for key, value in car.items():
    print(key, "->", value)
