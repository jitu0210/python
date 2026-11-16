# ==========================================================
# MEMBERSHIP OPERATORS
# ==========================================================
# Test whether a sequence contains a value.
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)        # True
print("pineapple" not in fruits) # True

# Works with strings too:
text = "Hello World"
print("H" in text)               # True
print("hello" in text)           # False (case-sensitive)
print("z" not in text)           # True

# With dictionaries, `in` checks the KEYS:
person = {"name": "Ravi", "age": 36}
print("name" in person)          # True
