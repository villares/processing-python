""" Exemplo de uso da Biblioteca PeasyCam
    * documentação em http://mrfeinberg.com/peasycam/
    No menu do IDE Processing: Sketch > Import Library... > Add Library.. > [search for PeasyCam & install]
    depois Import Library... > PeasyCam
    - Clique e arraste o mouse (mouseDragged) para orbitar
    - Scroll Wheel = Zoom
    - Command = Translate
"""
add_library('peasycam')


def setup():
    global camera
    size(200, 200, P3D)       # note o setup do canvas 3D
    camera = PeasyCam(this, 100)
    camera.set_minimum_distance(50)
    camera.set_maximum_distance(500)


def draw():
    rotate_x(-.5)
    rotate_y(-.5)
    background(0)
    fill(255, 0, 0)
    box(30)
    with push_matrix():
        translate(0, 0, 20)
        fill(0, 0, 255)
        box(5)
    camera.begin_hud()  # para desenhar relativo ao ponto de vista da câmera
    fill(255)
    rect(30, 30, 30, 30)
    camera.end_hud()  # se usou .beginHUD() no esqueça de .endHUD() sempre!
