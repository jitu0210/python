# ==========================================================
# JOIN SETS
# ==========================================================
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# ---------- union() / | - all items from both ----------
set3 = set1.union(set2)
print(set3)
print(set1 | set2)

# Join many sets:
set4 = {"John", "Elena"}
print(set1.union(set2, set4))
print(set1 | set2 | set4)

# union() also accepts lists/tuples (the | operator does not):
print({"a", "b"}.union([1, 2], (3,)))

# ---------- update() - add items into the existing set ----------
set1 = {"a", "b", "c"}
set1.update(set2)
print(set1)
# union() and update() both drop duplicates.

# ---------- intersection() / & - only items in BOTH ----------
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1.intersection(set2))
print(set1 & set2)
set1.intersection_update(set2)   # keep only the duplicates in set1
print(set1)

# ---------- difference() / - - items in the first set only ----------
set1 = {"apple", "banana", "cherry"}
print(set1.difference(set2))
print(set1 - set2)
set1.difference_update(set2)
print(set1)

# ---------- symmetric_difference() / ^ - items NOT in both ----------
set1 = {"apple", "banana", "cherry"}
print(set1.symmetric_difference(set2))
print(set1 ^ set2)
set1.symmetric_difference_update(set2)
print(set1)
