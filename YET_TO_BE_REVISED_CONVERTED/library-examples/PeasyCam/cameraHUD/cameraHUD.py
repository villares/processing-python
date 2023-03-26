from java.lang import System
from peasy import PeasyCam
<< << << < HEAD: library-examples/PeasyCam/camera_hud/camera_hud.py
""" PeasyCam provides a dead-simple mouse-driven camera for Processing.
    full documentation at http://mrfeinberg.com/peasycam/
"""
== == == =
System.setProperty("jogl.disable.openglcore", "false")

""" PeasyCam provides a dead-simple mouse-driven camera for Processing.
    full documentation at http://mrfeinberg.com/peasycam/
"""

add_library('peasycam')
>>>>>> > parent of 0d73f95(first conversion): library-examples/PeasyCam/camera_hud/camera_hud.pyde


def setup():
    global cam
    size(200, 200, P3D)


<< << << < HEAD: library-examples/PeasyCam/camera_hud/camera_hud.py
this = get_current_sketch()
cam = PeasyCam(this, 100)
cam.set_minimum_distance(50)
cam.set_maximum_distance(500)

== == == =
camera = PeasyCam(this, 100)
camera.set_minimum_distance(50)
camera.set_maximum_distance(500)
>>>>>> > parent of 0d73f95(first conversion): library-examples/PeasyCam/camera_hud/camera_hud.pyde


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


<< << << < HEAD: library-examples/PeasyCam/camera_hud/camera_hud.py
cam.begin_hud()  # start drawing relative to the camera view
fill(255)
rect(20, 10, 120, 30)
fill(0)
text(str(get_frame_rate()), 30, 30)
cam.end_hud()  # and don't forget to stop/close with this!
== == == =
camera.begin_hud()  # start drawing relative to the camera view
fill(255)
rect(20, 10, 120, 30)
fill(0)
text(str(frame_rate), 30, 30)
camera.end_hud()  # and don't forget to stop/close with this!
>>>>>> > parent of 0d73f95(first conversion): library-examples/PeasyCam/camera_hud/camera_hud.pyde
