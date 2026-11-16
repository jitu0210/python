# ==========================================================
# __repr__
# ==========================================================
# __repr__ returns an unambiguous, developer-friendly string -
# ideally one that looks like the code to re-create the object.
# Used by repr(), the interactive shell, and inside lists.

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __repr__(self):
        return f"Book({self.title!r}, {self.pages})"

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

b = Book("Python Basics", 250)
print(repr(b))          # Book('Python Basics', 250)
print(b)                # uses __str__
print([b, Book("Advanced Python", 400)])   # lists show __repr__

# If only __repr__ is defined, print() falls back to it.
