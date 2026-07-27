import os
import json
from pathlib import Path

ROOT = Path(".")

print("=" * 80)
print("OPENJARVIS PROJECT ANALYSIS")
print("=" * 80)

# ------------------------
# Print directory tree
# ------------------------
print("\nPROJECT STRUCTURE\n")

EXCLUDE = {
    ".git",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
    "dist",
    "build",
    ".next",
    ".idea",
    ".vscode"
}

def tree(path, prefix=""):
    items = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    items = [i for i in items if i.name not in EXCLUDE]

    for index, item in enumerate(items):
        connector = "└── " if index == len(items)-1 else "├── "
        print(prefix + connector + item.name)

        if item.is_dir():
            extension = "    " if index == len(items)-1 else "│   "
            tree(item, prefix + extension)

tree(ROOT)

# ------------------------
# package.json
# ------------------------

pkg = ROOT / "package.json"
if pkg.exists():
    print("\n" + "="*80)
    print("PACKAGE.JSON")
    print("="*80)

    data = json.loads(pkg.read_text(encoding="utf-8"))

    for key in [
        "name",
        "version",
        "description",
        "scripts",
        "dependencies",
        "devDependencies"
    ]:
        if key in data:
            print(f"\n{key}:")
            print(json.dumps(data[key], indent=2))

# ------------------------
# requirements.txt
# ------------------------

req = ROOT / "requirements.txt"
if req.exists():
    print("\n" + "="*80)
    print("requirements.txt")
    print("="*80)
    print(req.read_text())

# ------------------------
# pyproject.toml
# ------------------------

pyproject = ROOT / "pyproject.toml"
if pyproject.exists():
    print("\n" + "="*80)
    print("pyproject.toml")
    print("="*80)
    print(pyproject.read_text())

# ------------------------
# Docker
# ------------------------

for name in [
    "Dockerfile",
    "docker-compose.yml",
    "docker-compose.yaml",
]:
    file = ROOT / name
    if file.exists():
        print("\n" + "="*80)
        print(name)
        print("="*80)
        print(file.read_text())

# ------------------------
# ENV files
# ------------------------

print("\n" + "="*80)
print(".env FILES")
print("="*80)

for file in ROOT.rglob("*"):
    if file.name.startswith(".env"):
        print("\nFILE:", file)
        try:
            print(file.read_text())
        except:
            print("Cannot read.")

# ------------------------
# README
# ------------------------

for name in [
    "README.md",
    "README.MD",
    "readme.md"
]:
    file = ROOT / name
    if file.exists():
        print("\n" + "="*80)
        print("README")
        print("="*80)
        print(file.read_text())
        break

# ------------------------
# Ports
# ------------------------

print("\n" + "="*80)
print("POSSIBLE PORTS")
print("="*80)

ports = []

for path in ROOT.rglob("*"):
    if path.is_file():
        try:
            text = path.read_text(errors="ignore")
            for line in text.splitlines():
                if "localhost:" in line or "127.0.0.1:" in line:
                    ports.append((path, line.strip()))
                elif "PORT" in line.upper():
                    ports.append((path, line.strip()))
        except:
            pass

for p in ports[:200]:
    print(p[0], ":", p[1])

# ------------------------
# Main files
# ------------------------

print("\n" + "="*80)
print("ENTRY FILES")
print("="*80)

for name in [
    "main.py",
    "app.py",
    "server.py",
    "manage.py",
    "index.js",
    "index.ts",
    "main.ts",
]:
    for f in ROOT.rglob(name):
        print(f)

print("\nAnalysis Complete.")