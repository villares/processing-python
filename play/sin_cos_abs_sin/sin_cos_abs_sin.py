def setup():
    size(1024, 300)
    # blendMode(ADD)
    background(0)


def draw():
    translate(-100, height/2, 0)
    scale(3, -1, 1)
    ang = frame_count / 30.
    stroke(255, 0, 0)
    line(frame_count, height/2, frame_count, height/2 + sin(ang) * 100)
    stroke(0, 255, 0)
    line(frame_count, height/2, frame_count, height/2 + cos(ang) * 100)
    stroke(0, 0, 255)
    line(frame_count, height/2, frame_count, height/2 + abs(sin(ang)) * 100)

    if ang > width:
        no_loop()
