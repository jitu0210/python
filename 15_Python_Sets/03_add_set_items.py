# ==========================================================
# ADD SET ITEMS
# ==========================================================

# ---------- add() - one item ----------
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# ---------- update() - items from another set ----------
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# ---------- update() works with any iterable ----------
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
