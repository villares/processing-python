"""
 *    Droppings Remade
 *
 *    This example shows how to create a simple remake of my favorite
 *    soundtoy:<br/>
 *
 *        <a href=http:#www.balldroppings.com/>BallDroppings</a>
 *             by Josh Nimoy.
 """
from fisica import FWorld, Fisica, FCircle, FBody, FBox
add_library('fisica')

mundo, caja = None, None
x, y = 0, 0


def setup():
    global mundo
    size(400, 400)
    smooth()

    Fisica.init(this)
    mundo = FWorld()
    mundo.set_gravity(0, 200)

    frame_rate(24)
    background(0)


def draw():
    fill(0, 100)
    no_stroke()
    rect(0, 0, width, height)
    if frame_count % 24 == 0:
        bolita = FCircle(8)
        bolita.set_no_stroke()
        bolita.set_fill(255)
        bolita.set_position(100, 20)
        bolita.set_velocity(0, 400)
        bolita.set_restitution(0.9)
        bolita.set_damping(0)
        mundo.add(bolita)
    mundo.step()
    mundo.draw(this)


def mouse_pressed():
    global caja, x, y
    caja = FBox(4, 4)
    caja.set_static_body(True)
    caja.set_stroke(255)
    caja.set_fill(255)
    caja.set_restitution(0.9)
    mundo.add(caja)

    x = mouse_x
    y = mouse_y


def mouse_dragged():
    if not caja:
        return
    ang = atan2(y - mouse_y, x - mouse_x)
    caja.set_rotation(ang)
    caja.set_position(x+(mouse_x-x)/2.0, y+(mouse_y-y)/2.0)
    caja.set_width(dist(mouse_x, mouse_y, x, y))


def contact_started(contacto):
    cuerpo1 = contacto.get_body1()
    cuerpo1.set_fill(255, 0, 0)
    cuerpo1.set_stroke(255, 0, 0)

    no_fill()
    stroke(255)
    ellipse(contacto.get_x(), contacto.get_y(), 30, 30)


def contact_ended(contacto):
    cuerpo1 = contacto.get_body1()
    cuerpo1.set_fill(255)
    cuerpo1.set_stroke(255)


def key_pressed():
    save_frame("screenshot.png")
