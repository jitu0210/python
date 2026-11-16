# ==========================================================
# GLOBAL VARIABLES
# ==========================================================
# Variables created OUTSIDE of a function are global variables.
# They can be used everywhere, inside and outside functions.

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# A variable with the same name created INSIDE a function is local.
# The global variable keeps its original value.
x = "awesome"

def myfunc2():
    x = "fantastic"           # local
    print("Python is " + x)

myfunc2()
print("Python is " + x)       # still "awesome"

# ---------- The global keyword ----------
# Use `global` to create a global variable inside a function:
def myfunc3():
    global y
    y = "brilliant"

myfunc3()
print("Python is " + y)

# ...or to CHANGE a global variable inside a function:
x = "awesome"

def myfunc4():
    global x
    x = "fantastic"

myfunc4()
print("Python is " + x)       # now "fantastic"
