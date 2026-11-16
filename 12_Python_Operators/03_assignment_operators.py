# ==========================================================
# ASSIGNMENT OPERATORS
# ==========================================================
x = 5;   print("x = 5    ->", x)
x += 3;  print("x += 3   ->", x)   # x = x + 3
x -= 3;  print("x -= 3   ->", x)   # x = x - 3
x *= 3;  print("x *= 3   ->", x)   # x = x * 3
x /= 3;  print("x /= 3   ->", x)   # x = x / 3
x = 5
x %= 3;  print("x %= 3   ->", x)   # x = x % 3
x = 5
x //= 3; print("x //= 3  ->", x)   # x = x // 3
x = 5
x **= 3; print("x **= 3  ->", x)   # x = x ** 3
x = 5
x &= 3;  print("x &= 3   ->", x)   # x = x & 3
x = 5
x |= 3;  print("x |= 3   ->", x)   # x = x | 3
x = 5
x ^= 3;  print("x ^= 3   ->", x)   # x = x ^ 3
x = 5
x >>= 3; print("x >>= 3  ->", x)   # x = x >> 3
x = 5
x <<= 3; print("x <<= 3  ->", x)   # x = x << 3

# ---------- The Walrus operator :=  (Python 3.8+) ----------
# Assigns a value AND returns it, inside an expression.
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
