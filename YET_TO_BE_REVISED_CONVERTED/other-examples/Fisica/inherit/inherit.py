from fisica import Fisica, FWorld, FBox
add_library('fisica')


class Texto(FBox):
    def __init__(self, _texto):
        FBox.__init__(self, text_width(_texto), text_ascent() + text_descent())
        self.texto = _texto
        self.text_offset = text_ascent() - self.get_height()/2

    def draw(self, applet):
        FBox.draw(self, applet)
        self.pre_draw(applet)
        fill(0)
        stroke(0)
        text_align(CENTER)
        text(self.texto, 0, self.text_offset)
        self.post_draw(applet)


msg = ''
world = None


def setup():
    global world

    size(400, 400)
    smooth()
    Fisica.init(this)
    font = load_font("FreeMonoBold-24.vlw")
    text_font(font, 24)
    world = FWorld()
    world.set_edges(this, color(120))
    world.remove(world.top)
    world.set_gravity(0, 500)
    t = Texto("Type and ENTER")
    t.set_position(width/2, height/2)
    t.set_rotation(random(-1, 1))
    t.set_fill(255)
    t.set_no_stroke()
    t.set_restitution(0.75)
    world.add(t)


def draw():
    background(120)
    world.step()
    world.draw()


def key_pressed():
    global msg
    if key == ENTER:
        if msg:
            t = Texto(msg)
            t.set_position(width/2, height/2)
            t.set_rotation(random(-1, 1))
            t.set_fill(255)
            t.set_no_stroke()
            t.set_restitution(0.65)
            world.add(t)
            msg = ''
    elif key == CODED and key_code == CONTROL:
        save_frame("screenshot.png")
    else:
        msg += str(key)
