# ==========================================================
# PYTHON NONE
# ==========================================================
# None is a special constant that means "no value" / "nothing".
# It is the only value of the NoneType type.
x = None
print(x)
print(type(x))

# ---------- Comparing with None ----------
# Use `is` (or `is not`) to check for None, not ==
result = None
if result is None:
    print("No result yet")
else:
    print("Result:", result)

result = 42
if result is not None:
    print("Result:", result)

# ---------- None is falsy ----------
print(bool(None))              # False
if not None:
    print("None counts as False in conditions")

# But None is not the same as 0, "" or False:
print(None == 0, None == "", None == False)

# ---------- Functions return None by default ----------
def greet():
    print("Hello!")

value = greet()
print("greet() returned:", value)

# ---------- None as a default parameter ----------
# A common pattern for "argument not given":
def add_item(item, items=None):
    if items is None:
        items = []          # create a NEW list each call
    items.append(item)
    return items

print(add_item("apple"))
print(add_item("banana"))
