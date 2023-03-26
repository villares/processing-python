""" Exemplo de uso da Biblioteca PeasyCam criada por Jonathan Feinberg
    * documentação em http://mrfeinberg.com/peasycam/
    No menu do IDE Processing: Sketch > Import Library... > Add Library.. > [search for PeasyCam & install]
    depois Import Library... > PeasyCam
    Este exemplo mostra como realocar o clique-arraste da rodinha e do botão da direita
    - Clique e arraste o botão central (rodinha) para orbitar
    - Clique e arraste o botão da direita = Pan/Translate
    - Rodinha/mouse wheel = Zoom
    - Tecla R - reset da câmera
    - Tecla S - salva um estado
    - Tecla L - carrega o estado salvo
"""

add_library('peasycam')  # import peasy.*
saved_cam_state = None


def setup():
    global cam
    size(200, 200, P3D)
    cam = PeasyCam(this, 100)
    cam.set_minimum_distance(50)
    cam.set_maximum_distance(500)
    # Reassign some drag handlers
    orbit_dh = cam.get_rotate_drag_handler()  # pega o RotateDragHandler
    # define como ação do botão centra/rodinha
    cam.set_center_drag_handler(orbit_dh)
    pan_dh = cam.get_pan_drag_handler()       # pega PanDragHandler
    # define como ação do botão da direita
    cam.set_right_drag_handler(pan_dh)
    # nenhum Handler para o botão da esquerda
    cam.set_left_drag_handler(None)


def draw():
    background(0)
    fill(255, 0, 0)
    box(30)
    push_matrix()
    translate(0, 0, 20)
    fill(0, 0, 255)
    box(5)
    pop_matrix()


def key_pressed():
    global saved_cam_state
    if key == 'r' or key == 'R':
        cam.reset()    # reseta o estado original da câmera

    if key == 's' or key == 'S':
        saved_cam_state = cam.get_state()    # salva estado da câmera

    if key == 'l' or key == 'L':
        if saved_cam_state:
            # carrega o estado previamente salvo
            cam.set_state(saved_cam_state)
