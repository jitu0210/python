# ==========================================================
# COPY LISTS
# ==========================================================
# You cannot copy a list with list2 = list1:
# list2 is only a REFERENCE, changes to list1 also show up in list2.
list1 = ["apple", "banana"]
list2 = list1
list1.append("cherry")
print(list2)          # ['apple', 'banana', 'cherry']

# ---------- copy() method ----------
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# ---------- list() constructor ----------
mylist = list(thislist)
print(mylist)

# ---------- Slice operator ----------
mylist = thislist[:]
print(mylist)

# Now changes do not affect the copy:
thislist.append("kiwi")
print(thislist, mylist)
