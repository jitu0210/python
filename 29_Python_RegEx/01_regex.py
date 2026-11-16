# ==========================================================
# PYTHON REGEX (Regular Expressions)
# ==========================================================
# A RegEx is a sequence of characters that forms a search pattern.
# Python's built-in `re` module works with them.
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print("Match!" if x else "No match")

# ---------- RegEx functions ----------
#   findall - list of all matches
#   search  - Match object for the first match
#   split   - list split at each match
#   sub     - replace matches with a string

# ---------- Metacharacters ----------
#   []  a set of characters          "[a-m]"
#   \   special sequence / escape    "\d"
#   .   any character except newline "he..o"
#   ^   starts with                  "^hello"
#   $   ends with                    "planet$"
#   *   zero or more                 "he.*o"
#   +   one or more                  "he.+o"
#   ?   zero or one                  "he.?o"
#   {}  exactly this many            "he.{2}o"
#   |   either or                    "falls|stays"
#   ()  capture and group

# ---------- Special sequences ----------
#   \A  match at the beginning      \b  word boundary
#   \B  NOT a word boundary         \d  digit 0-9
#   \D  not a digit                 \s  whitespace
#   \S  not whitespace              \w  word character [a-zA-Z0-9_]
#   \W  not a word character        \Z  match at the end

# ---------- Sets ----------
#   [arn]   one of a, r, n          [a-n]  lowercase a..n
#   [^arn]  anything except a,r,n   [0123] one of these digits
#   [0-9]   any digit               [0-5][0-9] two-digit 00..59
#   [a-zA-Z] any letter             [+]    a literal +

# ---------- findall() ----------
print(re.findall("ai", txt))          # ['ai', 'ai']
print(re.findall("Portugal", txt))    # []

# ---------- search() ----------
x = re.search(r"\s", txt)
print("First white-space at position:", x.start())
print(re.search("Portugal", txt))     # None

# ---------- split() ----------
print(re.split(r"\s", txt))
print(re.split(r"\s", txt, maxsplit=1))

# ---------- sub() ----------
print(re.sub(r"\s", "9", txt))
print(re.sub(r"\s", "9", txt, count=2))

# ---------- Match object ----------
x = re.search(r"\bS\w+", txt)
print(x.span())      # (start, end) of the match
print(x.string)      # the string passed in
print(x.group())     # the matched part
