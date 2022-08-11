"""
Many Pages.

Saves a new page into a PDF file each loop through draw().
Pressing the mouse finishes writing the file and exits the program.
"""


add_library('pdf')


def setup():
    global pdf
    size(600, 600)
    frame_rate(4)
    pdf = begin_record(PDF, "Lines.pdf")


def draw():
    background(255)
    stroke(0, 20)
    stroke_weight(20.0)
    line(mouse_x, 0, width - mouse_y, height)
    pdf.next_page()


def mouse_pressed():
    end_record()
    exit()
