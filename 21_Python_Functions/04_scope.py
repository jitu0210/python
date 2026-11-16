# ==========================================================
# PYTHON SCOPE
# ==========================================================
# A variable is only available inside the region where it is created.
# That region is called its scope.

# ---------- Local scope ----------
def myfunc():
    x = 300           # local to myfunc
    print(x)

myfunc()

# ---------- Function inside a function ----------
# The inner function can read the outer function's variables.
def outer():
    x = 300
    def inner():
        print(x)
    inner()

outer()

# ---------- Global scope ----------
x = 300               # global

def myfunc2():
    print(x)          # can read the global

myfunc2()
print(x)

# ---------- Naming variables ----------
# Same name inside and outside a function = two different variables.
x = 300

def myfunc3():
    x = 200
    print(x)          # 200 (local)

myfunc3()
print(x)              # 300 (global)

# ---------- global keyword ----------
def myfunc4():
    global y
    y = 300

myfunc4()
print(y)

x = 300
def myfunc5():
    global x
    x = 200

myfunc5()
print(x)              # 200

# ---------- nonlocal keyword ----------
# Use the variable from the OUTER function (not global).
def myfunc6():
    x = "Jane"
    def myfunc7():
        nonlocal x
        x = "hello"
    myfunc7()
    return x

print(myfunc6())      # hello

# ---------- The LEGB rule ----------
# Python looks up names in this order:
#   L - Local        (inside the current function)
#   E - Enclosing    (inside enclosing functions)
#   G - Global       (module level)
#   B - Built-in     (print, len, ...)
