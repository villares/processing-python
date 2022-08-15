# Ported from Code found in Chrisir's post:
# https://forum.processing.org/two/discussion/21400/how-to-rotate-a-3d-line-like-a-2d-line

def setup():
    size(640, 360, P3D)


def draw():
    background(0)
    lights()
    with push_matrix():
        # a vector that points to the mouse location
        mouse = Py5Vector(mouse_x, mouse_y, 0)
        stroke(255)
        sq_section_bar(220, 220, -220,
                       mouse.x, mouse.y, mouse.z,
                       10)


def sq_section_bar(x1, y1, z1,
                   x2, y2, z2,
                   weight):
    """
    drawLine programmed by James Carruthers
    http://processing.org/discourse/yabb2/YaBB.pl?num=1262458611/0#9
    """
    p1 = Py5Vector(x1, y1, z1)
    p2 = Py5Vector(x2, y2, z2)
    v1 = Py5Vector(x2 - x1, y2 - y1, z2 - z1)
    rho = sqrt(v1.x ** 2 + v1.y ** 2 + v1.z ** 2)
    phi = acos(v1.z / rho)
    the = atan2(v1.y, v1.x)
    v1 *= 0.5

    with push_matrix():
        translate(x1, y1, z1)
        translate(v1.x, v1.y, v1.z)
        rotate_z(the)
        rotate_y(phi)
        no_stroke()
        # box(weight,weight,p1.dist(p2)*1.2)
        box(weight, weight, p1.dist(p2) * 1.0)
