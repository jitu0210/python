# ==========================================================
# SORT LISTS
# ==========================================================

# ---------- Sort alphanumerically (ascending) ----------
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# ---------- Sort descending ----------
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

# ---------- Customize sort with key= ----------
# Sort by how close each number is to 50:
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# ---------- Case-insensitive sort ----------
# By default capital letters come before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist.sort(key=str.lower)
print(thislist)

# ---------- Reverse order ----------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# sorted() returns a NEW sorted list and leaves the original unchanged
nums = [3, 1, 2]
print(sorted(nums), nums)
