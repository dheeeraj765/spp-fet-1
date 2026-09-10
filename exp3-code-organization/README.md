# Exp 3 — Code Organization, Modularization & Documentation

## Aim
To organize a Python project using a proper folder structure, create reusable
modules and scripts, and document the code using docstrings and comments.

## Project Structure
```
exp3-code-organization/
├── README.md
├── requirements.txt
├── main.py
├── print_tree.py
└── src/
    ├── __init__.py
    └── methods.py
```

## Files
- **src/methods.py** — reusable functions (`add`, `sub`)
- **main.py** — imports and runs the functions from `src.methods`
- **print_tree.py** — prints the project's folder/file structure
- **requirements.txt** — project dependencies (none required)

## How to Run
```bash
python main.py
python print_tree.py
```

## Expected Output (main.py)
```
15
5
```

## Conclusion
This experiment demonstrated good Python coding practices by organizing code
into modules and documenting it using comments and docstrings, making the
project more readable, reusable, and maintainable.
