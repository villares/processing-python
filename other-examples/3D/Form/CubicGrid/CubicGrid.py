from java.lang import System
System.setProperty("jogl.disable.openglcore", "false")
"""
    Cubic Grid
    by Ira Greenberg.

    3D translucent colored grid uses nested pushMatrix()
    and popMatrix() functions.
"""
box_size = 40
margin = box_size*2
depth = 400


def setup():
    size(640, 360, P3D)
    no_stroke()


def draw():
    background(255)

    # Center and spin grid
    translate(width/2, height/2, -depth)
    rotate_y(frame_count * 0.01)
    rotate_x(frame_count * 0.01)

    # Build grid using multiple translations
    i = -depth/2+margin
    while i <= depth/2-margin:
        push_matrix()
        j = -height+margin
        while j <= height-margin:
            push_matrix()
            k = -width + margin
            while k <= width-margin:
                # Base fill color on counter values, abs function
                # ensures values stay within legal range
                box_fill = color(abs(i), abs(j), abs(k), 50)
                push_matrix()
                translate(k, j, i)
                fill(box_fill)
                box(box_size, box_size, box_size)
                pop_matrix()
                k += box_size
            pop_matrix()
            j += box_size
        pop_matrix()
        i += box_size
