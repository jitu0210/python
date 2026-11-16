# ==========================================================
# PYTHON ELIF
# ==========================================================
# elif = "if the previous conditions were not true, try this one"
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# You can have as many elif blocks as you need:
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
# Python stops at the FIRST true condition.
