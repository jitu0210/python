# ==========================================================
# PYTHON ITERATORS
# ==========================================================
# An iterator is an object you can step through one value at a time.
# It implements the iterator protocol: __iter__() and __next__().

# ---------- Iterator vs Iterable ----------
# Lists, tuples, dicts, sets and strings are ITERABLES:
# you can get an iterator from them with iter().
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit), next(myit), next(myit))

# ---------- Looping through an iterator ----------
# A for loop creates an iterator and calls next() for you.
for x in mytuple:
    print(x)

# ---------- Create an iterator ----------
# Give your class __iter__() and __next__():
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))

# ---------- StopIteration ----------
# Raise StopIteration to end the iteration (otherwise it never ends).
class UpToTwenty:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        raise StopIteration

for x in UpToTwenty():
    print(x, end=" ")
print()
