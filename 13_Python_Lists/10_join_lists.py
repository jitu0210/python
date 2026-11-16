# ==========================================================
# JOIN LISTS
# ==========================================================
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# ---------- + operator ----------
list3 = list1 + list2
print(list3)

# ---------- append items one by one ----------
list1 = ["a", "b", "c"]
for x in list2:
    list1.append(x)
print(list1)

# ---------- extend() ----------
list1 = ["a", "b", "c"]
list1.extend(list2)
print(list1)
