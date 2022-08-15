"""
Based on Loading Tabular Data example by Daniel Shiffman.
"""
from Bubble import Bubble
from input_message import input
import pickle


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
    global bubbles
    with open("data/bubbles.data", "rb") as f2:
        bubbles = pickle.load(f2)


def mouse_pressed():
    name = input("Name:")
    bubbles.append(Bubble(mouse_x,
                          mouse_y,
                          random(40, 80),
                          name))
    # If the list has more than 10 objects
    if len(bubbles) > 10:
        # Delete the oldest Buuble
        bubbles.pop(0)
    # WARNING: on Save you have to put the folder :(
    with open("data/bubbles.data", "wb") as file:
        pickle.dump(bubbles, file)

    load_data()
