from Classes import Bola

lista_de_bolas = []


def setup():
    global bola1, bola2, limpa_tela, lista_de_bolas
    size(300, 200)
    for _ in range(10):
        lista_de_bolas.append(Bola(random(width), random(height),
                                   random(-2, 2), 128))
    limpa_tela = True


def draw():
    if limpa_tela:
        background(0)
    for bola in lista_de_bolas:
        bola.mostra()
        bola.anda()


def mouse_pressed():
    lista_de_bolas.append(Bola(mouse_x, mouse_y, 2, 255))


def key_pressed():
    global limpa_tela
    limpa_tela = not limpa_tela
