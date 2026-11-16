# ==========================================================
# PYTHON IF
# ==========================================================
# Conditions use the comparison operators:
#   a == b   a != b   a < b   a <= b   a > b   a >= b
# They are most often used in if statements and loops.

a = 33
b = 200
if b > a:
    print("b is greater than a")

# ---------- Indentation ----------
# Python uses indentation to define the body of the if statement.
# if b > a:
# print("b is greater than a")   # IndentationError

# ---------- Several statements in the block ----------
age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")

# ---------- Boolean variables in if ----------
is_logged_in = True
if is_logged_in:
    print("Welcome back!")
