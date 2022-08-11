from java.lang import System
System.setProperty("jogl.disable.openglcore", "false")
"""
  Shape Transform
  by Ira Greenberg.
  (Rewritten in Python by Jonathan Feinberg.)

  Illustrates the geometric relationship
  between Cube, Pyramid, Cone and
  Cylinder 3D primitives.

  Instructions:
  Up Arrow - increases points
  Down Arrow - decreases points
  'p' key toggles between cube/pyramid
 """

# constants
radius = 99
cylinder_length = 95
angle_inc = PI / 300.0

# globals that can be chaned by the user
pts = 12
is_pyramid = False


def setup():
    size(640, 360, OPENGL)
    no_stroke()


def draw():
    background(170, 95, 95)
    lights()
    fill(255, 200, 200)
    translate(width / 2, height / 2)
    rotate_x(frame_count * angle_inc)
    rotate_y(frame_count * angle_inc)
    rotate_z(frame_count * angle_inc)

    d_theta = TWO_PI / pts
    def x(j): return cos(d_theta * j) * radius
    def y(j): return sin(d_theta * j) * radius

    # draw cylinder tube
    begin_shape(QUAD_STRIP)
    for j in range(pts + 1):
        vertex(x(j), y(j), cylinder_length)
        if is_pyramid:
            vertex(0, 0, -cylinder_length)
        else:
            vertex(x(j), y(j), -cylinder_length)
    end_shape()
    # draw cylinder ends
    begin_shape()
    for j in range(pts + 1):
        vertex(x(j), y(j), cylinder_length)
    end_shape(CLOSE)
    if not is_pyramid:
        begin_shape()
        for j in range(pts + 1):
            vertex(x(j), y(j), -cylinder_length)
        end_shape(CLOSE)


"""
 up/down arrow keys control
 polygon detail.
 """


def key_pressed():
    global pts, is_pyramid
    if key == CODED:
        if key_code == UP and pts < 90:
            pts += 1
        elif key_code == DOWN and pts > 4:
            pts -= 1
    elif key == 'p':
        is_pyramid = not is_pyramid
