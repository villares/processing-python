"""
  Zoando o 'Mirror2' do Daniel Shiffman
 Messing with Processing demo 'Mirror2' by coding hero Daniel Shiffman.
 Grid of circles, size varies with the brightness of the captured pixel at the center of each circle
"""
add_library('video')
gravar = False


def setup():
    global tamanho, colunas, filas, video
    size(640, 480)
    frame_rate(10)
    no_stroke()
    smooth()
    rect_mode(CENTER)
    tamanho = 10  # tamanho das células da grade
    colunas = width / tamanho
    filas = height / tamanho
    video = Capture(this, width, height)
    # Começa a captura
    video.start()
    background(0)


def draw():
    background(0)
    if video.available():
        video.read()
        video.load_pixels()
        # Loopando nas colundas da grade
        for i in range(colunas):
            # Loopando nas filas da grade
            for j in range(filas):
                x = i * tamanho
                y = j * tamanho
                loc = x + y * video.width  # acha posição do pixel na captura
                cor = video.pixels[loc]  # pega cor do pixel
                fill(cor)                # aplica cor do pixel
                lumin = brightness(cor)  # calcula luminosidade do pixel
                ellipse(x + tamanho / 2, y + tamanho / 2,
                        tamanho * lumin / 255, tamanho * lumin / 255)
        if gravar:
            save_frame("frame####.png")


def keyPressed():
    gravar = not gravar  # inverte o flag de gravação
    println("gravando: ", gravar)
