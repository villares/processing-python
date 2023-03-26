def setup():
    print(sketch_name())


def sketch_name():
    """
    print the sketch name (same as the folder name - no exetension)
    """
    from os import path
    sketch = sketch_path()
    name = path.basename(sketch)
    return name
