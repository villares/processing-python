
tamanho = 50


def setup():
    size(500, 500)


def draw():
    background(200)
    if tamanho > 0:
        fill(0, 0, 200)
    else:
        fill(200, 0, 0)
    square(width / 2, height / 2, tamanho)


def mouse_wheel(event):
    movimento_roda = event.get_count()
    global tamanho
    tamanho += movimento_roda
