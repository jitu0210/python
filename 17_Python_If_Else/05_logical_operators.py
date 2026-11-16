# ==========================================================
# IF WITH LOGICAL OPERATORS
# ==========================================================
a = 200
b = 33
c = 500

# and - both conditions must be true
if a > b and c > a:
    print("Both conditions are True")

# or - at least one condition must be true
if a > b or a > c:
    print("At least one of the conditions is True")

# not - reverses the result
if not a > b:
    print("a is NOT greater than b")
else:
    print("a is greater than b")

# Combining them (use parentheses for clarity):
age = 25
is_student = False
has_coupon = True
if age < 26 and (is_student or has_coupon):
    print("You get a discount")
