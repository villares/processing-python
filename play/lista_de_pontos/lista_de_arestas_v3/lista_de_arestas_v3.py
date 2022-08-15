""" Alexandre B A Villares - http://abav.lugaralgum.com
    Brincando com uma lista de pontos, e agora arestas.
    Para rodar, instale o Processing Modo Python.
    Desenvolvido principalmente durante o Carnahacking 2017
    no Garoa Hacker Clube - http://garoa.net.br
    e publicado em https://github.com/villares/py.processing-play
"""
import random as rnd  # para não conflitar com o random do Processing
pontos = set()  # conjunto de Pontos
arestas = []    # lista de Arestas

TAM_PONTO = 50  # TAM_PONTO dos Pontos \
TAM_BARRA = 100
VEL_MAX = 2  # velocidade máxima nas ortogonais vx e vy
PONTOS_INI = 5  # númer inicial de pontos


def setup():
    size(600, 600)
    stroke_weight(3)
    for _ in range(PONTOS_INI):
        x, y = random(width), random(height)
        pontos += Ponto(x, y)  # acrescenta um Ponto


def draw():
    background(128)        # limpa a tela
    # para cada ponto
    for ponto in pontos:
        ponto.desenha()  # desenha
        ponto.move()    # atualiza posição
    # para cada aresta
    for aresta in arestas:  # checa se há Arestas com Pontos já removidos
        if (aresta.p1 not in pontos) or (aresta.p2 not in pontos):
            arestas.remove(aresta)   # nesse caso remove a Aresta também
        else:                # senão
            aresta.desenha()  # desenha a linha
            aresta.puxa_empurra()  # altera a velocidade dos pontos

# Sob clique do mouse seleciona/deseleciona Pontos ou Arestas


def mouse_clicked():
    for ponto in pontos:   # para cada Ponto checa distância do mouse
        if dist(mouse_x, mouse_y, ponto.x, ponto.y) < TAM_PONTO / 2:
            ponto.sel = not ponto.sel  # inverte status de seleção
    mouse = Py5Vector(mouse_x, mouse_y)
    for aresta in arestas:    # para cada Aresta checa o 'mouse over'
        if point_inside_line(mouse, aresta.p1, aresta.p2, 6):
            aresta.sel = not aresta.sel  # inverte status de seleção


def key_pressed():   # Quando uma tecla é pressionada
    # Barra de espaço acrescenta Pontos na posição atual do mouse
    if key == ' ':
        pontos += Ponto(mouse_x, mouse_y)  # acrescenta Ponto no set
    # 'd' remove os Pontos previamente selecionandos com clique, marcados em preto.
    if key == 'd':
        for ponto in pontos:
            # se a lista tiver pelo menos 2 pontos
            if ponto.sel and len(pontos) > 1:
                pontos.remove(ponto)           # remove pontos selecionados
        for aresta in arestas:
            if aresta.sel:  # se a lista tiver pelo menos 2 pontos
                arestas.remove(aresta)           # remove pontos selecionados


def mouse_dragged():        # quando o mouse é arrastado
    for ponto in pontos:   # para cada Ponto checa distância do mouse
        if dist(mouse_x, mouse_y, ponto.x, ponto.y) < TAM_PONTO / 2:
            # move o Ponto para posição do mouse
            ponto.x, ponto.y = mouse_x, mouse_y
            ponto.vx = 0
            ponto.vy = 0


class Ponto():

    " Pontos num grafo, VEL_MAX inicial sorteada, criam Arestas com outros Pontos "

    def __init__(self, x, y, cor=color(0)):
        self.x = x
        self.y = y
        self.z = 0  # para compatibilidade com PVector...
        self.vx = random(-VEL_MAX, VEL_MAX)
        self.vy = random(-VEL_MAX, VEL_MAX)
        self.sel = False   # se está selecionado, começa sem seleção
        self.cor = color(random(128, 255),  # R
                         random(128, 255),  # G
                         random(128, 255),  # B
                         128)              # Alpha ~50%
        self.cria_arestas()

    def __getitem__(self, i):
        return (self.x, self.y, self.z)[i]

    def desenha(self):
        if self.sel:
            stroke(0)
        else:
            no_stroke()
        fill(self.cor)
        ellipse(self.x, self.y, TAM_PONTO, TAM_PONTO)
        if dist(mouse_x, mouse_y, self.x, self.y) < TAM_PONTO:
            stroke(255)
            no_fill()
            ellipse(self.x, self.y, TAM_PONTO + 5, TAM_PONTO + 5)
            # fill(0)
            # text(str(len(pontos)) + " " + str(len(arestas)), self.x, self.y)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if not (0 < self.x < width):
            self.vx = -self.vx
        if not (0 < self.y < height):
            self.vy = -self.vy
        self.vx = self.limitar(self.vx, VEL_MAX)
        self.vy = self.limitar(self.vy, VEL_MAX)

    def cria_arestas(self, modo='random'):
        if modo == 'random':
            lista_pontos = list(pontos)
            if lista_pontos:
                nova_aresta = Aresta(rnd.choice(lista_pontos), self)
                arestas.append(nova_aresta)
        elif modo == 'all':
            for ponto in pontos:
                nova_aresta = Aresta(ponto, self)
                arestas.append(nova_aresta)

    def limitar(self, v, v_max):
        if v > v_max:
            return v_max
        elif v < -v_max:
            return -v_max
        else:
            return v


class Aresta():

    """ Arestas contém só dois Pontos e podem ou não estar selecionadas """

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.sel = False

    def desenha(self):
        if self.sel:
            stroke(0)
        else:
            stroke(255)
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        no_stroke()
        fill(255)
        ellipse(self.p1.x, self.p1.y, TAM_PONTO / 6, TAM_PONTO / 6)
        ellipse(self.p2.x, self.p2.y, TAM_PONTO / 6, TAM_PONTO / 6)

    def puxa_empurra(self):
        d = dist(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        delta = TAM_BARRA - d
        dir = self.p1 - self.p2
        dir *= delta / 1000
        self.p1.vx = self.p1.vx + dir.x
        self.p1.vy = self.p1.vy + dir.y
        self.p2.vx = self.p2.vx - dir.x
        self.p2.vy = self.p2.vy - dir.y


def point_inside_line(
        the_point,
        the_line_end_point1,
        the_line_end_point2,
        the_tolerance):
    # from Andreas Schlegel / http://www.sojamo.de """
    dir = Py5Vector(the_line_end_point2.x, the_line_end_point2.y, 0)
    dir -= the_line_end_point1
    diff = Py5Vector(the_point.x, the_point.y, 0)
    diff -= the_line_end_point1
    try:
        inside_distance = diff.dot(dir) / dir.dot(dir)
    except ZeroDivisionError:
        inside_distance = 1000
    if (0 < inside_distance < 1):
        closest = Py5Vector(the_line_end_point1.x, the_line_end_point1.y, 0)
        dir *= inside_distance
        closest += dir
        d = Py5Vector(the_point.x, the_point.y)
        d -= closest
        distsqr = d.dot(d)
        return (distsqr < pow(the_tolerance, 2))
    return False
