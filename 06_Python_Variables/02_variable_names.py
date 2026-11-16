# ==========================================================
# VARIABLE NAMES
# ==========================================================
# A variable can have a short name (x, y) or a descriptive one (car_name).
# Rules:
#   - must start with a letter or the underscore _
#   - cannot start with a number
#   - can only contain letters, numbers and underscores (A-z, 0-9, _)
#   - names are case-sensitive (age, Age and AGE are three variables)
#   - cannot be a Python keyword (if, for, while, class, def, ...)

# Legal names:
myvar = "Ravi"
my_var = "Ravi"
_my_var = "Ravi"
myVar = "Ravi"
MYVAR = "Ravi"
myvar2 = "Ravi"

# Illegal names (would cause SyntaxError):
# 2myvar = "Ravi"
# my-var = "Ravi"
# my var = "Ravi"

# ---------- Multi-word variable names ----------
# Camel case: each word except the first starts with a capital
myVariableName = "Camel"
# Pascal case: each word starts with a capital
MyVariableName = "Pascal"
# Snake case: words separated by underscores (most common in Python)
my_variable_name = "Snake"

print(myVariableName, MyVariableName, my_variable_name)
