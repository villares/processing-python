""" Variante do exemplo de herança proposto pelo João Adriano Freitas
"""

from FabricaBandeirinhas import Fabrica

bandeirinhas = []  # lista de objetos


def setup():
    """ Define área de desenho e popula lista de bandeirinhas """
    size(400, 400)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2, height / 2
    for _ in range(50):
        nova_bandeirinha = Fabrica(meia_largura, meia_altura)
        bandeirinhas.append(nova_bandeirinha)


def draw():
    """ Limpa a tela, desenha e atualiza bandeirinhas """
    background(0)  # atualização do desenho, fundo preto
    for bandeira in bandeirinhas:
        bandeira.desenha()
        bandeira.anda()


def mouse_pressed():
    """ Acrescenta pequena bandeirinha branca """
    nova_bandeirinha = Fabrica(mouse_x, mouse_y, 25)
    nova_bandeirinha.cor = color(255)  # forçando que seja branca!
    bandeirinhas.append(nova_bandeirinha)


def key_pressed():
    """ tecla 'espaço' remove a última bandeirinha da lista """
    if key == ' ' and len(bandeirinhas) > 1:
        removida = bandeirinhas.pop()
