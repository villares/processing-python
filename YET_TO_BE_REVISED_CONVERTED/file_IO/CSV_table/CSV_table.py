"""
Based on Loading Tabular Data example by Daniel Shiffman.
"""
from Bubble import Bubble
from input_message import input

bubbles = []


def setup():
    size(640, 360)
    load_data()


def draw():
    background(255)
    # Display all bubbles
    for b in bubbles:
        b.display()
        b.rollover(mouse_x, mouse_y)

    text_align(LEFT)
    fill(0)
    text("Click to add bubbles.", 10, height - 10)


def load_data():
    # Load CSV file into a Table object
    global table
    global bubbles
    # "header" option indicates the file has a header row
    table = load_table("data.csv", "header")
    bubbles = []

    for row in table.rows():
        # You can access the fields via their column name (or index)
        x = row.get_float("x")
        y = row.get_float("y")
        d = row.get_float("diameter")
        n = row.get_string("name")
        # Make a Bubble object out of the data read
        bubbles.append(Bubble(x, y, d, n))


def mouse_pressed():
    global table
    # Create a new row
    row = table.add_row()
    # Set the values of that row
    row.set_float("x", mouse_x)
    row.set_float("y", mouse_y)
    row.set_float("diameter", random(40, 80))
    name = input("Name:")
    row.set_string("name", name)

    # If the table has more than 10 rows
    if table.get_row_count() > 10:
        # Delete the oldest row
        table.remove_row(0)

    # WARNING: on Save you have to put the folder :(
    save_table(table, "data/data.csv")
    # Reload
    load_data()
