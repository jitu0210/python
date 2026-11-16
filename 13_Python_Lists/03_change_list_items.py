# ==========================================================
# CHANGE LIST ITEMS
# ==========================================================

# ---------- Change one item ----------
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# ---------- Change a range of items ----------
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert MORE items than you replace -> list grows
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert FEWER items than you replace -> list shrinks
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# ---------- Insert items ----------
# insert(index, item) adds an item without replacing anything
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
