""" Click on the sketch to pause and restart """

paused = False


def setup():
    size(100, 100)


def draw():
    background(0)
    text(str(frame_count), 5, 15)


def mouse_clicked():
    global paused
    paused = not paused
    if paused:
        no_loop()
    else:
        loop()
