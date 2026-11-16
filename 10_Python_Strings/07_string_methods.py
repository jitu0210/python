# ==========================================================
# STRING METHODS
# ==========================================================
# All string methods return NEW values; the original string is unchanged.
t = "hello, welcome to my world."

print(t.capitalize())              # first character upper case
print(t.casefold())                # lower case (aggressive)
print(t.center(35, "*"))           # centered string
print(t.count("o"))                # times a value occurs
print(t.encode())                  # encoded version (bytes)
print(t.endswith("."))             # ends with value?
print("H\te\tl".expandtabs(4))     # set tab size
print(t.find("welcome"))           # position, -1 if not found
print("{} is {}".format("Ravi", 36))  # format values
print(t.index("welcome"))          # like find(), but error if missing
print("abc123".isalnum())          # all alphanumeric?
print("abc".isalpha())             # all letters?
print("abc".isascii())             # all ASCII?
print("2".isdecimal())             # all decimals?
print("12".isdigit())              # all digits?
print("my_var".isidentifier())     # valid identifier?
print("abc".islower())             # all lower case?
print("12".isnumeric())            # all numeric?
print("Hi!".isprintable())         # all printable?
print("   ".isspace())             # all whitespace?
print("Hello World".istitle())     # title case?
print("ABC".isupper())             # all upper case?
print("-".join(["a", "b", "c"]))   # join an iterable
print("hi".ljust(10, ".") + "|")   # left justified
print("HeLLo".lower())             # lower case
print("  hi".lstrip())             # left trim
tbl = str.maketrans("a", "4")      # translation table
print("banana".translate(tbl))     # translate using table
print(t.partition("welcome"))      # split into 3-part tuple
print(t.replace("world", "home"))  # replace
print(t.rfind("o"))                # last position
print(t.rindex("o"))               # last position (error if missing)
print("hi".rjust(10, ".")) # right justified
print(t.rpartition("o"))           # partition at last occurrence
print("a,b,c".rsplit(",", 1))      # split from the right
print("hi  ".rstrip() + "|")       # right trim
print("a,b,c".split(","))          # split
print("line1\nline2".splitlines())  # split at line breaks
print(t.startswith("hello"))       # starts with value?
print("  hi  ".strip())            # trim both sides
print("HeLLo".swapcase())          # swap case
print(t.title())                   # first letter of each word upper
print(t.upper())                   # upper case
print("42".zfill(5))               # fill with zeros at the start
