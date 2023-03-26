"""
/**
 *  Contacts
 *
 *  by Ricard Marxer
 *
 *  This example shows how to use the contact events.
 */
"""
import fisica
add_library('fisica')

world = None
obstacle = None


def setup():
    global world, obstacle
    size(400, 400)
    smooth()

    fisica._fisica.init(this)

    world = fisica.f_world()

    obstacle = fisica.f_box(150, 150)
    obstacle.set_rotation(PI/4)
    obstacle.set_position(width/2, height/2)
    obstacle.set_static(True)
    obstacle.set_fill(0)
    obstacle.set_restitution(0)
    world.add(obstacle)


def draw():
    background(255)

    if frame_count % 5 == 0:
        b = fisica.f_circle(20)
        b.set_position(width/2 + random(-50, 50), 50)
        b.set_velocity(0, 200)
        b.set_restitution(0)
        b.set_no_stroke()
        b.set_fill(200, 30, 90)
        world.add(b)

    world.draw()
    world.step()

    stroke_weight(1)
    stroke(255)
    for c in obstacle.get_contacts():
        line(
            c.get_body1().get_x(),
            c.get_body1().get_y(),
            c.get_body2().get_x(),
            c.get_body2().get_y())


def contact_started(c):
    ball = None
    if c.get_body1() == obstacle:
        ball = c.get_body2()
    elif c.get_body2() == obstacle:
        ball = c.get_body1()
    if ball:
        ball.set_fill(30, 190, 200)


def contact_persisted(c):
    ball = None
    if c.get_body1() == obstacle:
        ball = c.get_body2()
    elif c.get_body2() == obstacle:
        ball = c.get_body1()
    if not ball:
        return

    ball.set_fill(30, 120, 200)
    no_stroke()
    fill(255, 220, 0)
    ellipse(c.get_x(), c.get_y(), 10, 10)


def contact_ended(c):
    ball = None
    if c.get_body1() == obstacle:
        ball = c.get_body2()
    elif c.get_body2() == obstacle:
        ball = c.get_body1()
    if ball:
        ball.set_fill(200, 30, 90)


def key_pressed():
    save_frame("screenshot.png")
