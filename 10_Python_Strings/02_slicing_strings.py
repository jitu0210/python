# ==========================================================
# SLICING STRINGS
# ==========================================================
# Return a range of characters with  string[start:end]
# start is INCLUDED, end is NOT included.
b = "Hello, World!"
print(b[2:5])     # llo

# ---------- Slice from the start ----------
print(b[:5])      # Hello

# ---------- Slice to the end ----------
print(b[2:])      # llo, World!

# ---------- Negative indexing ----------
# Count from the end of the string (-1 is the last character)
print(b[-5:-2])   # orl

# ---------- Step ----------
print(b[::2])     # every second character
print(b[::-1])    # reversed string
