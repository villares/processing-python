"""
 *    Densities
 *
 *    by Ricard Marxer
 *
 *    This example shows how the density works.
 *    The density determines the mass per area of a body.
 *    In this example we show a column of balls all of same area and increasing
 *    densities from 0.1 to 0.9.
 *    These balls will collide against another column of balls all with the same
 *    density of 0.9.
 *    We can observe the different behavior of the collisions depending on the
 *    density.
 *
 *    Note that a density of 0.0 corresponds to a mass of 0 and the body will be
 *    considered static.
 """
from fisica import FWorld, Fisica, FCircle
add_library('fisica')

world = None
ball_count = 9


def setup():
    global world
    size(400, 400)
    smooth()
    Fisica.init(this)
    world = FWorld()
    world.set_gravity(0, 0)
    world.set_edges()
    world.remove(world.left)
    world.remove(world.top)
    world.remove(world.bottom)
    for i in range(ball_count):
        b = FCircle(25)
        b.set_position(40, map(i, 0, ball_count-1, 40, height-40))
        b.set_density(map(i, 0, ball_count-1, 0.1, 0.9))
        b.set_velocity(100, 0)
        b.set_damping(0.0)
        b.set_no_stroke()
        b.set_fill(map(i, 0, ball_count-1, 120, 0))
        world.add(b)
    for i in range(ball_count):
        b = FCircle(25)
        b.set_position(width/2, map(i, 0, ball_count-1, 40, height-40))
        b.set_velocity(0, 0)
        b.set_damping(0.0)
        b.set_density(0.9)
        b.set_no_stroke()
        b.set_fill(125, 80, 120)
        world.add(b)


def draw():
    background(255)
    world.step()
    world.draw()


def key_pressed():
    save_frame("screenshot.png")
