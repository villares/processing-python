""" Labirinto Tosco!
    Alexandre B A Villares - http://abav.lugaralgum.com
    Para rodar, instale o Processing Python Mode:
    http://abav.lugaralgum.com/como-instalar-o-processing-modo-python/
"""

tamanho = 30  # tamanho das células da grade
x, y = tamanho/2, 5  # posiciona toscamente o x e y do jogador


def setup():
    global fundo
    size(600, 600)
    gera_labirinto()
    fill(128, 128, 255)
    no_stroke()
    # meio, alvo, meta, objetivo - vitória não implementada ainda
    ellipse(width/2, height/2, 30, 30)
    save_frame("data/fundo.png")
    # acho que tem um jeito melhor de fazer isso, mas eu não lembro
    fundo = load_image("fundo.png")


def draw():
    background(fundo)  # limpa redraw usando fundo
    fill(255, 0, 0)
    no_stroke()
    ellipse(x, y, 10, 10)  # desenha jogador


def key_pressed():  # move jogador
    global x, y
    if key_code == UP and move_legal(0, -6):
        y = y - 5
    if key_code == DOWN and move_legal(0, 6):
        y = y + 5
    if key_code == LEFT and move_legal(-6, 0):
        x = x - 5
    if key_code == RIGHT and move_legal(6, 0):
        x = x + 5
    # Segue o wrap around
    if x < 0:
        x = width
    if x > width:
        x = 0
    if y < 0:
        y = height
    if y > height:
        y = 0


def move_legal(mx, my):
    ''' checa se a posição não invade uma parede preta'''
    if get(x+mx, y+my) == color(0):
        return False
    else:
        return True


def gera_labirinto():
    ''' prepara/desenha um labirinto tosco '''
    stroke_weight(10)
    background(255)
    colunas = width / tamanho
    filas = height / tamanho
    for fila in range(filas):
        for coluna in range(colunas):
            push_matrix()
            translate(coluna * tamanho, fila * tamanho)
            no_stroke()
            fill(random(255), 50)
            rect(0, 0, tamanho, tamanho)
            stroke(0)
            if int(
                    random(2)):  # esta é a tosca mágica hardcodada desse 'estilo' de labirinto tosco
                line(tamanho/2, 0, tamanho/2, tamanho)
            else:
                if int(random(2)):
                    line(0, tamanho/2, tamanho, tamanho/2)
                else:
                    line(0, tamanho/2, tamanho, tamanho/2)
                    line(tamanho/2, 0, tamanho/2, tamanho)
            pop_matrix()
