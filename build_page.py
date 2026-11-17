"""Build index.html: a single page that lists every file in this repo,
shows the code with highlighting, and runs Python in the browser (Pyodide).

Run:  python build_page.py   -> then open index.html in a browser.
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", ".claude", ".planning"}
EXTS = {".py", ".md", ".txt", ".json"}

files = {}
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
    for name in sorted(filenames):
        if os.path.splitext(name)[1] not in EXTS:
            continue
        full = os.path.join(dirpath, name)
        rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
        with open(full, encoding="utf-8", errors="replace") as f:
            files[rel] = f.read()

data = json.dumps(files, ensure_ascii=False).replace("</", "<\\/")

with open(os.path.join(ROOT, "page_template.html"), encoding="utf-8") as f:
    template = f.read()

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(template.replace("__FILES_JSON__", data))

print(f"index.html built with {len(files)} files")
