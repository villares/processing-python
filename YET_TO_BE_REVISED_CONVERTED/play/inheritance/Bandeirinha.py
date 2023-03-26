# -*- coding: latin-1 -*-

class Bandeirinha(object):
    """ Classe Bandeirinha, cor sorteada, velocidade sorteada """

    def __init__(self, px, py, ptamanho=None):
        self.x = float(px)
        self.y = float(py)
        if ptamanho:
            self.tamanho = ptamanho
        else:
            self.tamanho = random(50, 200)
        self.vx = random(-1, 1)
        self.vy = random(-1, 1)
        self.cor = color(random(255),  # R
                         random(255),  # G
                         random(255),  # B
                         200)  # alpha

    def desenha(self):
        """ Desenha polígono em torno das coordenadas do objeto """
        metade = self.tamanho / 2
        with push_matrix():   # preseservando o sistema de coordenadas anterior
            translate(self.x, self.y)  # translada o sistema de coordenadas
            no_stroke()  # sem contorno
            # se o mouse estiver longe, normal, senão, branca
            if dist(mouse_x, mouse_y, self.x, self.y) > metade:
                fill(self.cor)
            else:
                fill(255, 100)
            begin_shape()  # inicia polígono
            vertex(-metade, -metade)
            vertex(-metade, metade)
            vertex(0, 0)
            vertex(metade, metade)
            vertex(metade, -metade)
            end_shape(CLOSE)  # encerra polígono, fechando no primeiro vértice

    def anda(self):
        """ atualiza a posição do objeto e devolve do lado oposto se sair """
        self.x += self.vx
        self.y += self.vy
        metade = self.tamanho / 2
        if self.x > width + metade:
            self.x = -metade
        if self.y > height + metade:
            self.y = -metade
        if self.x < -metade:
            self.x = width + metade
        if self.y < -metade:
            self.y = height + metade
