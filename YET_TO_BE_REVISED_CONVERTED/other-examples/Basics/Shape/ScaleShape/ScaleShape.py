"""
 Scale Shape.
 Illustration by George Brower.
 (Rewritten in Python by Jonathan Feinberg.)

 Move the mouse left and right to zoom the SVG file.
 This shows how, unlike an imported image, the lines
 remain smooth at any size.
 """

# The file "bot1.svg" must be in the data folder
# of the current sketch to load successfully
bot = load_shape("bot1.svg")


def setup():
    size(640, 360)
    smooth()


def draw():
    background(102)
    translate(width / 2, height / 2)
    zoom = map(mouse_x, 0, width, 0.1, 4.5)
    scale(zoom)
    shape(bot, -140, -140)
