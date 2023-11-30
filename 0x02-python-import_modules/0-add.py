if __name__ == "__main__":
    a = 1
    b = 2

    # Importing the function add from add_0.py
    import importlib
    add_module = importlib.import_module("add_0")
    add = add_module.add

    result = add(a, b)
    print(f"{a} + {b} = {result}")
