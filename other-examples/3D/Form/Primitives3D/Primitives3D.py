"""
Primitives 3D.

 Placing mathematically 3D objects in synthetic space.
 The lights() method reveals their imagined dimension.
 The box() and sphere() functions each have one parameter
 which is used to specify their size. These shapes are
 positioned using the translate() function.
"""


def setup():
    size(640, 360, P3D)
    background(0)


def draw():
    lights()
    fill(50)
    push_matrix()
    translate(130, height / 2, 0)
    rotate_y(1.25)
    rotate_x(-0.4)
    box(100)
    pop_matrix()
    no_fill()
    stroke(255)
    push_matrix()
    translate(500, height * 0.35, -200)
    sphere(210)
    pop_matrix()
