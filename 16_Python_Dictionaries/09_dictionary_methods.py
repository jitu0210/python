# ==========================================================
# DICTIONARY METHODS
# ==========================================================
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(car.copy())                         # copy()
print(dict.fromkeys(["a", "b"], 0))       # fromkeys() - dict from keys + value
print(car.get("model"))                   # get()
print(car.items())                        # items()
print(car.keys())                         # keys()
print(car.values())                       # values()
print(car.setdefault("color", "red"))     # setdefault() - get, or insert if missing
print(car)
car.update({"year": 2020})                # update()
print(car)
print(car.pop("color"))                   # pop()     - remove by key
print(car.popitem())                      # popitem() - remove last inserted
car.clear()                               # clear()
print(car)
