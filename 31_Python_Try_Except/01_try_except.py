# ==========================================================
# PYTHON TRY ... EXCEPT
# ==========================================================
#   try     - test a block of code for errors
#   except  - handle the error
#   else    - run code when there was NO error
#   finally - run code no matter what

# ---------- Exception handling ----------
# Without try, an error stops the program. With try, we can handle it:
try:
    print(undefined_variable)
except:
    print("An exception occurred")

# ---------- Many exceptions ----------
try:
    print(undefined_variable)
except NameError:
    print("Variable is not defined")
except:
    print("Something else went wrong")

# ---------- else ----------
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# ---------- finally ----------
try:
    print(undefined_variable)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# finally is useful for closing resources:
import os, tempfile
path = os.path.join(tempfile.gettempdir(), "demo_try.txt")
f = open(path, "w")
try:
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()
    os.remove(path)

# ---------- Getting the error message ----------
try:
    10 / 0
except ZeroDivisionError as e:
    print("Error:", e)

# ---------- Raise an exception ----------
x = -1
try:
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except Exception as e:
    print(e)

x = "hello"
try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
except TypeError as e:
    print(e)
