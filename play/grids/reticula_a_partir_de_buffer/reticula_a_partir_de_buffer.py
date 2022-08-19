"""
 Retícula de bolinhas brancas a partir de imagem
 Aperte 'g' para gravar um PDF na pasta do sketch
"""
add_library('pdf')
tam_celula = 4  # tamanho das células da grade
gravar_pdf = False


def setup():
    global colunas, filas, img
    size(600, 400)
    no_stroke()
    smooth()
    rect_mode(CENTER)
    # print(PFont.list())
    f = create_font("Tomorrow Bold", 80)
    colunas = int(width / tam_celula)
    filas = int(height / tam_celula)
    # Começa a captura
    img = create_graphics(600, 400)
    img.begin_draw()
    img.background(100)
    img.text_font(f)
    img.text_align(CENTER, CENTER)
    img.text_size(100)
    img.text("Hello", width / 3, height / 3)
    img.stroke(0)
    img.stroke_weight(10)
    img.circle(450, 250, 100)
    img.filter(BLUR, 2)
    img.end_draw()


def draw():
    global gravar_pdf

    if gravar_pdf:
        begin_record(PDF, "Imagem.pdf")
    background(0)
    no_stroke()
    img.load_pixels()
    # Loopando as colunas da grade
    for i in range(colunas):
        # Loop das filas
        for j in range(filas):
            x = i * tam_celula
            y = j * tam_celula
            loc = x + y * img.width
            cor = img.pixels[loc]
            tam = map(brightness(cor), 0, 255, 0, tam_celula - 1)
            color_mode(HSB)
            fill(255)
            ellipse(x + tam_celula / 2, y + tam_celula / 2, tam, tam)
         # fim fo loop das filas
     # fim do loop das colunas
    if (gravar_pdf):
        end_record()
        print('gravado arquivo imagem.pdf')
        gravar_pdf = False
        exit()


def key_pressed(self):
    global gravar_pdf
    if key == 'g':
        gravar_pdf = True
