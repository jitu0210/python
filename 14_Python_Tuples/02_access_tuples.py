# ==========================================================
# ACCESS TUPLE ITEMS
# ==========================================================
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[1])       # by index
print(thistuple[-1])      # negative index
print(thistuple[2:5])     # range of indexes
print(thistuple[:4])      # from the start
print(thistuple[2:])      # to the end
print(thistuple[-4:-1])   # negative range

# Check if an item exists
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
