# ==========================================================
# TERNARY OPERATOR (conditional expression)
# ==========================================================
# Write a simple if/else on ONE line:
#     value_if_true if condition else value_if_false

a = 2
b = 330
print("A") if a > b else print("B")

# Most often used to assign a value:
age = 20
status = "adult" if age >= 18 else "minor"
print(status)

# Several conditions can be chained (keep it readable!):
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Choosing the larger of two numbers:
x, y = 15, 20
bigger = x if x > y else y
print("Bigger:", bigger)
