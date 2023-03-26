add_library('peasycam')


def setup():
    global cam
    size(200, 200, P3D)
    cam = PeasyCam(this, 100)
    cam.set_minimum_distance(50)
    cam.set_maximum_distance(500)


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
