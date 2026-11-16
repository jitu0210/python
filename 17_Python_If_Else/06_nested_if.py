# ==========================================================
# NESTED IF
# ==========================================================
# An if statement inside another if statement.
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# Practical example:
username = "admin"
password = "1234"
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Unknown user")
