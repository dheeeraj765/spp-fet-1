"""
print_tree.py

Prints the project's folder and file structure as a tree,
so the organization created in this experiment can be verified visually.
"""

import os


def print_tree(start_path=".", prefix=""):
    """Recursively print the directory tree starting at start_path."""
    entries = sorted(
        e for e in os.listdir(start_path)
        if e not in (".git", "__pycache__", ".venv")
    )
    for i, entry in enumerate(entries):
        path = os.path.join(start_path, entry)
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry)
        if os.path.isdir(path):
            extension = "    " if i == len(entries) - 1 else "│   "
            print_tree(path, prefix + extension)


if __name__ == "__main__":
    print_tree(".")
