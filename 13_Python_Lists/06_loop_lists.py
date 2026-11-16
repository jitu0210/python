# ==========================================================
# LOOP LISTS
# ==========================================================
thislist = ["apple", "banana", "cherry"]

# ---------- for loop ----------
for x in thislist:
    print(x)

# ---------- Loop through the index numbers ----------
# range(len(...)) gives 0, 1, 2 ...
for i in range(len(thislist)):
    print(i, thislist[i])

# ---------- while loop ----------
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# ---------- Looping with list comprehension ----------
# A short way to loop (more in the next lesson):
[print(x) for x in thislist]

# ---------- enumerate() - index and value together ----------
for index, fruit in enumerate(thislist):
    print(index, fruit)
