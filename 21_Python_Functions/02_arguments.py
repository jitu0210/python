# ==========================================================
# PYTHON FUNCTION ARGUMENTS
# ==========================================================
# Information passed into a function = arguments.
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")

# Parameter = the variable in the definition (fname)
# Argument  = the value sent when calling ("Emil")

# ---------- Number of arguments ----------
# Must match the number of parameters, unless defaults are given.
def full_name(fname, lname):
    print(fname + " " + lname)

full_name("Emil", "Refsnes")
# full_name("Emil")      # TypeError: missing 1 required argument

# ---------- Default parameter values ----------
def my_country(country="Norway"):
    print("I am from " + country)

my_country("Sweden")
my_country()             # uses the default

# ---------- Keyword arguments ----------
# key = value syntax; the order does not matter.
def kids(child3, child2, child1):
    print("The youngest child is " + child3)

kids(child1="Emil", child2="Tobias", child3="Linus")

# ---------- Positional + keyword ----------
# Positional arguments must come BEFORE keyword arguments.
def describe(animal, name):
    print(f"I have a {animal} called {name}")

describe("dog", name="Buddy")

# ---------- Passing different data types ----------
def show_items(food):
    for x in food:
        print(x)

show_items(["apple", "banana", "cherry"])

# ---------- Return values ----------
def times5(x):
    return 5 * x

print(times5(3))

# ---------- Positional-only arguments  ( , / ) ----------
def pos_only(x, /):
    print(x)

pos_only(3)
# pos_only(x=3)   # TypeError

# ---------- Keyword-only arguments  ( *, ) ----------
def kw_only(*, x):
    print(x)

kw_only(x=3)
# kw_only(3)      # TypeError

# ---------- Combining both ----------
def combined(a, b, /, *, c, d):
    print(a + b + c + d)

combined(5, 6, c=7, d=8)
