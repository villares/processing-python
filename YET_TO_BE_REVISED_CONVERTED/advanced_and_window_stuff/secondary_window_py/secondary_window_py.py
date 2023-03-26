
def setup():
    size(200, 300)
    second_window = OtherWindow("2nd")


def draw():
    background(0)
    ellipse(mouse_x, mouse_y, 10, 10)


class OtherWindow(Sketch):

    def __init__(self, title=""):
        switches = ('--sketch-path=' + sketch_path(), '')
        PApplet.runSketch(switches, self)
        self.surface.set_title(title)

    def settings(self):
        self.size(300, 200)

    def draw(self):  # este é o draw pra a segunda janela
        self.background(255)
        self.fill(0)
        self.rect(self.mouse_x, self.mouse_y, 10, 10)
