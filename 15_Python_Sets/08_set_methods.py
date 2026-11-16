# ==========================================================
# SET METHODS
# ==========================================================
s = {"apple", "banana"}

s.add("cherry")                        # add()
print(s)
c = s.copy()                           # copy()
print(c)
print({1, 2, 3}.difference({2}))       # difference()            -
x = {1, 2, 3}; x.difference_update({2}); print(x)   # difference_update()  -=
s.discard("banana")                    # discard()
print(s)
print({1, 2}.intersection({2, 3}))     # intersection()          &
x = {1, 2}; x.intersection_update({2, 3}); print(x) # intersection_update() &=
print({1, 2}.isdisjoint({3}))          # isdisjoint()
print({1}.issubset({1, 2}))            # issubset()              <=
print({1, 2} < {1, 2, 3})              # proper subset           <
print({1, 2}.issuperset({1}))          # issuperset()            >=
print({1, 2, 3} > {1})                 # proper superset         >
x = {1, 2}; x.pop(); print(x)          # pop()     remove a random item
x = {1, 2}; x.remove(1); print(x)      # remove()
print({1, 2}.symmetric_difference({2, 3}))   # symmetric_difference()  ^
x = {1, 2}; x.symmetric_difference_update({2, 3}); print(x)  # ^=
print({1}.union({2}))                  # union()                 |
x = {1}; x.update([2, 3]); print(x)    # update()                |=
s.clear()                              # clear()
print(s)
