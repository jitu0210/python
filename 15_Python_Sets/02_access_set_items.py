# ==========================================================
# ACCESS SET ITEMS
# ==========================================================
# Set items have no index, so you cannot use thisset[0].
# Instead, loop through the set or check with `in`.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

print("banana" in thisset)       # True
print("banana" not in thisset)   # False

# Once a set is created you cannot CHANGE its items,
# but you can add new items (next lesson).
