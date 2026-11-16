# ==========================================================
# PYTHON LAMBDA
# ==========================================================
# A lambda is a small anonymous function.
# It can take any number of arguments, but has only ONE expression.
#
#   lambda arguments : expression

x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

# ---------- Why use lambda? ----------
# Lambdas shine when used as an anonymous function inside another function.
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

# ---------- Lambda with built-in functions ----------
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# map() - apply to every item
doubled = list(map(lambda n: n * 2, numbers))
print(doubled)

# filter() - keep items where the lambda returns True
odd = list(filter(lambda n: n % 2 != 0, numbers))
print(odd)

# sorted() with a key
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
print(sorted(students, key=lambda s: s[1]))

words = ["apple", "pie", "banana", "cherry"]
print(sorted(words, key=lambda w: len(w)))
