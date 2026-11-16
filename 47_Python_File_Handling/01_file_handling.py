# ==========================================================
# PYTHON FILE HANDLING
# ==========================================================
# File handling is an important part of many programs.
# Python has functions to create, read, update and delete files.
import os
# Work in this script's folder so the demo files are created here.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ---------- open() ----------
# open(filename, mode)
#
# Modes:
#   "r" - Read    (default) error if the file does not exist
#   "a" - Append  creates the file if it does not exist
#   "w" - Write   creates the file if it does not exist (overwrites!)
#   "x" - Create  error if the file already exists
#
# Plus, how the file is handled:
#   "t" - Text    (default)
#   "b" - Binary  (e.g. images)

# Make a small file to work with:
with open("demofile.txt", "w") as f:
    f.write("Hello! Welcome to demofile.txt\nThis file is for testing purposes.\nGood Luck!\n")

# These two lines are the same ("r" and "t" are defaults):
f = open("demofile.txt")
f.close()
f = open("demofile.txt", "rt")
f.close()

print("demofile.txt created - see the next folders for reading/writing.")
