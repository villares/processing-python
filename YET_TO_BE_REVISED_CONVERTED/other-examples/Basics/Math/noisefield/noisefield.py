"""
  noisefield.py - demonstrate Perlin noise
  Jonathan Feinberg
"""
src_size = 50
dest_size = 400
g = None


def setup():
    global g
    size(dest_size, dest_size)
    g = create_graphics(src_size, src_size)


def draw():
    t = .0005 * millis()
    g.begin_draw()
    for y in range(src_size):
        for x in range(src_size):
            blue = noise(t + .1*x, t + .05*y, .1 * t)
            g.set(x, y, color(0, 0, 255 * blue))
    g.end_draw()
    image(g, 0, 0, dest_size, dest_size)
