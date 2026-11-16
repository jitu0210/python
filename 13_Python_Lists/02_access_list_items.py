# ==========================================================
# ACCESS LIST ITEMS
# ==========================================================
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# ---------- Access by index ----------
print(thislist[1])        # banana  (first item has index 0)

# ---------- Negative indexing ----------
print(thislist[-1])       # mango   (-1 = last item)

# ---------- Range of indexes ----------
print(thislist[2:5])      # items 2, 3, 4  (end not included)
print(thislist[:4])       # from the beginning to index 3
print(thislist[2:])       # from index 2 to the end

# ---------- Range of negative indexes ----------
print(thislist[-4:-1])    # orange, kiwi, melon

# ---------- Check if an item exists ----------
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
