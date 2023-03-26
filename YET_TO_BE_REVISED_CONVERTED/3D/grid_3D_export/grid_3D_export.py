"""
A funny wobbling 3D grid - by Alexandre B A Villares (abav.lugaralgum.com)
1. install Processing (processing.org)
2. install Python Mode (isntructions on py.processing.org)
3. install PeasyCam library under Sketch...>Import Libray...>Add Library...
"""

add_library('peasycam')  # Drag the mouse to orbit!
add_library('gifAnimation')

ANG = 0
RANGE = 8
NUM_BOXES = RANGE ** 3
BOXES = [()] * NUM_BOXES
S_SIZE = 5  # Controls the spacing of the grid
B_SIZE = 5   # B_SIZE <= box_size < B_SIZE * 2
SLIDE = 5    # Changes the sliding behaviour
SPEED = 0.01  # Increments ANG
GIF_EXPORT = False


def setup():
    # hint(ENABLE_DEPTH_SORT)
    # fullScreen(1)
    size(600, 600, P3D)
    cam = PeasyCam(this, 110)
    cam.set_minimum_distance(110)
    cam.set_maximum_distance(110)
    on_grid(set_boxes, BOXES)
    stroke_weight(2)


def draw():
    global ANG, SAVE_FRAME

    background(0)
    on_grid(plot_boxes, BOXES)

    if True:  # was mousePressed:
        ANG += SPEED

    global GIF_EXPORT
    if not frame_count % 20 and GIF_EXPORT:
        GIF_EXPORT = gif_export(GifMaker,
                                frames=1000,
                                delay=300,
                                filename="grid_3D")


def on_grid(func, L):
    n = 0
    for i in range(RANGE):
        for j in range(RANGE):
            for k in range(RANGE):
                func(i, j, k, n, L)
                n += 1


def set_boxes(x, y, z, n, L):
    r = map(x, 0, RANGE, 1, 255)
    g = map(y, 0, RANGE, 1, 255)
    b = map(z, 0, RANGE, 1, 255)
    box_size = random(B_SIZE, B_SIZE * 2)
    L[n] = (color(r, g, b), box_size)


def plot_boxes(x, y, z, n, L):
    box_color, box_size = L[n]
    no_fill()
    # noStroke()
    stroke(box_color)
    with push_matrix():
        translate(x * S_SIZE * sin(ANG + x * SLIDE),
                  y * S_SIZE * sin(ANG + y * SLIDE),
                  z * S_SIZE * sin(ANG + z * SLIDE)
                  )
        box(box_size)


def key_pressed():
    global GIF_EXPORT
    GIF_EXPORT = True


"""
Alexandre B A Villares http://abav.lugaralgum.com - GPL v3

A helper for the Processing gifAnimation library (https://github.com/jordanorelli)
ported to Processing 3 by 01010101 (https://github.com/01010101)
Download the library from https://github.com/01010101/GifAnimation/archive/master.zip
This helper was inspired by an example by Art Simon https://github.com/APCSPrinciples/AnimatedGIF/

Put  at the start of your sketch:
   add_library('gifAnimation')
   from gif_exporter import gif_export
and at the end of draw():
    gif_export(GifMaker)
"""


def gif_export(GifMaker,             # gets a reference to the library
               filename="exported",  # .gif will be added
               repeat=0,             # 0 makes it an "endless" animation
               quality=182,          # quality range 0 - 255
               delay=170,            # this is quick
               frames=0):            # 0 will stop on keyPressed or frameCount >= 100000
    global gif_exporter
    try:
        gif_exporter
    except NameError:
        gif_exporter = GifMaker(this, filename + ".gif")
        gif_exporter.set_repeat(repeat)
        gif_exporter.set_quality(quality)
        gif_exporter.set_delay(delay)
        gif_export._frame = frame_count
        print("gif start")

    gif_exporter.add_frame()

    if (frames == 0 and key_pressed or frame_count - gif_export._frame >=
            100000) or (frames != 0 and frame_count - gif_export._frame >= frames):
        gif_exporter.finish()
        background(255)
        print("gif saved")
        del(gif_exporter)
        return False
    else:
        return True
