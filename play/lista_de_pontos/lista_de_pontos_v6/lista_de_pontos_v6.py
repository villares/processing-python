""" Alexandre B A Villares - abav.lugaralgum.com
    Brincando com uma lista de pontos --> github.com/villares
"""
lista = []  # lista de pontos
tamanho = 30


def setup():
    size(600, 600)
    stroke_weight(2)
    stroke(255)     # traço/linha e branco
    no_fill()       # sem preenchinmento
    for _ in range(5):
        x, y, cor = random(width), random(
            height), cor_rnd()  # sorteia propriedades
        lista.append(Ponto(x, y, cor))  # acrescenta um ponto na lista


def draw():
    background(128)             # limpa a tela
    for ponto in lista:                  # para cada ponto
        ponto.desenha()
        ponto.move()
        # pegua um segundo ponto (inclui o mesmo)
        for outro_ponto in lista:
            if ponto != outro_ponto:     # checa se não é o mesmo
                Ponto.desenha_linha(ponto, outro_ponto)  # desenha setas


def cor_rnd(alpha_value=128):
    return color(
        random(
            128, 255), random(
            128, 255), random(
                128, 255), alpha_value)


def mouse_clicked():  # ao soltar do mousw
    # acrescenta poneto na pos. clicada
    lista.append(Ponto(mouse_x, mouse_y, cor_rnd()))


def key_pressed():               # tecla pressionada
    if len(lista) > 1:          # se a lista tiver pelo menos 2 pontos
        removido = lista.pop(0)  # remove primeiro ponto da lista


def mouse_dragged():
    for ponto in lista:                  # para cada ponto
        if dist(mouse_x, mouse_y, ponto.x, ponto.y) < tamanho*3/2:
            ponto.x, ponto.y = mouse_x, mouse_y


class Ponto:
    " pontos num grafo "

    def __init__(self, x, y, cor=color(0)):
        self.x = x
        self.y = y
        self.cor = cor
        self.vx = random(-0.5, 0.5)
        self.vy = random(-0.5, 0.5)

    def desenha(self):
        if dist(mouse_x, mouse_y, self.x, self.y) < tamanho*3/2:
            stroke(0)
            no_fill()
            ellipse(self.x, self.y, tamanho*3, tamanho*3)
        stroke(255)
        fill(self.cor)
        ellipse(self.x, self.y, tamanho, tamanho)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if not (0 < self.x < width):
            self.vx = -self.vx
        if not (0 < self.y < height):
            self.vy = -self.vy

    @classmethod
    def desenha_linha(cls, p1, p2):
        x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y
        d = dist(x1, y1, x2, y2)
        with push_matrix():
            translate(x2, y2)
            angle = atan2(x1 - x2, y2 - y1)
            rotate(angle)
            offset = -tamanho*.6
            head = 6
            line(0, offset, 0, -d - offset)
            line(0, offset, -head/3, -head + offset)
            line(0, offset, head/3, -head + offset)
