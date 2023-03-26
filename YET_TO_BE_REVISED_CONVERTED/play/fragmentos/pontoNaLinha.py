"""
 Code from Andreas Schlegel / http://www.sojamo.de
 posted on https://processing.org/discourse/beta/num_1247920826.html
 ported to Python Mode by Alexandre Villares / http://abav.lugaralgum.com
"""


def setup():
    global p1, p2, mouse
    size(400, 400)
    mouse = Py5Vector()
    p1 = Py5Vector(100, 100)
    p2 = Py5Vector(200, 200)


def draw():
    background(0)
    stroke(255)
    mouse.set(mouse_x, mouse_y)
    if(point_inside_line(mouse, p1, p2, 4)):
        stroke(0, 255, 0)
    line(p1.x, p1.y, p2.x, p2.y)


def point_inside_line(
        the_point,
        the_line_end_point1,
        the_line_end_point2,
        the_tolerance):
    """
    """
    dir = Py5Vector(the_line_end_point2.x, the_line_end_point2.y)
    dir -= the_line_end_point1
    diff = Py5Vector(the_point.x, the_point.y)
    diff -= the_line_end_point1
    # inside distance determines the weighting
    # between linePoint1 and linePoint2
    inside_distance = diff.dot(dir) / dir.dot(dir)
    if(inside_distance > 0 and inside_distance < 1):
        # thePois inside/close to
        # the line if insideDistance>0 or <1
        closest = Py5Vector(the_line_end_point1.x, the_line_end_point1.y)
        dir *= inside_distance
        closest += dir
        d = Py5Vector(the_point.x, the_point.y)
        d -= closest
        distsqr = d.dot(d)
        # check the distance of thePoto the line against our tolerance.
        return (distsqr < pow(the_tolerance, 2))
    return False
