# ==========================================================
# ADD DICTIONARY ITEMS
# ==========================================================
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# ---------- Use a new key ----------
car["color"] = "red"
print(car)

# ---------- update() ----------
# If the key does not exist it is added:
car.update({"owner": "Ravi"})
print(car)
