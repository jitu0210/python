# ==========================================================
# REMOVE LIST ITEMS
# ==========================================================

# ---------- remove() - remove a specified item ----------
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# If there are duplicates, remove() only removes the FIRST one:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# ---------- pop() - remove by index ----------
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Without an index, pop() removes the LAST item
thislist = ["apple", "banana", "cherry"]
removed = thislist.pop()
print(thislist, "- removed:", removed)

# ---------- del keyword ----------
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# del can delete the whole list:
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist)   # NameError - the list no longer exists

# ---------- clear() - empty the list ----------
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)     # []
