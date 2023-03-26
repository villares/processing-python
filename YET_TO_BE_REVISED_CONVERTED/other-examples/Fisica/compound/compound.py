"""
 *    Compound
 *
 *    by Ricard Marxer
 *
 *    This example shows how to create compound bodies
 *    which are bodies made of multiple shapes.
 """
from fisica import Fisica, FWorld, FCompound, FCircle, FBox
add_library('fisica')

world, pop, cage = None, None, None


def setup():
    global world, pop, cage
    size(400, 400)
    smooth()
    Fisica.init(this)
    Fisica.setScale(10)
    world = FWorld()
    world.set_edges()
    world.remove(world.top)
    pop = create_pop()
    pop.set_position(width/2, height/2)
    pop.set_bullet(True)
    world.add(pop)
    cage = create_cage()
    cage.set_position(width/2, height/2)
    cage.set_rotation(PI/6)
    cage.set_bullet(True)
    world.add(cage)

    for _ in range(10):
        c = FCircle(7)
        c.set_position(width/2-10+random(-5, 5), height/2-10+random(-5, 5))
        c.set_bullet(True)
        c.set_no_stroke()
        c.set_fill_color(color(0xFF, 0x92, 0x03))
        world.add(c)

    rect_mode(CENTER)


def draw():
    background(255)
    world.step()
    world.draw()


def create_pop():
    b = FBox(6, 60)
    b.set_fill_color(color(0x1F, 0x71, 0x6B))
    b.set_no_stroke()
    c = FCircle(20)
    c.set_position(0, -30)
    c.set_fill_color(color(0xFF, 0x00, 0x51))
    c.set_no_stroke()

    result = FCompound()
    result.add_body(b)
    result.add_body(c)

    return result


def create_cage():
    b1 = FBox(10, 110)
    b1.set_position(50, 0)
    b1.set_fill(0)
    b1.set_no_stroke()
    b2 = FBox(10, 110)
    b2.set_position(-50, 0)
    b2.set_fill(0)
    b2.set_no_stroke()

    b3 = FBox(110, 10)
    b3.set_position(0, 50)
    b3.set_fill(0)
    b3.set_no_stroke()

    b4 = FBox(110, 10)
    b4.set_position(0, -50)
    b4.set_fill(0)
    b4.set_no_stroke()

    result = FCompound()
    result.add_body(b1)
    result.add_body(b2)
    result.add_body(b3)
    result.add_body(b4)
    return result


def key_pressed():
    save_frame("screenshot.png")
