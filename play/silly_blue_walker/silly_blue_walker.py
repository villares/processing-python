x, y, vx, vy = 3, 3, 1, 1
translucido = False


def setup():
    global x, y
    full_screen()
    background(255)
    no_stroke()
    x, y = width / 2, height / 2


def draw():
    global x, y, vx, vy
    if translucido:
        alfa = 100
    else:
        alfa = 255
    cor = color(0, 0, random(255), alfa)
    fill(cor)
    tamanho = random(10, 50)
    ellipse(x, y, tamanho, tamanho)
    x += vx
    y += vy
    if not (0 < x < width):
        vx = -vx
    if not (0 < y < height):
        vy = -vy
    vx += random(-1, 1)
    vy += random(-1, 1)


def key_pressed():
    save_frame()
    print "Imagem salva na pasta do sketch!"


def mouse_clicked():
    global translucido
    background(255)
    translucido = not translucido
