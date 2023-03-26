"""
 * RGB Cube.
 *
 * The three primary colors of the additive color model are red, green, and blue.
 * This RGB color cube displays smooth transitions between these colors.
 """

xmag, ymag = (0, 0)
new_xmag, new_ymag = (0, 0)


def setup():
    size(640, 360, P3D)
    no_stroke()
    color_mode(RGB, 1)


def draw():
    global xmag, ymag, new_xmag, new_ymag

    background(0.5)

    push_matrix()
    translate(width / 2, height / 2, -30)

    new_xmag = mouse_x / float(width) * TWO_PI
    new_ymag = mouse_y / float(height) * TWO_PI

    diff = xmag - new_xmag
    if abs(diff) > 0.01:
        xmag -= diff / 4.0

    diff = ymag - new_ymag
    if abs(diff) > 0.01:
        ymag -= diff / 4.0

    rotate_x(-ymag)
    rotate_y(-xmag)

    scale(90)
    begin_shape(QUADS)
    fill(0, 1, 1)
    vertex(-1, 1, 1)
    fill(1, 1, 1)
    vertex(1, 1, 1)
    fill(1, 0, 1)
    vertex(1, -1, 1)
    fill(0, 0, 1)
    vertex(-1, -1, 1)
    fill(1, 1, 1)
    vertex(1, 1, 1)
    fill(1, 1, 0)
    vertex(1, 1, -1)
    fill(1, 0, 0)
    vertex(1, -1, -1)
    fill(1, 0, 1)
    vertex(1, -1, 1)
    fill(1, 1, 0)
    vertex(1, 1, -1)
    fill(0, 1, 0)
    vertex(-1, 1, -1)
    fill(0, 0, 0)
    vertex(-1, -1, -1)
    fill(1, 0, 0)
    vertex(1, -1, -1)
    fill(0, 1, 0)
    vertex(-1, 1, -1)
    fill(0, 1, 1)
    vertex(-1, 1, 1)
    fill(0, 0, 1)
    vertex(-1, -1, 1)
    fill(0, 0, 0)
    vertex(-1, -1, -1)
    fill(0, 1, 0)
    vertex(-1, 1, -1)
    fill(1, 1, 0)
    vertex(1, 1, -1)
    fill(1, 1, 1)
    vertex(1, 1, 1)
    fill(0, 1, 1)
    vertex(-1, 1, 1)
    fill(0, 0, 0)
    vertex(-1, -1, -1)
    fill(1, 0, 0)
    vertex(1, -1, -1)
    fill(1, 0, 1)
    vertex(1, -1, 1)
    fill(0, 0, 1)
    vertex(-1, -1, 1)

    end_shape()

    pop_matrix()
