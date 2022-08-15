""" Alexandre B A Villares - abav.lugaralgum.com
    Brincando com uma lista de pontos --> github.com/villares
    Para rodar, instale o Processing Modo Python.
"""
pontos = set()  # pontos
arestas = []

tamanho = 30  # tamanho dos 'pontos'
velocidade = 0.2
pontos_iniciais = 5


def setup():
    size(600, 600)
    stroke_weight(2)
    stroke(255)     # traço/linha e branco
    no_fill()       # sem preenchinmento
    for _ in range(pontos_iniciais):
        x, y = random(width), random(height)
        cor = cor_rnd()  # sorteia cor
        pontos += Ponto(x, y, cor)  # acrescenta um ponto na lista
    uns_pontos = list(pontos)
    for i, ponto in enumerate(uns_pontos):
        for outro_ponto in uns_pontos[i:]:
            if ponto != outro_ponto:  # checa se não é o mesmo
                nova_aresta = Aresta(ponto, outro_ponto)
                arestas.append(nova_aresta)


def draw():
    background(128)             # limpa a tela
    for aresta in arestas:
        if (aresta.p1 not in pontos) or (aresta.p2 not in pontos):
            arestas.remove(aresta)
            print(aresta.p1, aresta.p2)
        else:
            aresta.desenha_linha()
    for ponto in pontos:  # para cada ponto
        ponto.desenha()
        ponto.move()


def cor_rnd(alpha_value=128):
    return color(
        random(
            128, 255), random(
            128, 255), random(
                128, 255), alpha_value)


def mouse_clicked():  # ao soltar do mouse
    novo_ponto = Ponto(mouse_x, mouse_y, cor_rnd())
    for ponto in pontos:
        nova_aresta = Aresta(ponto, novo_ponto)
        arestas.append(nova_aresta)
    pontos += novo_ponto  # acrescenta poneto na pos. clicada


def key_pressed():               # tecla pressionada
    if len(pontos) > 1:          # se a lista tiver pelo menos 2 pontos
        removido = pontos.pop()  # remove primeiro ponto da lista


def mouse_dragged():
    for ponto in pontos:                  # para cada ponto
        if dist(mouse_x, mouse_y, ponto.x, ponto.y) < tamanho * 3 / 2:
            ponto.x, ponto.y = mouse_x, mouse_y


class Ponto():
    " pontos num grafo "

    def __init__(self, x, y, cor=color(0)):
        self.x = x
        self.y = y
        self.cor = cor
        self.vx = random(-velocidade, velocidade)
        self.vy = random(-velocidade, velocidade)

    def desenha(self):
        fill(self.cor)
        ellipse(self.x, self.y, tamanho, tamanho)
        if dist(mouse_x, mouse_y, self.x, self.y) < tamanho * 3 / 2:
            stroke(0)
            no_fill()
            ellipse(self.x, self.y, tamanho * 3, tamanho * 3)
            fill(0)
            text(str(len(pontos))+" "+str(len(arestas)), self.x, self.y)
        stroke(255)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if not (0 < self.x < width):
            self.vx = -self.vx
        if not (0 < self.y < height):
            self.vy = -self.vy


class Aresta():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def desenha_linha(self):
        x1, y1, x2, y2 = self.p1.x, self.p1.y, self.p2.x, self.p2.y
        d = dist(x1, y1, x2, y2)
        with push_matrix():
            translate(x2, y2)
            angle = atan2(x1 - x2, y2 - y1)
            rotate(angle)
            offset = -tamanho * .6
            head = 6
            line(0, offset, 0, -d - offset)
            line(0, offset, -head / 3, -head + offset)
            line(0, offset, head / 3, -head + offset)
