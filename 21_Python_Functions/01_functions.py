# ==========================================================
# PYTHON FUNCTIONS
# ==========================================================
# A function is a block of code that only runs when it is called.
# You can pass data (parameters) into it, and it can return data.

# ---------- Creating a function ----------
def my_function():
    print("Hello from a function")

# ---------- Calling a function ----------
my_function()
my_function()     # call it as many times as you like

# ---------- Function names ----------
# Same rules as variable names: start with a letter or _, then letters,
# numbers, underscores. Use descriptive snake_case names: calculate_sum()

# ---------- Why use functions? ----------
# Write the code once, reuse it many times - instead of repeating yourself.
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# ---------- Return values ----------
def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)

# A function without a return statement returns None:
def no_return():
    x = 1

print(no_return())

# ---------- pass ----------
# A function body cannot be empty; use pass as a placeholder.
def todo():
    pass
