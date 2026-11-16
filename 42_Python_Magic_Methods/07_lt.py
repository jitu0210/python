# ==========================================================
# __lt__
# ==========================================================
# __lt__ defines < (less than). With it, sorted() and min()/max()
# can work on your objects.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __lt__(self, other):
        return self.grade < other.grade

    def __repr__(self):
        return f"{self.name}:{self.grade}"

a = Student("Emil", 85)
b = Student("Tobias", 92)
print(a < b)            # True
print(b > a)            # True - Python flips it and uses __lt__

students = [b, Student("Linus", 78), a]
print(sorted(students))
print(min(students), max(students))

# Related: __le__ <=   __gt__ >   __ge__ >=
