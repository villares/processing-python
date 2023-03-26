TOLERANCE = EPSILON


def setup():
    global p1, p2, mouse
    size(500, 500)
    background(0)
    no_smooth()


def draw():
    s = 2  # scale factor
    scale(s)
    mouse = Py5Vector(mouse_x, mouse_y) / s

    stroke(255)
    p1 = Py5Vector(50, 50)
    p2 = Py5Vector(150, 150)
    if point_inside_line(mouse, p1, p2,
                         TOLERANCE):
        stroke(255, 0, 0)
        point(mouse.x, mouse.y)
        stroke(0, 255, 0)
    line(p1.x, p1.y, p2.x, p2.y)

    stroke(255)
    p1x, p1y = 50, 100
    p2x, p2y = 150, 200
    if point_over_line(mouse.x, mouse.y,
                       p1x, p1y, p2x, p2y,
                       tolerance=TOLERANCE):
        stroke(255, 0, 0)
        point(mouse.x, mouse.y)
        stroke(0, 0, 255)
    line(p1x, p1y, p2x, p2y)


def point_over_line(px, py, lax, lay, lbx, lby,
                    tolerance=EPSILON):
    """
    Check if point is over line using the sum of
    the distances from the point to the line ends
    (the result has to be near equal for True).
    """
    ab = dist(lax, lay, lbx, lby)
    pa = dist(lax, lay, px, py)
    pb = dist(px, py, lbx, lby)
    return (pa + pb) <= ab + tolerance / 100.0


def points_are_colinear(ax, ay, bx, by, cx, cy,
                        tolerance=EPSILON):
    """
    Test for colinearity by calculating the area
    of a triangle formed by the 3 points.
    """
    area = triangle_area((ax, ay), (bx, by), (cx, cy))
    return abs(area) < tolerance


def triangle_area(p0, p1, p2):
    a = (p1[0] * (p2[1] - p0[1]) +
         p2[0] * (p0[1] - p1[1]) +
         p0[0] * (p1[1] - p2[1]))
    return a


def point_inside_line(
        the_point,
        the_line_end_point1,
        the_line_end_point2,
        the_tolerance=2):
    """
    Code from Andreas Schlegel / http://www.sojamo.de
    posted on https://processing.org/discourse/beta/num_1247920826.html
    ported to Python Mode by Alexandre Villares / http://abav.lugaralgum.com
    """
    dir = Py5Vector(the_line_end_point2.x, the_line_end_point2.y)
    dir -= the_line_end_point1
    diff = Py5Vector(the_point.x, the_point.y)
    diff -= the_line_end_point1
    # inside distance determines the weighting
    # between linePoint1 and linePoint2
    inside_distance = diff.dot(dir) / dir.dot(dir)
    if(inside_distance > 0 and inside_distance < 1):
        # the point is inside/close to
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
