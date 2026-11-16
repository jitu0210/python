# ==========================================================
# LIST COMPREHENSION
# ==========================================================
# A shorter syntax to create a new list based on an existing one.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Without list comprehension:
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# With list comprehension - one line:
newlist = [x for x in fruits if "a" in x]
print(newlist)

# ---------- The syntax ----------
#   newlist = [expression for item in iterable if condition == True]
# The original list is left unchanged.

# ---------- Condition ----------
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in fruits]          # no condition -> copy
print(newlist)

# ---------- Iterable ----------
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)

# ---------- Expression ----------
newlist = [x.upper() for x in fruits]
print(newlist)
newlist = ["hello" for x in fruits]
print(newlist)

# The expression can contain a condition (like a filter that changes values):
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
