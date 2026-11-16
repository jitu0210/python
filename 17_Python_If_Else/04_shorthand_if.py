# ==========================================================
# SHORTHAND IF
# ==========================================================
a = 200
b = 33

# ---------- Short hand if: one statement on the same line ----------
if a > b: print("a is greater than b")

# ---------- Short hand if ... else (ternary / conditional expression) ----------
print("A") if a > b else print("B")

# Assign a value with it:
bigger = a if a > b else b
print("Bigger:", bigger)

# ---------- Several conditions on one line ----------
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
