# ==========================================================
# PYTHON JSON
# ==========================================================
# JSON is a text format for storing and exchanging data.
# Python's built-in json module works with it.
import json

# ---------- Parse JSON (JSON string -> Python) ----------
x = '{ "name":"Ravi", "age":30, "city":"Delhi"}'
y = json.loads(x)          # result is a Python dictionary
print(y["age"])

# ---------- Convert Python -> JSON ----------
x = {"name": "Ravi", "age": 30, "city": "Delhi"}
y = json.dumps(x)          # result is a JSON string
print(y)

# These Python types can be converted to JSON:
print(json.dumps({"name": "Ravi", "age": 30}))   # dict  -> Object
print(json.dumps(["apple", "bananas"]))          # list  -> Array
print(json.dumps(("apple", "bananas")))          # tuple -> Array
print(json.dumps("hello"))                       # str   -> String
print(json.dumps(42))                            # int   -> Number
print(json.dumps(31.76))                         # float -> Number
print(json.dumps(True))                          # True  -> true
print(json.dumps(False))                         # False -> false
print(json.dumps(None))                          # None  -> null

x = {
    "name": "Ravi",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x))

# ---------- Format the result ----------
print(json.dumps(x, indent=4))                          # indentation
print(json.dumps(x, indent=4, separators=(". ", " = ")))  # custom separators

# ---------- Order the result ----------
print(json.dumps(x, indent=4, sort_keys=True))
