# ==========================================================
# OPERATOR PRECEDENCE
# ==========================================================
# Precedence describes the order in which operations are performed.

# Parentheses have the highest precedence:
print((6 + 3) - (6 + 3))     # 0

# Multiplication beats addition:
print(100 + 5 * 3)           # 115, not 315

# Order, highest first:
#   ()                         parentheses
#   **                         exponentiation
#   +x  -x  ~x                 unary plus, minus, bitwise NOT
#   *  /  //  %                multiplication, division, floor div, modulus
#   +  -                       addition, subtraction
#   <<  >>                     bitwise shifts
#   &                          bitwise AND
#   ^                          bitwise XOR
#   |                          bitwise OR
#   == != > >= < <= is is not in not in   comparisons, identity, membership
#   not                        logical NOT
#   and                        AND
#   or                         OR

# Same precedence -> evaluated left to right:
print(5 + 4 - 7 + 3)         # 5
print(2 ** 3 ** 2)           # 512  (** is evaluated RIGHT to left)
