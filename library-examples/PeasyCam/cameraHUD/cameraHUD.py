from java.lang import System
System.setProperty("jogl.disable.openglcore", "false")

""" PeasyCam provides a dead-simple mouse-driven camera for Processing.
    full documentation at http://mrfeinberg.com/peasycam/
"""

add_library('peasycam')


def setup():
    global camera
    size(200, 200, P3D)
    camera = PeasyCam(this, 100)
    camera.set_minimum_distance(50)
    camera.set_maximum_distance(500)


def draw():
    rotate_x(-.5)
    rotate_y(-.5)
    background(0)
    fill(255, 0, 0)
    box(30)
    with push_matrix():
        translate(0, 0, 20)
        fill(0, 0, 255)
        box(5)
    camera.begin_hud()  # start drawing relative to the camera view
    fill(255)
    rect(20, 10, 120, 30)
    fill(0)
    text(str(frame_rate), 30, 30)
    camera.end_hud()  # and don't forget to stop/close with this!
