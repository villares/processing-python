"""
Minimal SVG Export test for Processing Python Mode
"""

add_library('svg')


def setup():
    global bg
    size(400, 400)
    background(255)
    # PGraphics pgDrawing
    pg_drawing = create_graphics(400, 400, SVG, "test.svg")
    pg_drawing.begin_draw()
    pg_drawing.background(255)
    pg_drawing.stroke(0)
    pg_drawing.stroke_weight(4)
    pg_drawing.rect(10, 10, 70, 50, 10)
    pg_drawing.end_draw()
    pg_drawing.dispose()
    # Load PShape bg
    bg = load_shape("test.svg")


def draw():
    shape(bg, 0, 0)
    no_loop()
