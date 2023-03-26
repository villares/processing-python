def setup():
    rect_mode(CENTER)
    size(200, 200)
    rect_rot(100, 100, QUARTER_PI, 50, 20)
    ellipse(100, 100, 10, 10)


def rect_rot(x, y, ang, *args):
    """
    x, y, angle, width, height
    and optional corner radius
    like the original rect()
    """
    with push_matrix():
        translate(x, y)
        rotate(ang)
        rect(0, 0, *args)
