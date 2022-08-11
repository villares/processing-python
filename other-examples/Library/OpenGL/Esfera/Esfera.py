"""
 * Esfera
 * by David Pena. (Adapted to Python by Jonathan Feinberg)
 *
 * Distribucion aleatoria uniforme sobre la superficie de una esfera.
"""

# Too slow for original 8000.
cuantos = 4000


class pelo:
    def __init__(self):
        self.z = random(-radio, radio)
        self.phi = random(TWO_PI)
        self.largo = random(1.15, 1.2)
        self.theta = asin(self.z / radio)

    def dibujar(self):
        off = (noise(millis() * 0.0005, sin(self.phi)) - 0.5) * 0.3
        offb = (noise(millis() * 0.0007, sin(self.z) * 0.01) - 0.5) * 0.3

        thetaff = self.theta + off
        phff = self.phi + offb
        x = radio * cos(self.theta) * cos(self.phi)
        y = radio * cos(self.theta) * sin(self.phi)
        z = radio * sin(self.theta)
        msx = screen_x(x, y, z)
        msy = screen_y(x, y, z)

        xo = radio * cos(thetaff) * cos(phff)
        yo = radio * cos(thetaff) * sin(phff)
        zo = radio * sin(thetaff)

        xb = xo * self.largo
        yb = yo * self.largo
        zb = zo * self.largo

        begin_shape(LINES)
        stroke(0)
        vertex(x, y, z)
        stroke(200, 150)
        vertex(xb, yb, zb)
        end_shape()


def setup():
    size(1024, 768, OPENGL)
    global radio, lista, rx, ry
    radio = height / 3.5
    lista = [pelo() for i in range(cuantos)]
    rx, ry = 0.0, 0.0
    noise_detail(3)


def draw():
    background(0)
    translate(width / 2, height / 2)

    rxp = ((mouse_x - (width / 2)) * 0.005)
    ryp = ((mouse_y - (height / 2)) * 0.005)
    global rx, ry
    rx = (rx * 0.9) + (rxp * 0.1)
    ry = (ry * 0.9) + (ryp * 0.1)
    rotate_y(rx)
    rotate_x(ry)
    fill(0)
    no_stroke()
    sphere(radio)

    for p in lista:
        p.dibujar()
