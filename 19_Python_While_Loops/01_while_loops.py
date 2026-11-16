# ==========================================================
# PYTHON WHILE LOOPS
# ==========================================================
# Python has two loop commands: while and for.
# A while loop runs as long as its condition is true.

i = 1
while i < 6:
    print(i)
    i += 1          # don't forget this, or the loop runs forever!

# ---------- break - stop the loop ----------
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# ---------- continue - skip to the next iteration ----------
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# ---------- else - runs once when the condition becomes false ----------
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
