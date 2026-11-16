# ==========================================================
# UNPACK TUPLES
# ==========================================================
# Creating a tuple = "packing" values into it:
fruits = ("apple", "banana", "cherry")

# Extracting the values into variables = "unpacking":
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# ---------- Using an asterisk * ----------
# If there are fewer variables than values, * collects the rest into a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green, yellow, red)

# The * can be on any variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green, tropic, red)
