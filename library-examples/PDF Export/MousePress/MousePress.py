"""
Mouse Press.

Saves one PDF of the contents of the display window
each time the mouse is pressed.
"""


add_library('pdf')

save_one_frame = False


def setup():
    size(600, 600)
    frame_rate(24)


def draw():
    global save_one_frame
    if save_one_frame:
        begin_record(PDF, "Line.pdf")

    background(255)
    stroke(0, 20)
    stroke_weight(20.0)
    line(mouse_x, 0, width - mouse_y, height)

    if save_one_frame:
        end_record()
        save_one_frame = False


def mouse_pressed():
    global save_one_frame
    save_one_frame = True
