"""
ContactRemove by Ricard Marxer
This example shows how to use the contact events in order to remove bodies.
"""
from fisica import Fisica, FWorld, FBox, FCircle, FBody, FContact
add_library('fisica')

world, pala = None, None


def setup():
    global world, pala
    size(400, 400)
    smooth()
    Fisica.init(this)
    world = FWorld()
    pala = FBox(50, 20)
    pala.set_position(width/2, height - 40)
    pala.set_static(True)
    pala.set_fill(0)
    pala.set_restitution(0)
    world.add(pala)


def draw():
    background(255)
    if frame_count % 8 == 0:
        b = FCircle(random(5, 20))
        b.set_position(random(0+10, width-10), 50)
        b.set_velocity(0, 200)
        b.set_restitution(0)
        b.set_no_stroke()
        b.set_fill(200, 30, 90)
        world.add(b)
    pala.set_position(mouse_x, height - 40)
    world.draw()
    world.step()


def contact_started(c):
    ball = None
    if c.get_body1() == pala:
        ball = c.get_body2()
    elif c.get_body2() == pala:
        ball = c.get_body1()
    if not ball:
        return
    ball.set_fill(30, 190, 200)
    world.remove(ball)


def key_pressed():
    save_frame("screenshot.png")
