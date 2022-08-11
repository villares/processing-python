"""
Many PDFs.

Saves one PDF file each each frame while the mouse is pressed.
When the mouse is released, the PDF creation stops.
"""


add_library('pdf')

save_pdf = False


def setup():
    size(600, 600)
    frame_rate(24)


def draw():
    if save_pdf:
        begin_record(PDF, "lines%d.pdf" % (frame_count))

    background(255)
    stroke(0, 20)
    stroke_weight(20.0)
    line(mouse_x, 0, width - mouse_y, height)

    if save_pdf:
        end_record()


def mouse_pressed():
    global save_pdf
    save_pdf = True


def mouse_released():
    global save_pdf
    save_pdf = False
