# ==========================================================
# PYTHON VARIABLES
# ==========================================================
# Variables are containers for storing data values.

# ---------- Creating variables ----------
# There is no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x = 5
y = "Ravi"
print(x)
print(y)

# Variables don't need a declared type, and can even change type:
x = 4        # x is an int
x = "Sita"   # x is now a str
print(x)

# ---------- Casting ----------
# Choose the data type yourself:
a = str(3)    # '3'
b = int(3)    # 3
c = float(3)  # 3.0
print(a, b, c)

# ---------- Get the type ----------
print(type(b))
print(type(y))

# ---------- Single or double quotes? ----------
name = "Ravi"
name = 'Ravi'     # exactly the same

# ---------- Case-sensitive ----------
age = 4
Age = "Old"       # Age does NOT overwrite age
print(age, Age)
