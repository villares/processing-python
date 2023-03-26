"""
 *    Buttons and bodies
 *
 *    by Ricard Marxer
 *
 *    This example shows how to create bodies.
 *    It also demonstrates the use of bodies as buttons.
 """
from fisica import Fisica, FWorld, FBox, FCircle, FPoly
add_library('fisica')

box_button = None
circle_button = None
poly_button = None
world = None
button_color = color(0x15, 0x5A, 0xAD)
hover_color = color(0x55, 0xAA, 0x11)
body_color = color(0x6E, 0x05, 0x95)


def setup():
    global box_button, circle_button, poly_button, world

    size(400, 400)
    smooth()
    Fisica.init(this)
    world = FWorld()
    world.set_edges()
    world.remove(world.left)
    world.remove(world.right)
    world.remove(world.top)
    box_button = FBox(40, 40)
    box_button.set_position(width/4, 100)
    box_button.set_static(True)
    box_button.set_fill_color(button_color)
    box_button.set_no_stroke()
    world.add(box_button)
    circle_button = FCircle(40)
    circle_button.set_position(2*width/4, 100)
    circle_button.set_static(True)
    circle_button.set_fill_color(button_color)
    circle_button.set_no_stroke()
    world.add(circle_button)
    poly_button = FPoly()
    poly_button.vertex(20, 20)
    poly_button.vertex(-20, 20)
    poly_button.vertex(0, -20)
    poly_button.set_position(3*width/4, 100)
    poly_button.set_static(True)
    poly_button.set_fill_color(button_color)
    poly_button.set_no_stroke()
    world.add(poly_button)


def draw():
    background(255)
    world.step()
    world.draw()


def mouse_pressed():
    pressed = world.get_body(mouse_x, mouse_y)
    if pressed == box_button:
        my_box = FBox(40, 40)
        my_box.set_position(width/4, 200)
        my_box.set_rotation(random(TWO_PI))
        my_box.set_velocity(0, 200)
        my_box.set_fill_color(body_color)
        my_box.set_no_stroke()
        world.add(my_box)
    elif pressed == circle_button:
        my_circle = FCircle(40)
        my_circle.set_position(2*width/4, 200)
        my_circle.set_rotation(random(TWO_PI))
        my_circle.set_velocity(0, 200)
        my_circle.set_fill_color(body_color)
        my_circle.set_no_stroke()
        world.add(my_circle)
    elif pressed == poly_button:
        my_poly = FPoly()
        my_poly.vertex(20, 20)
        my_poly.vertex(-20, 20)
        my_poly.vertex(0, -20)
        my_poly.set_position(3*width/4, 200)
        my_poly.set_rotation(random(TWO_PI))
        my_poly.set_velocity(0, 200)
        my_poly.set_fill_color(body_color)
        my_poly.set_no_stroke()
        world.add(my_poly)


def mouse_moved():
    hovered = world.get_body(mouse_x, mouse_y)
    if hovered in (box_button, circle_button, poly_button):
        hovered.set_fill_color(hover_color)
    else:
        box_button.set_fill_color(button_color)
        circle_button.set_fill_color(button_color)
        poly_button.set_fill_color(button_color)


def key_pressed():
    save_frame("screenshot.png")
