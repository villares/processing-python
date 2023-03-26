"""
Ortho vs Perspective.

Click to see the difference between orthographic projection
and perspective projection as applied to a simple box.
The ortho() function sets an orthographic projection and
defines a parallel clipping volume. All objects with the
same dimension appear to be the same size, regardless of whether
they are near or far away from the camera. The parameters to this
function specify the clipping volume where left and right
are the minimum and maximum x values respectively,
top and bottom are the minimum and maximum y values respectively,
and lastly, the near and far are the minimum and maximum z values.
 """
show_perspective = True


def setup():
    size(640, 360, P3D)
    fill(204)
    no_stroke()


def draw():
    lights()
    background(0)
    far = map(mouse_x, 0, width, 120, 400)
    if show_perspective:
        perspective(THIRD_PI, float(width) / height, 10, far)
    else:
        ortho(0, width, 0, height, 10, far)

    translate(width / 2, height / 2, 0)
    rotate_x(-0.5 * THIRD_PI)
    rotate_y(THIRD_PI)
    box(160)


def mouse_pressed():
    global show_perspective
    show_perspective = not show_perspective
