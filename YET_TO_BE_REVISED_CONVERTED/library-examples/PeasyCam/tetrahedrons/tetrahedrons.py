""" Tetrahedrons + PeasyCam"""

add_library('peasycam')

T_LIST, ROT_X, ROT_Y = [], 0, 0
X_MIN, X_MAX = -300, 300
Y_MIN, Y_MAX = -300, 300
Z_MIN, Z_MAX = -300, 300


def setup():
    cam = PeasyCam(this, 500)  # Drag mouse to orbit, scroll to zoom
    # cam.setMaximumDistance(250);
    # cam.setMaximumDistance(1000);
    # hint(DISABLE_DEPTH_TEST)
    size(800, 800, P3D)
    for _ in range(100):
        x = random(X_MIN, X_MAX)
        y = random(Y_MIN, Y_MAX)
        z = random(Z_MIN, Z_MAX)
        T_LIST.append(Tetrahedron(x, y, z, 50))  # 50 is the radius/size


def draw():
    global ROT_X, ROT_Y
    ROT_X += 0.005
    ROT_Y += 0.01
    background(0)
    stroke_weight(7)
    for tetra in T_LIST:
        # Draws only edges, or only faces if a key is pressed
        tetra.plot(ROT_X, ROT_Y, key_pressed)


class Tetrahedron():

    """ Tetrahedron """

    def __init__(self, x, y, z, radius):
        self.x, self.y, self.z = x, y, z
        self.radius = radius
        self.points = []
        # calculate geometry
        a = radius * 2 / 3.
        self.points.append(Py5Vector(+a, +a, +a))  # vertex 1
        self.points.append(Py5Vector(-a, -a, +a))  # vertex 2
        self.points.append(Py5Vector(-a, +a, -a))  # vertex 3
        self.points.append(Py5Vector(+a, -a, -a))  # vertex 4

    # draws tetrahedron
    def plot(self, rx=0, ry=0, show_faces=False):
        c = color(map(self.x, X_MIN, X_MAX, 255, 0),
                  map(self.y, Y_MIN, Y_MAX, 255, 0),
                  map(self.z, Z_MIN, Z_MAX, 0, 255), 100)
        if show_faces:
            no_stroke()
            fill(c)
        else:
            no_fill()
            stroke(c)
        with push_matrix():
            translate(self.x, self.y, self.z)
            rotate_x(ry)
            rotate_y(rx)
            begin_shape(TRIANGLE_STRIP)
            p = self.points
            vertex(p[0].x, p[0].y, p[0].z)  # vertex 1
            vertex(p[1].x, p[1].y, p[1].z)  # vertex 2
            vertex(p[2].x, p[2].y, p[2].z)  # vertex 3
            vertex(p[3].x, p[3].y, p[3].z)  # vertex 4
            vertex(p[0].x, p[0].y, p[0].z)  # vertex 1
            vertex(p[1].x, p[1].y, p[1].z)  # vertex 2
            vertex(p[3].x, p[3].y, p[3].z)  # vertex 4
            vertex(p[2].x, p[2].y, p[2].z)  # vertex 3
            vertex(p[1].x, p[1].y, p[1].z)  # vertex 2
            end_shape(CLOSE)
