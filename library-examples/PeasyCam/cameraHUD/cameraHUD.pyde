<<<<<<< HEAD:library-examples/PeasyCam/cameraHUD/cameraHUD.py
""" PeasyCam provides a dead-simple mouse-driven camera for Processing.
    full documentation at http://mrfeinberg.com/peasycam/
"""
from peasy import PeasyCam
=======
from java.lang import System 
System.setProperty("jogl.disable.openglcore", "false") 

""" PeasyCam provides a dead-simple mouse-driven camera for Processing.
    full documentation at http://mrfeinberg.com/peasycam/
"""

add_library('peasycam')
>>>>>>> parent of 0d73f95 (first conversion):library-examples/PeasyCam/cameraHUD/cameraHUD.pyde

def setup():
    global cam
    size(200, 200, P3D)
<<<<<<< HEAD:library-examples/PeasyCam/cameraHUD/cameraHUD.py
    this = get_current_sketch()
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(50)
    cam.setMaximumDistance(500)

=======
    camera = PeasyCam(this, 100)
    camera.setMinimumDistance(50)
    camera.setMaximumDistance(500)
>>>>>>> parent of 0d73f95 (first conversion):library-examples/PeasyCam/cameraHUD/cameraHUD.pyde

def draw():
    rotateX(-.5)
    rotateY(-.5)
    background(0)
    fill(255, 0, 0)
    box(30)
    with pushMatrix():
        translate(0, 0, 20)
        fill(0, 0, 255)
        box(5)
<<<<<<< HEAD:library-examples/PeasyCam/cameraHUD/cameraHUD.py
    cam.beginHUD()  # start drawing relative to the camera view
    fill(255)
    rect(20, 10, 120, 30)
    fill(0)
    text(str(get_frame_rate()), 30, 30)
    cam.endHUD()  # and don't forget to stop/close with this!
=======
    camera.beginHUD()  # start drawing relative to the camera view
    fill(255)
    rect(20, 10, 120, 30)
    fill(0)
    text(str(frameRate), 30, 30)
    camera.endHUD()  # and don't forget to stop/close with this!
>>>>>>> parent of 0d73f95 (first conversion):library-examples/PeasyCam/cameraHUD/cameraHUD.pyde
