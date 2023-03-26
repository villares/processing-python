"""
 Retícula de bolinhas brancas a partir da câmera
 Aperte 'g' para gravar um PDF na pasta do sketch
"""
add_library('video')
add_library('pdf')
tam_celula = 16  # tamanho das células da grade
gravar_pdf = False


def setup():
    global colunas, filas, video
    size(640, 480)
    no_stroke()
    smooth()
    rect_mode(CENTER)
    colunas = int(width / tam_celula)
    filas = int(height / tam_celula)
    video = Capture(this, width, height)
    # Começa a captura
    video.start()
    background(0)


def draw():
    global gravar_pdf
    if video.available():
        # se foi apertado 'g'
        if gravar_pdf:
            fill(0)
            rect(0, 0, width, height)
            begin_record(PDF, "Imagem.pdf")
        background(0)
        video.read()
        video.load_pixels()
        # Loopando as colunas da grade
        for i in range(colunas):
            # Loop das filas
            for j in range(filas):
                x = i * tam_celula
                y = j * tam_celula
                loc = x + y * video.width
                cor = video.pixels[loc]
                tam = map(brightness(cor), 0, 255, 0, tam_celula - 1)
                fill(255)
                ellipse(x + tam_celula / 2, y + tam_celula / 2, tam, tam)
             # dim fo loop das filas
         # fim do loop das colunas
        if (gravar_pdf):
            end_record()
            print('gravado arquivo imagem.pdf')
            gravar_pdf = False


def key_pressed(self):
    global gravar_pdf
    if key == 'g':
        gravar_pdf = True
