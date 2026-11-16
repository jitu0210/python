# ==========================================================
# PYTHON FOR LOOPS
# ==========================================================
# A for loop iterates over a sequence (list, tuple, dict, set, string).
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# ---------- Looping through a string ----------
for x in "banana":
    print(x)

# ---------- break ----------
for x in fruits:
    print(x)
    if x == "banana":
        break

# break before print:
for x in fruits:
    if x == "banana":
        break
    print(x)

# ---------- continue ----------
for x in fruits:
    if x == "banana":
        continue
    print(x)

# ---------- range() ----------
for x in range(6):          # 0..5
    print(x)
for x in range(2, 6):       # 2..5
    print(x)
for x in range(2, 30, 3):   # step 3
    print(x)

# ---------- else in a for loop ----------
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# else does NOT run if the loop was stopped by break:
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")   # not printed

# ---------- Nested loops ----------
adj = ["red", "big", "tasty"]
for a in adj:
    for f in fruits:
        print(a, f)

# ---------- pass ----------
for x in [0, 1, 2]:
    pass
