# ==========================================================
# PYTHON DATA TYPES
# ==========================================================
# Variables store data of different types. Built-in types:
#   Text Type:       str
#   Numeric Types:   int, float, complex
#   Sequence Types:  list, tuple, range
#   Mapping Type:    dict
#   Set Types:       set, frozenset
#   Boolean Type:    bool
#   Binary Types:    bytes, bytearray, memoryview
#   None Type:       NoneType

# ---------- Getting the data type ----------
x = 5
print(type(x))

# ---------- Setting the data type ----------
# The type is set when you assign a value:
examples = [
    "Hello World",                 # str
    20,                            # int
    20.5,                          # float
    1j,                            # complex
    ["apple", "banana"],           # list
    ("apple", "banana"),           # tuple
    range(6),                      # range
    {"name": "Ravi", "age": 36},   # dict
    {"apple", "banana"},           # set
    frozenset({"apple", "banana"}),# frozenset
    True,                          # bool
    b"Hello",                      # bytes
    bytearray(5),                  # bytearray
    memoryview(bytes(5)),          # memoryview
    None,                          # NoneType
]
for value in examples:
    print(f"{str(value):35} {type(value).__name__}")

# ---------- Setting a specific data type ----------
# Use the constructor functions:
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana"))
x = tuple(("apple", "banana"))
x = range(6)
x = dict(name="Ravi", age=36)
x = set(("apple", "banana"))
x = frozenset(("apple", "banana"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
print(type(x))
