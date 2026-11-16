# ==========================================================
# NESTED DICTIONARIES
# ==========================================================
# A dictionary can contain other dictionaries.
myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}
print(myfamily)

# Or build it from separate dictionaries:
child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}
myfamily = {"child1": child1, "child2": child2, "child3": child3}

# ---------- Access items in nested dictionaries ----------
print(myfamily["child2"]["name"])

# ---------- Loop through nested dictionaries ----------
for key, child in myfamily.items():
    print(key)
    for field in child:
        print("   ", field + ":", child[field])
