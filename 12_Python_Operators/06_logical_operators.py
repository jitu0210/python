# ==========================================================
# LOGICAL OPERATORS
# ==========================================================
x = 5

# and -> True if BOTH statements are true
print(x > 3 and x < 10)          # True

# or  -> True if ONE of the statements is true
print(x > 3 or x < 4)            # True

# not -> reverses the result
print(not(x > 3 and x < 10))     # False

# Example with variables:
age = 25
has_ticket = True
if age >= 18 and has_ticket:
    print("You may enter")
