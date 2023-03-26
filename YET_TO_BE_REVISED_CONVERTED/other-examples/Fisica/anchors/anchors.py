"""
 *    Anchors and the bridge by Ricard Marxer
 *
 *    This example shows the use of anchors and distance joints in order
 *    to create a bridge.
 """
from fisica import Fisica, FBody, FBox, FWorld, FCircle, FDistanceJoint
add_library('fisica')

frequency = 5
damping = 1
puente_y = None
step_count = 20
steps = []
world = []
box_width = 400/step_count - 2


def setup():
    global puente_y, world

    size(400, 400)
    smooth()
    puente_y = height/3
    Fisica.init(this)
    world = FWorld()
    bola = FCircle(40)
    bola.set_position(width/3, puente_y-10)
    bola.set_density(0.2)
    bola.set_fill(120, 120, 190)
    bola.set_no_stroke()
    world.add(bola)
    for i in range(step_count):
        box = FBox(box_width, 10)
        box.set_position(map(i, 0, step_count - 1, box_width,
                         width-box_width), puente_y)
        box.set_no_stroke()
        box.set_fill(120, 200, 190)
        world.add(box)
        steps.append(box)
    for i in range(1, step_count):
        junta = FDistanceJoint(steps[i-1], steps[i])
        junta.set_anchor1(box_width/2, 0)
        junta.set_anchor2(-box_width/2, 0)
        junta.set_frequency(frequency)
        junta.set_damping(damping)
        junta.set_fill(0)
        junta.calculate_length()
        world.add(junta)
    left = FCircle(10)
    left.set_static(True)
    left.set_position(0, puente_y)
    left.set_drawable(False)
    world.add(left)
    right = FCircle(10)
    right.set_static(True)
    right.set_position(width, puente_y)
    right.set_drawable(False)
    world.add(right)
    junta_principio = FDistanceJoint(steps[0], left)
    junta_principio.set_anchor1(-box_width/2, 0)
    junta_principio.set_anchor2(0, 0)
    junta_principio.set_frequency(frequency)
    junta_principio.set_damping(damping)
    junta_principio.calculate_length()
    junta_principio.set_fill(0)
    world.add(junta_principio)
    junta_final = FDistanceJoint(steps[step_count-1], right)
    junta_final.set_anchor1(box_width/2, 0)
    junta_final.set_anchor2(0, 0)
    junta_final.set_frequency(frequency)
    junta_final.set_damping(damping)
    junta_final.calculate_length()
    junta_final.set_fill(0)
    world.add(junta_final)


def draw():
    background(255)
    world.step()
    world.draw()


def mouse_pressed():
    radius = random(10, 40)
    bola = FCircle(radius)
    bola.set_position(mouse_x, mouse_y)
    bola.set_density(0.2)
    bola.set_fill(120, 120, 190)
    bola.set_no_stroke()
    world.add(bola)


def key_pressed():
    save_frame("screenshot.png")
