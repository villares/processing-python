"""
Minimal SVG Export test for Processing Python Mode
"""

add_library('svg')


def setup():
    size(400, 400)
    # PGraphics pgDrawing
    pg_drawing = create_graphics(400, 400, SVG, "test.svg")
    begin_record(pg_drawing)
    # background(255)
    stroke(0)
    stroke_weight(4)
    rect(10, 10, 70, 50, 10)
    end_record()


def draw():
    no_loop()
