# ==========================================================
# ESCAPE CHARACTERS
# ==========================================================
# To put characters that are not allowed into a string, use an escape
# character: a backslash \ followed by the character.

# txt = "We are the so-called "Vikings" from the north."   # error
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Other escape characters:
print('It\'s alright.')          # \'  single quote
print("A backslash: \\")         # \\  backslash
print("Hello\nWorld!")           # \n  new line
print("Hello\rWorld!")           # \r  carriage return
print("Hello\tWorld!")           # \t  tab
print("Hello \bWorld!")          # \b  backspace
print("\110\145\154\154\157")      # \ooo octal value  -> Hello
print("\x48\x65\x6c\x6c\x6f")      # \xhh hex value    -> Hello
