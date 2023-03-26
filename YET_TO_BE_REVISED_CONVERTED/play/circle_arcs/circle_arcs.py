def setup():
    """
    Testing some simplified arc from circle syntax
    PI, HALF_PI, TOP, LEFT etc are Processing defined constants
    """

    circle_arc(5, 5, 25, 0, HALF_PI)
    half_circle(60, 5, 25, DOWN)
    quarter_circle(95, 95, 25, TOP+LEFT)


def quarter_circle(x, y, radius, quadrant):
    ROTATION = {0: 0,
                BOTTOM + RIGHT: 0,
                DOWN + RIGHT: 0,
                1: HALF_PI,
                DOWN + LEFT: HALF_PI,
                BOTTOM + LEFT: HALF_PI,
                2: PI,
                TOP + LEFT: PI,
                UP + LEFT: PI,
                3: PI + HALF_PI,
                TOP + RIGHT: PI + HALF_PI,
                UP + RIGHT: PI + HALF_PI,
                }
    circle_arc(x, y, radius, ROTATION[quadrant], HALF_PI)


def half_circle(x, y, radius, quadrant):
    ROTATION = {0: 0,
                BOTTOM: 0,
                DOWN: 0,
                1: HALF_PI,
                LEFT: HALF_PI,
                2: PI,
                TOP: PI,
                UP: PI,
                3: PI + HALF_PI,
                RIGHT: PI + HALF_PI,
                }
    circle_arc(x, y, radius, ROTATION[quadrant], PI)


def circle_arc(x, y, radius, start_ang, sweep_ang):
    arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang)
