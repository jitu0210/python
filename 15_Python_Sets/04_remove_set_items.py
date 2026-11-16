# ==========================================================
# REMOVE SET ITEMS
# ==========================================================

# ---------- remove() ----------
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# remove() raises an error if the item does not exist.

# ---------- discard() ----------
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
thisset.discard("not-there")     # no error
print(thisset)

# ---------- pop() ----------
# Removes a RANDOM item (sets are unordered) and returns it.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print("removed:", x)
print(thisset)

# ---------- clear() ----------
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)       # set()

# ---------- del ----------
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)     # NameError
