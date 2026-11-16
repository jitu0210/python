# ==========================================================
# LIST METHODS
# ==========================================================
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")          # append()  add an element at the end
print(fruits)

copy = fruits.copy()             # copy()    return a copy
print(copy)

print(fruits.count("apple"))     # count()   number of times a value appears

fruits.extend(["kiwi", "fig"])   # extend()  add elements of an iterable
print(fruits)

print(fruits.index("cherry"))    # index()   index of the first match

fruits.insert(1, "lemon")        # insert()  add at a position
print(fruits)

fruits.pop(1)                    # pop()     remove at a position
print(fruits)

fruits.remove("fig")             # remove()  remove the first matching item
print(fruits)

fruits.reverse()                 # reverse() reverse the order
print(fruits)

fruits.sort()                    # sort()    sort the list
print(fruits)

fruits.clear()                   # clear()   remove all elements
print(fruits)
