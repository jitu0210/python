# ==========================================================
# FORMAT STRINGS
# ==========================================================
# We cannot combine strings and numbers with +
age = 36
# txt = "My name is Ravi, I am " + age    # TypeError

# ---------- F-Strings (Python 3.6+) ----------
# Put an f before the string and {placeholders} inside it.
txt = f"My name is Ravi, I am {age}"
print(txt)

# ---------- Placeholders and modifiers ----------
price = 59
print(f"The price is {price} dollars")

# Modifier :.2f -> fixed point with 2 decimals
print(f"The price is {price:.2f} dollars")

# Placeholders can hold expressions / math / function calls
print(f"The price is {20 * 59} dollars")
