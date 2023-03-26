lista_de_bolas = []


def setup():
    global bola1, bola2, lista_de_bolas
    size(300, 200)
    for i in range(2):
        lista_de_bolas.append(
            Bola(
                random(width),
                random(height),
                random(
                    1,
                    3)))


def draw():
    background(0)
    for bola in lista_de_bolas:
        bola.mostra()
        bola.anda()


def mouse_pressed():
    global lista_de_bolas
    lista_de_bolas.append(Bola(mouse_x, mouse_y, random(1, 3)))


class Bola():
    def __init__(self, px, py, v):
        self.x = px
        self.y = py
        self.cor = color(random(255), random(255), random(255))
        self.velocidade_x = v
        self.velocidade_y = v

    def mostra(self):
        fill(self.cor)
        ellipse(self.x, self.y, 10, 10)

    def anda(self):
        self.x += self.velocidade_x  # self.x = self.x + self.velocidade_x
        self.y += self.velocidade_y
        if not(0 < self.x < width):
            self.velocidade_x = -self.velocidade_x
        if not(0 < self.y < height):
            self.velocidade_y = -self.velocidade_y
