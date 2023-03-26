"""
Exemplo de Perlin Noise em três dimensões
"""

perlin_scale = 0.1
z = 0


def setup():
    size(500, 500)  # define o tamanho da tela em pixels. Largura X Altura
    no_stroke()
    color_mode(HSB)


def draw():
    background(0)
    cols = 50
    tam = width / cols
    for x in range(cols):
        for y in range(cols):
            n = noise(
                (mouse_x + x) * perlin_scale,
                (mouse_y + y) * perlin_scale,
                z * perlin_scale)
            fill(240 * n, 255, 255)
            ellipse(tam / 2 + x * tam, tam / 2 + y * tam,
                    tam - tam * n, tam - tam * n)


def key_pressed():
    global z
    if key_code == UP:
        z += 1
    if key_code == DOWN:
        z -= 1
