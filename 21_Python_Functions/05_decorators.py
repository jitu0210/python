# ==========================================================
# PYTHON DECORATORS
# ==========================================================
# A decorator lets you add extra behaviour to a function WITHOUT changing
# the function's code. It is a function that takes a function and returns
# a new function.

def changecase(func):
    def wrapper():
        return func().upper()
    return wrapper

@changecase                  # same as: myfunction = changecase(myfunction)
def myfunction():
    return "Hello Sally"

print(myfunction())          # HELLO SALLY

# ---------- Reuse a decorator on many functions ----------
@changecase
def otherfunction():
    return "I am speed!"

print(otherfunction())

# ---------- Decorators with arguments (*args, **kwargs) ----------
def changecase2(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@changecase2
def greet(name):
    return "Hello " + name

print(greet("John"))

# ---------- Decorator with its own argument ----------
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()

# ---------- Multiple decorators ----------
def addgreeting(func):
    def wrapper(*args, **kwargs):
        return "Hello " + func(*args, **kwargs)
    return wrapper

@changecase2
@addgreeting               # applied first (closest to the function)
def myname(name):
    return name

print(myname("Tobias"))    # HELLO TOBIAS

# ---------- Preserving function metadata ----------
# A wrapper hides the original __name__ and docstring.
# functools.wraps copies them back:
import functools

def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logged
def add(a, b):
    """Add two numbers."""
    return a + b

print(add(2, 3))
print(add.__name__, "-", add.__doc__)
