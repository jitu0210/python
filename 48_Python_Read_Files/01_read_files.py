# ==========================================================
# PYTHON READ FILES
# ==========================================================
import os
# Work in this script's folder so the demo files are created here.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create the demo file first:
with open("demofile.txt", "w") as f:
    f.write("Hello! Welcome to demofile.txt\nThis file is for testing purposes.\nGood Luck!\n")

# ---------- Open a file and read it ----------
f = open("demofile.txt")
print(f.read())
f.close()

# A file in another folder: give the full path, e.g.
#   f = open("D:\\myfiles\\welcome.txt")

# ---------- Using the with statement ----------
# `with` closes the file automatically - the recommended way.
with open("demofile.txt") as f:
    print(f.read())

# ---------- Close files ----------
# Always close a file when done (with does it for you). Unclosed files
# may not save changes and keep system resources busy.
f = open("demofile.txt")
print(f.readline())
f.close()

# ---------- Read only parts of the file ----------
with open("demofile.txt") as f:
    print(f.read(5))           # first 5 characters

# ---------- Read lines ----------
with open("demofile.txt") as f:
    print(f.readline())        # one line
    print(f.readline())        # the next line

# Loop through the file line by line:
with open("demofile.txt") as f:
    for line in f:
        print(line.strip())
