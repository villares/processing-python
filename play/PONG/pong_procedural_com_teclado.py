""" Pong Procedural
    Esta estrutura deve facilitar uma futura refacção orientada a objetos
    Teclas 'a' e 'z' controlam um jogador, as setas para cima e para baixo o outro.
*** Tecla 'espaço' para iniciar o ponto.
"""

DIA_BOLA = 10
VEL_INICIAL = 4
MEIO_JOGADOR = 50
ESP_JOGADOR = 10
VEL_JOGADOR = 5


def setup():
    global vel_x, vel_y
    size(600, 400)
    no_stroke()
    prepara_jogo()    # prepara o jogo, esta função normalmente recomeça o jogo
    vel_x, vel_y = 0, 0  # mas aqui eu logo em seguida paro a bola zerando as velocidades


def draw():
    background(0)
    if not game_over:
        jogadores_move()
        jogadores_desenha()
        bola_move()
        bola_desenha()
    else:
        escreve_game_over()


def key_pressed():
    global sobe_1, desce_1, sobe_2, desce_2
    if key == 'a':
        sobe_1 = True
    elif key == 'z':
        desce_1 = True
    if key_code == UP:
        sobe_2 = True
    elif key_code == DOWN:
        desce_2 = True
    if key == ' ':
        prepara_jogo()


def key_released():
    global sobe_1, desce_1, sobe_2, desce_2
    if key == 'a':
        sobe_1 = False
    elif key == 'z':
        desce_1 = False
    if key_code == UP:
        sobe_2 = False
    elif key_code == DOWN:
        desce_2 = False


def bola_move():
    global bola_x, bola_y, vel_x, vel_y, game_over
    # altera posição x e y da bola usando as velocidades x e y
    bola_x, bola_y = bola_x + vel_x, bola_y + vel_y
    if not(0 < bola_x < width):                      # se a bola sair da tela à direita ou à esquerda
        if jogador_rebate(1) or jogador_rebate(
                2):  # se for rebatida pelo jogador 1 ou 2
            vel_x = -vel_x               # inverta a velocidade horizontal
        else:                          # senão:
            game_over = True          # game over!
    if not(0 < bola_y < height):   # se sair da tela por cima ou por baixo
        vel_y = -vel_y            # inverta a velocidade vertical


def bola_desenha():
    fill(255, 0, 0)  # vermelho
    ellipse(bola_x, bola_y, DIA_BOLA, DIA_BOLA)


def jogadores_move():
    global j1_y, j2_y
    if sobe_1:
        j1_y = j1_y - VEL_JOGADOR
    if desce_1:
        j1_y = j1_y + VEL_JOGADOR
    if sobe_2:
        j2_y = j2_y - VEL_JOGADOR
    if desce_2:
        j2_y = j2_y + VEL_JOGADOR


def jogadores_desenha():
    fill(0, 0, 255)  # azul
    rect(0, j1_y - MEIO_JOGADOR,
         ESP_JOGADOR, MEIO_JOGADOR*2)
    rect(width - ESP_JOGADOR, j2_y - MEIO_JOGADOR,
         ESP_JOGADOR, MEIO_JOGADOR*2)


def prepara_jogo():  # começa ou recomeça um jogo
    global game_over
    global bola_x, bola_y, vel_x, vel_y
    global sobe_1, desce_1, sobe_2, desce_2
    global j1_y, j2_y  # , j1_points, j2_points
    bola_x, bola_y = width/2, height/2
    vel_x = (-VEL_INICIAL, VEL_INICIAL)[int(random(2))]
    vel_y = (-VEL_INICIAL, VEL_INICIAL)[int(random(2))]
    sobe_1 = desce_1 = sobe_2 = desce_2 = False
    j1_y = j2_y = height/2
    #j1_pontos = j2_pontos = 0
    game_over = False


def escreve_game_over():
    text_size(60)
    text_align(CENTER)
    text("GAME OVER", width/2, height/2)


def jogador_rebate(jogador):  # checa se jogador 1 ou 2 rebateu com sucesso a bola
    if jogador == 1:
        return (bola_x <= 0 and
                j1_y - MEIO_JOGADOR < bola_y < j1_y + MEIO_JOGADOR)
    else:
        return (bola_x >= width and
                j2_y - MEIO_JOGADOR < bola_y < j2_y + MEIO_JOGADOR)
