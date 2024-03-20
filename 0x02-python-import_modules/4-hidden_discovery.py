#!/usr/bin/python3

import inspect

def print_hidden_names():
    with open("hidden_4.pyc", "rb") as f:
        code = f.read()

    module = compile(code, "hidden_4.py", "exec")
    names = [name for name, obj in inspect.getmembers(module)
             if not name.startswith("__")]

    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_hidden_names()

