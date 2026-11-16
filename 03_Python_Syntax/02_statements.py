# ==========================================================
# PYTHON STATEMENTS
# ==========================================================
# A computer program is a list of instructions.
# In Python each instruction is called a STATEMENT.

print("Python is fun!")          # one statement

# Most programs contain many statements, executed one by one, top to bottom:
print("Line one")
print("Line two")
print("Line three")

# ---------- Semicolons ----------
# Python statements end at the end of the line - no semicolon is needed.
# You CAN use semicolons to put several statements on one line:
print("A"); print("B"); print("C")
# ...but it is not recommended, it makes code harder to read.

# ---------- Long statements ----------
# Statements can continue over several lines inside brackets ( ) [ ] { }
total = (1 + 2 + 3 +
         4 + 5 + 6)
print(total)

# ...or with a backslash at the end of the line
total = 10 + \
        20
print(total)
