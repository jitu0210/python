# ==========================================================
# PYTHON MODULES
# ==========================================================
# A module is like a code library: a file with functions / variables
# you want to include in your program.

# ---------- Create a module ----------
# Save code in a file ending in .py -> see mymodule.py in this folder.

# ---------- Use a module ----------
import mymodule
mymodule.greeting("Jonathan")       # module_name.function_name

# ---------- Variables in a module ----------
a = mymodule.person1["age"]
print(a)

# ---------- Re-naming a module (alias) ----------
import mymodule as mx
print(mx.person1["country"])

# ---------- Built-in modules ----------
import platform
print(platform.system())

# ---------- dir() - list everything defined in a module ----------
print(dir(platform)[:10], "...")

# ---------- Import only part of a module ----------
from mymodule import person1
print(person1["name"])     # no module prefix needed now
