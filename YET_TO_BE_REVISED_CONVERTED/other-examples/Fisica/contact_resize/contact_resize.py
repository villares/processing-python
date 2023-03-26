"""
ContactRemove  by Ricard Marxer
This example shows how to use the contact events in order to remove bodies.
"""
from fisica import Fisica, FWorld, FCircle, FContact
add_library('fisica')


world = None


def setup():
    global world
    size(400, 400)
    smooth()
    Fisica.init(this)
    world = FWorld()
    world.set_gravity(0, 100)
    world.set_edges()


def draw():
    background(255)
    if frame_count % 50 == 0:
        sz = random(30, 60)
        b = FCircle(sz)
        b.set_position(random(0+30, width-30), 50)
        b.set_velocity(0, 100)
        b.set_restitution(0.7)
        b.set_damping(0.01)
        b.set_no_stroke()
        b.set_fill(200, 30, 90)
        world.add(b)
    world.draw()
    world.step()


def contact_ended(c):
    for b in (c.get_body1(), c.get_body2()):
        if not b.is_static() and b.get_size() > 5:
            b.set_size(b.get_size() * 0.9)


def key_pressed():
    save_frame("screenshot.png")
