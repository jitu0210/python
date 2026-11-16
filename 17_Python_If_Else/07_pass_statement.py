# ==========================================================
# THE PASS STATEMENT
# ==========================================================
# An if block cannot be empty. If you need an empty block
# (for example, as a placeholder), use `pass` to avoid an error.
a = 33
b = 200

if b > a:
    pass        # TODO: fill this in later

# pass also works in loops, functions and classes:
for i in range(3):
    pass

def future_function():
    pass

class FutureClass:
    pass

print("pass lets the program run without errors")
