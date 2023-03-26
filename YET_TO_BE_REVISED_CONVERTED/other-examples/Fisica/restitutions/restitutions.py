"""
Restitutions by Ricard Marxer
This example shows how the restitution coefficients works.
"""
from fisica import Fisica, FWorld, FCircle
add_library('fisica')

world = None

ball_count = 10


def setup():
    global world
    size(400, 400)
    smooth()
    Fisica.init(this)
    world = FWorld()
    world.set_edges()
    world.remove(world.left)
    world.remove(world.right)
    world.remove(world.top)
    world.set_edges_restitution(0.0)
    for i in range(ball_count):
        b = FCircle(25)
        b.set_position(map(i, 0, ball_count-1, 40, width-40), height/6)
        b.set_restitution(map(i, 0, ball_count-1, 0.0, 1.0))
        b.set_no_stroke()
        b.set_fill(map(i, 0, ball_count-1, 60, 255), 80, 120)
        world.add(b)


def draw():
    background(255)
    world.step()
    world.draw()


def key_pressed():
    save_frame("screenshot.png")
