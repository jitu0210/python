# ==========================================================
# PYTHON STRINGS
# ==========================================================
# Strings are surrounded by single or double quotes. 'hello' == "hello"
print("Hello")
print('Hello')

# ---------- Quotes inside quotes ----------
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# ---------- Assign a string to a variable ----------
a = "Hello"
print(a)

# ---------- Multiline strings ----------
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor."""
print(a)

# ---------- Strings are arrays ----------
# A string is an array of characters. Square brackets access an element.
# (Python has no separate "character" type - a character is a string of length 1.)
a = "Hello, World!"
print(a[1])          # e  (first position is 0)

# ---------- Looping through a string ----------
for ch in "banana":
    print(ch)

# ---------- String length ----------
print(len(a))

# ---------- Check string ----------
txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
    print("Yes, 'free' is present.")

# ---------- Check if NOT ----------
print("expensive" not in txt)
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
