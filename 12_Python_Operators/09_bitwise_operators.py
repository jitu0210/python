# ==========================================================
# BITWISE OPERATORS
# ==========================================================
# Work on numbers at the level of their binary bits.
a = 6     # 0110
b = 3     # 0011

print(a & b)    # AND  -> 0010 = 2   (1 where both bits are 1)
print(a | b)    # OR   -> 0111 = 7   (1 where either bit is 1)
print(a ^ b)    # XOR  -> 0101 = 5   (1 where only one bit is 1)
print(~a)       # NOT  -> -7         (inverts all bits)
print(a << 1)   # Zero-fill left shift  -> 1100 = 12
print(a >> 1)   # Signed right shift    -> 0011 = 3

# See the binary representation with bin():
print(bin(a), bin(b), bin(a & b))
