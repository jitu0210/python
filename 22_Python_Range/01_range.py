# ==========================================================
# PYTHON RANGE
# ==========================================================
# range() returns an immutable sequence of numbers.
# It is most often used to loop a specific number of times.
#
#   range(stop)
#   range(start, stop)
#   range(start, stop, step)
# start is included, stop is NOT included. Default start = 0, step = 1.

# ---------- One argument ----------
x = range(10)
print(list(x))           # 0..9

# ---------- Two arguments ----------
x = range(3, 10)
print(list(x))           # 3..9

# ---------- Three arguments ----------
x = range(3, 10, 2)
print(list(x))           # 3, 5, 7, 9

# Negative step - count down:
print(list(range(10, 0, -2)))

# ---------- Range in for loops ----------
for i in range(5):
    print("Loop number", i)

# ---------- Slicing a range ----------
r = range(0, 20)
print(r[5:10])            # range(5, 10)
print(list(r[5:10]))

# ---------- Membership test ----------
r = range(0, 10, 2)
print(6 in r)             # True
print(7 in r)             # False

# ---------- Length ----------
print(len(range(0, 10, 3)))   # 4

# A range uses very little memory - it does not store all numbers,
# it computes them when needed.
