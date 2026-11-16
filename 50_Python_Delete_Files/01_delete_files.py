# ==========================================================
# PYTHON DELETE FILES
# ==========================================================
# Import the os module and use os.remove() to delete a file.
import os
# Work in this script's folder so the demo files are created here.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create a file to delete:
with open("demofile.txt", "w") as f:
    f.write("delete me")

# ---------- Delete a file ----------
os.remove("demofile.txt")
print("demofile.txt deleted")

# ---------- Check if the file exists first ----------
# (avoids an error when it is not there)
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# ---------- Delete a folder ----------
# os.rmdir() removes an EMPTY folder.
os.mkdir("myfolder")
print("myfolder exists:", os.path.exists("myfolder"))
os.rmdir("myfolder")
print("myfolder exists:", os.path.exists("myfolder"))
