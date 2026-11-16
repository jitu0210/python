# ==========================================================
# PYTHON ELSE
# ==========================================================
# else catches anything not caught by the previous conditions.
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# else without elif:
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Even / odd check:
number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
