"""
Giving variable thickness to a line (calculating normals), based on code by Hamoid at:
https://discourse.processing.org/t/giving-variable-thickness-to-a-line-calculating-normals/5890
"""
from itertools import chain

pts = (
    Py5Vector(61, 183),
    Py5Vector(108, 113),
    Py5Vector(193, 118),
    Py5Vector(256, 158),
    Py5Vector(248, 239),
    Py5Vector(258, 310),
    Py5Vector(328, 353),
    Py5Vector(377, 341),
    )

def setup():
    size(400, 400)
    calculate()

def draw():
    background(255)
    # draw calculated thick line
    if is_mouse_pressed:
        stroke(0)
    else:
        no_stroke()
    fill("#FFCC00")
    with begin_shape(QUAD_STRIP):
        vertices(tuple(chain.from_iterable((p + n, p - n)
                                            for p, n in zip(pts, normals))))
#         for (p, n) in zip(pts, normals):
#             vertex(p.x + n.x, p.y + n.y)
#             vertex(p.x - n.x, p.y - n.y)
    # draw the original line
    stroke("#552200")
    no_fill()
    with begin_shape():
        vertices(pts)

    # draw line vertices
    stroke("#552200")
    stroke_weight(2)
    fill(255)
    for p in pts:
        ellipse(p.x, p.y, 6, 6)

    # draw contour pts
    # noStroke()
    stroke(0)
    fill("#883300")
    for (p, n) in zip(pts, normals):
        ellipse(p.x + n.x, p.y + n.y, 3, 3)
        ellipse(p.x - n.x, p.y - n.y, 3, 3)

def calculate():
    global normals
    # 2. calculations
    # Ensure normals has the same size as pts
    normals = [Py5Vector(0, 0)] * len(pts)
    # Calculate normals
    for i in range(len(pts) - 1):
        # sub = pts[i] - pts[i + 1]
        sub = pts[i] - pts[i + 1]
        normals[i] = Py5Vector(-sub.y, sub.x)
    for i in range(1, len(pts)):
        # sub = pts[i] - pts[i - 1]
        # normals[i] += PVector(sub.y, -sub.x)
        sub = pts[i] - pts[i - 1]
        normals[i] += Py5Vector(sub.y, -sub.x)
    # Resize normals
    for n in normals:
        n.normalize()
        n *= random(10, 30)

def key_pressed():
    calculate()
