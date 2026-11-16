# ==========================================================
# FROZENSET
# ==========================================================
# A frozenset is an IMMUTABLE version of a set.
# Its items cannot be added or removed after creation.
# Because it is immutable, it can be used as a dictionary key
# or as an element inside another set.

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# x.add("orange")   # AttributeError - frozensets cannot change

# ---------- Frozenset methods (they all return new objects) ----------
a = frozenset({1, 2, 3})
b = frozenset({3, 4})
print(a.copy())                  # copy()
print(a.difference(b))           # difference()        a - b
print(a.intersection(b))         # intersection()      a & b
print(a.isdisjoint(b))           # isdisjoint()
print(frozenset({1}).issubset(a))   # issubset()       <=
print(a.issuperset({1, 2}))      # issuperset()        >=
print(a.symmetric_difference(b)) # symmetric_difference()  a ^ b
print(a.union(b))                # union()             a | b

# As a dictionary key:
distances = {frozenset({"Delhi", "Agra"}): 233}
print(distances[frozenset({"Agra", "Delhi"})])
