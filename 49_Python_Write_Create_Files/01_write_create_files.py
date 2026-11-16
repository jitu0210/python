# ==========================================================
# PYTHON WRITE / CREATE FILES
# ==========================================================
import os
# Work in this script's folder so the demo files are created here.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("demofile.txt", "w") as f:
    f.write("Hello! Welcome to demofile.txt\n")

# ---------- Write to an existing file ----------
#   "a" - Append: adds to the end
#   "w" - Write:  overwrites ALL existing content

# Append
with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!\n")

with open("demofile.txt") as f:
    print(f.read())

# Overwrite
with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!\n")

with open("demofile.txt") as f:
    print(f.read())

# ---------- Create a new file ----------
#   "x" - Create: error if the file exists
#   "a" - Append: creates the file if it does not exist
#   "w" - Write:  creates the file if it does not exist
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")

f = open("myfile.txt", "x")
f.close()
print("myfile.txt created:", os.path.exists("myfile.txt"))

try:
    open("myfile.txt", "x")
except FileExistsError:
    print("'x' mode fails because myfile.txt already exists")

# Write several lines at once:
with open("myfile.txt", "w") as f:
    f.writelines(["line 1\n", "line 2\n", "line 3\n"])

with open("myfile.txt") as f:
    print(f.read())
