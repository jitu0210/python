# ==========================================================
# PYTHON USER INPUT
# ==========================================================
# input() asks the user for input and waits until they press Enter.
# The program stops at input() until the user responds.

username = input("Enter username: ")
print("Username is: " + username)

# ---------- Using a prompt ----------
name = input("Enter your name: ")
print(f"Hello {name}")

# ---------- input() always returns a STRING ----------
# Convert it if you need a number:
age = input("Enter your age: ")
print(type(age))                     # <class 'str'>

try:
    age = int(age)
    print("Next year you will be", age + 1)
except ValueError:
    print("That was not a whole number")

# ---------- Validate input: keep asking until it is valid ----------
while True:
    num = input("Enter a number between 1 and 10: ")
    if num.isdigit() and 1 <= int(num) <= 10:
        print("Thanks! You entered", num)
        break
    print("Wrong input, try again.")
