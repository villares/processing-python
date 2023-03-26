'''
Alexandre B A Villares - http://abav.lugaralgum.com
Desenho com simetria radial / Radial drawing

Use Processing Python Mode:
http://abav.lugaralgum.com/como-instalar-o-processing-modo-python/

Apoie-nos! / Support us! http://patreon.com/arteprog
'''

divisoes = 12  # divisions/rotations


def setup():
    size(500, 500)
    background(255)
    stroke_weight(5)


def draw():
    # desfeito ao final de draw / undone at the end of draw
    translate(width / 2, height / 2)
    for _ in range(divisoes):
        rotate(TWO_PI / divisoes)
        if mouse_pressed:
            with push_matrix():
                translate(-width / 2, -height / 2)
                line(pmouse_x, pmouse_y, mouse_x, mouse_y)


def key_pressed():
    global divisoes
    if key in ['+', '=']:
        divisoes += 1
    if key == '-' and divisoes > 1:
        divisoes -= 1
    if key == ' ':
        background(255)
    if key == '0':
        stroke(0)
    if key == 'r':
        stroke(255, 0, 0)
    if key == 'g':
        stroke(0, 255, 0)
    if key == 'b':
        stroke(0, 0, 255)
