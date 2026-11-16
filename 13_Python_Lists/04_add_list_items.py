# ==========================================================
# ADD LIST ITEMS
# ==========================================================

# ---------- append() - add to the end ----------
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# ---------- insert() - add at a given index ----------
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# ---------- extend() - add items from another list ----------
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# ---------- extend() with any iterable (tuple, set, dict...) ----------
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
