"""
 * Many Stars
 * (c)2018 Alexandre B A Villares
 * https://abav.lugaralgum.com
"""

STAR_LIST = []


def setup():
    size(800, 800, P3D)
    no_fill()
    stroke_weight(5)
    for i in range(100):
        x, y = random(width), random(height)
        new_star = Star(
            x, y, random(
                20, 60), random(
                50, 120), int(
                random(
                    3, 30)))
        STAR_LIST.append(new_star)


def draw():
    background(0)
    for star in STAR_LIST:
        star.plot()


class Star():

    def __init__(self, x, y, radius1, radius2, npoints):
        self.x, self.y = x, y
        self.radius1, self.radius2 = radius1, radius2
        self.angle = TWO_PI / npoints
        self.half_angle = self.angle / 2.0
        self.color = color(random(256), random(256), random(256), 120)

    def plot(self):
        with push_matrix():
            translate(self.x, self.y)
            rotate(frame_count / 100.0)
            stroke(self.color)
            self.radius3 = 5 + self.radius2 * sin(frame_count / 100.0)
            begin_shape()
            a = 0
            while a < TWO_PI:
                sx = cos(a) * self.radius3
                sy = sin(a) * self.radius3
                vertex(sx, sy)
                sx = cos(a + self.half_angle) * self.radius1
                sy = sin(a + self.half_angle) * self.radius1
                vertex(sx, sy)
                a += self.angle
            end_shape(CLOSE)
