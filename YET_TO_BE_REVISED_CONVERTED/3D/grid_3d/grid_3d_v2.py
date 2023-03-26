"""
A funny wobbling 3D grid - by Alexandre B A Villares (abav.lugaralgum.com)
1. install Processing (processing.org)
2. install Python Mode (isntructions on py.processing.org)
3. install PeasyCam library under Sketch...>Import Libray...>Add Library...
"""

add_library('peasycam')  # Drag the mouse to orbit!

ANG = 0
HALF_RANGE = 5
NUM_BOXES = (HALF_RANGE * 2) ** 3
BOXES = [()] * NUM_BOXES
S_SIZE = 10  # Controls the spacing of the grid
B_SIZE = 5   # B_SIZE <= box_size < B_SIZE * 2
SLIDE = 5    # Changes the sliding behaviour
SPEED = 0.01  # Increments ANG


def setup():
    size(600, 600, P3D)
    cam = PeasyCam(this, 200)
    cam.set_minimum_distance(200)
    cam.set_maximum_distance(200)
    on_grid(set_boxes, BOXES)


def draw():
    global ANG
    background(0)
    on_grid(plot_boxes, BOXES)
    ANG += SPEED


def on_grid(func, L):
    n = 0
    for i in range(-HALF_RANGE, HALF_RANGE):
        for j in range(-HALF_RANGE, HALF_RANGE):
            for k in range(-HALF_RANGE, HALF_RANGE):
                func(i, j, k, n, L)
                n += 1


def set_boxes(x, y, z, n, L):
    r, g, b = 150 + x * 20, 150 + y * 20, 150 + z * 20
    box_size = random(B_SIZE, B_SIZE * 2)
    L[n] = (color(r, g, b), box_size)


def plot_boxes(x, y, z, n, L):
    box_color, box_size = L[n]
    fill(box_color)
    with push_matrix():
        translate(x * S_SIZE * sin(ANG + x * SLIDE),
                  y * S_SIZE * sin(ANG + y * SLIDE),
                  z * S_SIZE * sin(ANG + z * SLIDE))
        box(box_size)
