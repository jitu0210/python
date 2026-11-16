# ==========================================================
# PYTHON GENERATORS
# ==========================================================
# A generator is a function that returns an iterator. It uses `yield`
# to produce values ONE AT A TIME, pausing between them.
# Values are created only when needed -> very memory efficient.

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

# ---------- yield keyword ----------
# yield returns a value and PAUSES the function; the next request
# continues right after the yield.
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)

# ---------- Generators save memory ----------
# This does not build a list of a million numbers in memory:
def large_sequence(n):
    for i in range(n):
        yield i

gen = large_sequence(1_000_000)
print(next(gen))
print(next(gen))
print(next(gen))

# ---------- next() ----------
def simple():
    yield "Emil"
    yield "Tobias"

g = simple()
print(next(g))
print(next(g))
# next(g) now would raise StopIteration

# ---------- Generator expressions ----------
# Like a list comprehension, but with ( ) - creates a generator.
squares_list = [x * x for x in range(5)]     # list
squares_gen = (x * x for x in range(5))      # generator
print(squares_list)
print(squares_gen)
print(sum(x * x for x in range(5)))          # handy inside functions

# ---------- Fibonacci generator ----------
def fibonacci():
    a, b = 0, 1
    while True:              # infinite, but values are made one at a time
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(10)])

# ---------- Generator methods ----------
# send() - send a value back into the generator
def echo():
    while True:
        received = yield
        print("Received:", received)

e = echo()
next(e)            # start the generator
e.send("Hello")
e.send("World")

# close() - stop the generator
def numbers():
    try:
        yield 1
        yield 2
    finally:
        print("Generator closed")

n = numbers()
print(next(n))
n.close()
