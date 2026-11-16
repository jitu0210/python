# ==========================================================
# *args AND **kwargs
# ==========================================================

# ---------- *args - arbitrary positional arguments ----------
# If you don't know how many arguments will be passed, add * before the
# parameter name. The function receives a TUPLE of arguments.
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def add_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40, 50))

# Regular parameters + *args:
def greet(greeting, *names):
    for name in names:
        print(greeting, name)

greet("Hello", "Emil", "Tobias", "Linus")

# ---------- **kwargs - arbitrary keyword arguments ----------
# Add ** before the parameter name; the function receives a DICTIONARY.
def my_function2(**kid):
    print("His last name is " + kid["lname"])

my_function2(fname="Tobias", lname="Refsnes")

def show_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_info(name="Ravi", age=36, city="Delhi")

# ---------- Combining them ----------
# Order: regular params, *args, then **kwargs
def everything(title, *args, **kwargs):
    print("title:", title)
    print("args:", args)
    print("kwargs:", kwargs)

everything("Demo", 1, 2, 3, color="red", size="L")

# ---------- Unpacking when CALLING ----------
def add3(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add3(*nums))                # list -> positional arguments

values = {"a": 1, "b": 2, "c": 3}
print(add3(**values))             # dict -> keyword arguments
