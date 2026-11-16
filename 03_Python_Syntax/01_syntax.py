# ==========================================================
# PYTHON SYNTAX
# ==========================================================

# ---------- Execute Python syntax ----------
# You can run code in the interactive shell (>>> print("Hi"))
# or save it in a .py file and run: python 01_syntax.py

# ---------- Python Indentation ----------
# Indentation = the spaces at the beginning of a code line.
# In other languages it is only for readability; in Python it is REQUIRED,
# because it tells Python which lines belong to a block.

if 5 > 2:
    print("Five is greater than two!")

# Missing indentation -> IndentationError:
# if 5 > 2:
# print("Five is greater than two!")

# You choose how many spaces (4 is the convention, at least 1 is required)
if 5 > 2:
 print("One space works")
if 5 > 2:
        print("Eight spaces work too")

# But inside ONE block you must use the same amount:
# if 5 > 2:
#     print("four spaces")
#         print("eight spaces")   # IndentationError

# ---------- Python Variables ----------
# Variables are created when you assign a value (no declaration command)
x = 5
y = "Hello, World!"
print(x, y)

# ---------- Comments ----------
# A line starting with # is a comment and is ignored by Python.
print("Syntax lesson finished")
