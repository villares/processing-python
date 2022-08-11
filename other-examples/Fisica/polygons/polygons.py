"""
Polygons by Ricard Marxer
This example shows how to create polygon bodies.
"""
from fisica import Fisica, FWorld, FPoly, FBody
add_library('fisica')

world, poly = None, None


def setup():
    global world
    size(400, 400)
    smooth()
    Fisica.init(this)
    world = FWorld()
    world.set_gravity(0, 800)
    world.set_edges()
    world.remove(world.left)
    world.remove(world.right)
    world.remove(world.top)

    world.set_edges_restitution(0.5)


def draw():
    background(255)
    world.step()
    world.draw(this)
    # Draw the polygon while
    # while it is being created
    # and hasn't been added to the
    # world yet
    if poly:
        poly.draw(this)


def mouse_pressed():
    if world.get_body(mouse_x, mouse_y):
        return
    global poly
    poly = FPoly()
    poly.set_stroke_weight(3)
    poly.set_fill(120, 30, 90)
    poly.set_density(10)
    poly.set_restitution(0.5)
    poly.vertex(mouse_x, mouse_y)


def mouse_dragged():
    if poly:
        poly.vertex(mouse_x, mouse_y)


def mouse_released():
    global poly
    if poly:
        world.add(poly)
        poly = None


def key_pressed():
    if key == BACKSPACE:
        hovered = world.get_body(mouse_x, mouse_y)
        if hovered and not hovered.is_static():
            world.remove(hovered)
    else:
        save_frame("screenshot.png")
