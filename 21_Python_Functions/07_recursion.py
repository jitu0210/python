# ==========================================================
# PYTHON RECURSION
# ==========================================================
# Recursion = a function that calls itself.
# Every recursive function needs:
#   - a BASE CASE that stops the recursion
#   - a RECURSIVE CASE that moves toward the base case
# Without a base case it would run until Python raises RecursionError.

def countdown(n):
    if n <= 0:                # base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1)      # recursive case

countdown(5)

# ---------- Factorial: 5! = 5*4*3*2*1 ----------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))     # 120

# ---------- Fibonacci ----------
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])

# ---------- Recursion with lists ----------
def sum_list(items):
    if len(items) == 0:
        return 0
    return items[0] + sum_list(items[1:])

print(sum_list([1, 2, 3, 4, 5]))

def find_max(items):
    if len(items) == 1:
        return items[0]
    rest = find_max(items[1:])
    return items[0] if items[0] > rest else rest

print(find_max([3, 7, 2, 9, 1]))

# ---------- Recursion depth limit ----------
import sys
print("Default recursion limit:", sys.getrecursionlimit())
# For very deep problems a loop is usually better than recursion.
