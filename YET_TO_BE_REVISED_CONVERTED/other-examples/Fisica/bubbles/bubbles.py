"""
Bubbles by Ricard Marxer
This example shows how to create a blob.
"""
from fisica import Fisica, FWorld, FPoly, FBlob
add_library('fisica')

world = None
x_pos = 0

circle_count = 20
hole = 50
top_margin = 50
bottom_margin = 300
side_margin = 100


def setup():
    global world

    size(400, 400)
    smooth()
    Fisica.init(this)
    world = FWorld()
    world.set_gravity(0, -300)
    l = FPoly()
    l.vertex(width/2-hole/2, 0)
    l.vertex(0, 0)
    l.vertex(0, height)
    l.vertex(0+side_margin, height)
    l.vertex(0+side_margin, height-bottom_margin)
    l.vertex(width/2-hole/2, top_margin)
    l.set_static(True)
    l.set_fill(0)
    l.set_friction(0)
    world.add(l)
    r = FPoly()
    r.vertex(width/2+hole/2, 0)
    r.vertex(width, 0)
    r.vertex(width, height)
    r.vertex(width-side_margin, height)
    r.vertex(width-side_margin, height-bottom_margin)
    r.vertex(width/2+hole/2, top_margin)
    r.set_static(True)
    r.set_fill(0)
    r.set_friction(0)
    world.add(r)


def draw():
    global x_pos
    background(80, 120, 200)
    if (frame_count % 40) == 1:
        b = FBlob()
        s = random(30, 40)
        space = (width-side_margin*2-s)
        x_pos = (x_pos + random(s, space/2)) % space
        b.set_as_circle(side_margin + x_pos+s/2, height-random(100), s, 20)
        b.set_stroke(0)
        b.set_stroke_weight(2)
        b.set_fill(255)
        b.set_friction(0)
        world.add(b)
    world.step()
    world.draw()
