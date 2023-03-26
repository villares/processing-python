"""
Inicio de uma ideia sobre mapas para jogos
"""

import random

TAMANHO = 50  # tamanho grade
mapa = []


def setup():
    global colunas, filas, mapa
    size(600, 600)
    colunas = width / TAMANHO
    filas = height / TAMANHO
    for fila in range(filas):
        for coluna in range(colunas):
            tipo = random.choice(Quadrado.TIPOS)
            quadrado = Quadrado(fila, coluna, tipo, 0)
            mapa.append(quadrado)


def draw():
    for quadrado in mapa:
        quadrado.desenha()


class Quadrado():
    ''' Região quadrada do mapa'''

    AMARELO = color(255, 230, 0)
    AZUL_ESCURO = color(7, 0, 255)
    MARROM_ESCURO = color(85, 25, 27)
    VERDE_CLARO = color(10, 237, 7)
    MARROM_CLARO = color(193, 109, 111)
    VERDE_ESCURO = color(48, 72, 36)
    TIPOS = ["mar", "montanha", "praia", "plano", "vila", "floresta"]
    CORES = {"mar": AZUL_ESCURO,
             "montanha": MARROM_ESCURO,
             "praia": AMARELO,
             "plano": VERDE_CLARO,
             "vila": MARROM_CLARO,
             "floresta": VERDE_ESCURO}

    def __init__(self, fila, coluna, tipo, altura):
        self.fila = fila
        self.coluna = coluna
        self.tipo = tipo
        self.altura = altura
        self.cor = Quadrado.CORES[tipo]

    def desenha(self):
        pos_x, pos_y = self.coluna * TAMANHO, self.fila * TAMANHO
        with push_matrix():
            translate(pos_x, pos_y)
            no_stroke()
            fill(self.cor)
            rect(0, 0, TAMANHO, TAMANHO)
            fill(0)       # preto
            text_size(10)  # para escrever o tipo se o mouse estiver perto
            if (dist(pos_x, pos_y, mouse_x, mouse_y) < TAMANHO * 2):
                text(self.tipo, 0, 20)
