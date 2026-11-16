# ==========================================================
# MODIFY STRINGS
# ==========================================================
# Python has built-in methods for working with strings.
# (Strings are immutable - methods RETURN a new string.)

a = "Hello, World!"

# Upper case
print(a.upper())

# Lower case
print(a.lower())

# Remove whitespace at the beginning/end
b = "   Hello, World!   "
print(b.strip())

# Replace a string with another string
print(a.replace("H", "J"))

# Split a string into a list, using a separator
print(a.split(","))     # ['Hello', ' World!']
