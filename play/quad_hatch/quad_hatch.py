def hatch_points(points, divisions, *sides):
    if not sides:
        sides = [0]
    for s in sides:
        a, b = points[-1 + s], points[+0 + s]
        d, c = points[-2 + s], points[-3 + s]
        for i in range(1, divisions):
            n = float(divisions)
            s0 = PVector.lerp(a, b, i / n)
            s1 = PVector.lerp(d, c, i / n)
            line(s0.x, s0.y, s1.x, s1.y)


def exp_hatch_points(points, divisions, *sides):
    if not sides:
        sides = [0]
    for s in sides:
        a, b = points[-1 + s], points[+0 + s]
        d, c = points[-2 + s], points[-3 + s]
        for i in range(1, divisions * divisions):
            s0 = PVector.lerp(a, b, sqrt(i) / divisions)
            s1 = PVector.lerp(d, c, sqrt(i) / divisions)
            line(s0.x, s0.y, s1.x, s1.y)


def setup():
    size(400, 400)
    init_points()


def key_pressed():
    init_points()
    loop()


def init_points():
    global points
    pos = [(-1, -1), (+1, -1), (+1, +1), (-1, +1)]
    points = [Py5Vector(x * 100 + random(-50, 50), y * 100 + random(-50, 50))
              for x, y in pos]


def draw():
    if not mouse_pressed:
        background(200)
    translate(width / 2, height / 2)
    no_fill()
    stroke_weight(2)
    begin_shape()
    for p in points:
        vertex(p.x, p.y)
    end_shape(CLOSE)
    stroke_weight(1)

    if key == "e":
        exp_hatch_points(points, 8)
    else:
        hatch_points(points, 8)
    no_loop()
