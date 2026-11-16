# ==========================================================
# PYTHON VIRTUAL ENVIRONMENTS
# ==========================================================
# A virtual environment is an isolated Python setup for one project.
# Each project gets its own packages and versions, so projects don't
# conflict with each other.
#
# Run these commands in a TERMINAL:
#
# ---------- Create a virtual environment ----------
#   python -m venv myfirstproject
#   (creates a folder "myfirstproject" with its own Python + pip)
#
# ---------- Activate it ----------
#   Windows:        myfirstproject\Scripts\activate
#   Mac / Linux:    source myfirstproject/bin/activate
#   The prompt now shows (myfirstproject) at the start.
#
# ---------- Install packages (only inside this environment) ----------
#   pip install cowsay
#
# ---------- Use the package ----------
#   python -c "import cowsay; cowsay.tux('Hello')"
#
# ---------- Deactivate ----------
#   deactivate
#
# ---------- Delete ----------
#   Just delete the environment folder.
#
# Tip: don't commit the venv folder to git - save your packages with
#   pip freeze > requirements.txt

# This script tells you whether it is running inside a virtual environment:
import sys
in_venv = sys.prefix != sys.base_prefix
print("Running inside a virtual environment:", in_venv)
print("Python prefix:", sys.prefix)
