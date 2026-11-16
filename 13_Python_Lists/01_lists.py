# ==========================================================
# PYTHON LISTS
# ==========================================================
# Lists store multiple items in a single variable, using square brackets.
mylist = ["apple", "banana", "cherry"]
print(mylist)

# ---------- List items ----------
# Items are ORDERED, CHANGEABLE, and ALLOW DUPLICATES.
# Items are indexed: the first item is [0], the second [1], ...

# Ordered: items have a defined order that won't change (new items go at the end).
# Changeable: we can change, add and remove items after creation.
# Allow duplicates:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# ---------- List length ----------
print(len(thislist))

# ---------- Data types ----------
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]   # mixed types are fine
print(list1, list2, list3, list4)

# ---------- type() ----------
print(type(mylist))          # <class 'list'>

# ---------- The list() constructor ----------
thislist = list(("apple", "banana", "cherry"))   # note the double brackets
print(thislist)

# ---------- Python collections (arrays) ----------
#   List       - ordered, changeable, duplicates allowed
#   Tuple      - ordered, unchangeable, duplicates allowed
#   Set        - unordered, items unchangeable (but add/remove ok), no duplicates
#   Dictionary - ordered*, changeable, no duplicate keys
#   (*ordered since Python 3.7)
