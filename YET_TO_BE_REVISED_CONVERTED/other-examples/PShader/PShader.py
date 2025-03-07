nebula = None


def setup():
    size(512, 384, P2D)

    global nebula
    nebula = load_shader("nebula.glsl")
    nebula.set("resolution", float(width), float(height))
    shader(nebula)


def draw():
    nebula.set("time", millis() / 1000.0)

    # The rect is needed to make the fragment shader go through every pixel of
    # the screen, but is not used for anything else since the rendering is entirely
    # generated by the shader.
    no_stroke()
    fill(0)
    rect(0, 0, width, height)
