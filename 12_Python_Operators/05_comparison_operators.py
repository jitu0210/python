# ==========================================================
# COMPARISON OPERATORS
# ==========================================================
# Compare two values. The result is True or False.
x = 5
y = 3

print(x == y)   # Equal                  False
print(x != y)   # Not equal              True
print(x > y)    # Greater than           True
print(x < y)    # Less than              False
print(x >= y)   # Greater than or equal  True
print(x <= y)   # Less than or equal     False

# ---------- Chaining comparisons ----------
# 1 < x < 10  is the same as  1 < x and x < 10
print(1 < x < 10)    # True
print(1 < x > 10)    # False
