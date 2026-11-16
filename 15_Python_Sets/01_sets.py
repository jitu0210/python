# ==========================================================
# PYTHON SETS
# ==========================================================
# A set stores multiple items using curly brackets.
# Sets are UNORDERED, items are UNCHANGEABLE*, and UNINDEXED.
# (*you can't change an item, but you can remove items and add new ones)
thisset = {"apple", "banana", "cherry"}
print(thisset)        # the order may be different each time!

# ---------- Duplicates not allowed ----------
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True and 1 are considered the same value (also False and 0):
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# ---------- Length ----------
print(len(thisset))

# ---------- Data types ----------
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False}
set4 = {"abc", 34, True, 40, "male"}
print(set1, set2, set3, set4)
print(type(set1))

# ---------- set() constructor ----------
thisset = set(("apple", "banana", "cherry"))   # double round brackets
print(thisset)

# Note: {} creates an empty DICTIONARY - use set() for an empty set
empty = set()
print(type(empty))
