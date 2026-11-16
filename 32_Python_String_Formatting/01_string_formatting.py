# ==========================================================
# PYTHON STRING FORMATTING
# ==========================================================

# ---------- F-Strings (preferred, Python 3.6+) ----------
txt = f"The price is 49 dollars"
print(txt)

# ---------- Placeholders and modifiers ----------
price = 59
print(f"The price is {price} dollars")
print(f"The price is {price:.2f} dollars")          # 2 decimals
print(f"The price is {95:.2f} dollars")             # a literal value

# ---------- Perform operations ----------
print(f"The price is {20 * 59} dollars")

price = 59
tax = 0.25
print(f"The price is {price + (price * tax)} dollars")

# if...else inside the placeholder
print(f"It is very {'Expensive' if price > 50 else 'Cheap'}")

# ---------- Execute functions ----------
fruit = "apples"
print(f"I love {fruit.upper()}")

def myconverter(x):
    return x * 0.3048

print(f"The plane is flying at a {myconverter(30000)} meter altitude")

# ---------- More modifiers ----------
price = 59000
print(f"The price is {price:,} dollars")    # thousand separator
print(f"{'left':<10}|")                     # left align in 10 spaces
print(f"{'right':>10}|")                    # right align
print(f"{'center':^10}|")                   # center
print(f"{0.25:%}  {0.25:.0%}")              # percentage
print(f"{255:b} {255:o} {255:x} {255:X}")   # binary, octal, hex
print(f"{12345.678:e}")                     # scientific
print(f"{42:05d}")                          # pad with zeros

# ---------- String format() ----------
# The older way, still widely used:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple values
quantity, itemno, price = 3, 567, 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index numbers
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age, name = 36, "Ravi"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
