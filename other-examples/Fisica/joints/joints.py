"""
 *    Joints
 *    by Ricard Marxer
 *    This example shows how to access all the joints of a given body.
"""
from fisica import Fisica, FWorld, FCircle, FDistanceJoint, FJoint
add_library('fisica')

body_color = color(0x6E, 0x05, 0x95)
hover_color = color(0xF5, 0xB5, 0x02)
spider_count = 10
main_size = 40
leg_count = 10
leg_size = 100

world = None
mains = []


def setup():
    global world
    size(400, 400)
    smooth()
    Fisica.init(this)
    world = FWorld()
    world.set_edges()
    world.set_gravity(0, 0)
    for _ in range(spider_count):
        create_spider()


def draw():
    background(255)
    world.step()
    world.draw()


def mouse_moved():
    hovered = world.get_body(mouse_x, mouse_y)
    for other in mains:
        if hovered == other:
            set_joints_drawable(other, True)
            set_joints_color(other, hover_color)
        else:
            set_joints_drawable(other, False)
            set_joints_color(other, body_color)


def key_pressed():
    save_frame("screenshot.png")


def create_spider():
    pos_x = random(main_size/2, width-main_size/2)
    pos_y = random(main_size/2, height-main_size/2)
    main = FCircle(main_size)
    main.set_position(pos_x, pos_y)
    main.set_velocity(random(-20, 20), random(-20, 20))
    main.set_fill_color(body_color)
    main.set_no_stroke()
    main.set_group_index(2)
    world.add(main)
    mains.append(main)
    for i in range(leg_count):
        x = leg_size * cos(i*TWO_PI/3) + pos_x
        y = leg_size * sin(i*TWO_PI/3) + pos_y
        leg = FCircle(main_size/2)
        leg.set_position(pos_x, pos_y)
        leg.set_velocity(random(-20, 20), random(-20, 20))
        leg.set_fill_color(body_color)
        leg.set_no_stroke()
        world.add(leg)
        j = FDistanceJoint(main, leg)
        j.set_length(leg_size)
        j.set_no_stroke()
        j.set_stroke(0)
        j.set_fill(0)
        j.set_drawable(False)
        j.set_frequency(0.1)
        world.add(j)


def set_joints_color(b, c):
    for j in b.get_joints():
        j.set_stroke_color(c)
        j.set_fill_color(c)
        j.get_body1().set_fill_color(c)
        j.get_body2().set_fill_color(c)


def set_joints_drawable(b, c):
    for j in b.get_joints():
        j.set_drawable(c)
