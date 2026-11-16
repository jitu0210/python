# ==========================================================
# PYTHON PIP
# ==========================================================
# PIP is the package manager for Python packages (modules).
# It is included with Python 3.4 and later.
#
# A PACKAGE contains all the files needed for a module.
# Packages are found at https://pypi.org
#
# Run these commands in a TERMINAL (not inside Python):
#
#   Check PIP is installed:     pip --version
#   Download a package:         pip install camelcase
#   Remove a package:           pip uninstall camelcase
#   List installed packages:    pip list
#   Upgrade a package:          pip install --upgrade camelcase
#   Save requirements:          pip freeze > requirements.txt
#   Install from requirements:  pip install -r requirements.txt
#
# After installing, use a package with import:
#
#   import camelcase
#   c = camelcase.CamelCase()
#   print(c.hump("hello world"))     # Hello World

# This script shows which packages are installed, using only the standard library:
from importlib import metadata

dists = sorted(metadata.distributions(), key=lambda d: (d.metadata["Name"] or "").lower())
print(f"{len(dists)} packages installed. First few:")
for d in dists[:10]:
    print(" ", d.metadata["Name"], d.version)
