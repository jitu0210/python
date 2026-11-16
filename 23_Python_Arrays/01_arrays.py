# ==========================================================
# PYTHON ARRAYS
# ==========================================================
# Python has no built-in array type - LISTS are used instead.
# (For real numeric arrays, use a library such as NumPy.)

cars = ["Ford", "Volvo", "BMW"]

# ---------- What is an array? ----------
# A special variable that can hold more than one value at a time.
# Instead of car1, car2, car3 ... you keep them in one array.

# ---------- Access the elements ----------
x = cars[0]
print(x)

# ---------- Modify ----------
cars[0] = "Toyota"
print(cars)

# ---------- Length of an array ----------
print(len(cars))
# The length is always one more than the highest index.

# ---------- Looping ----------
for x in cars:
    print(x)

# ---------- Adding elements ----------
cars.append("Honda")
print(cars)

# ---------- Removing elements ----------
cars.pop(1)              # by index
print(cars)
cars.remove("BMW")       # by value (first match)
print(cars)

# ---------- Array methods (list methods) ----------
# append() clear() copy() count() extend() index() insert()
# pop() remove() reverse() sort()

# ---------- The array module ----------
# For arrays of ONE numeric type, there is the built-in `array` module:
import array
nums = array.array("i", [1, 2, 3])   # "i" = signed integers
nums.append(4)
print(nums, nums[0])
