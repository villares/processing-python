"""
 Kinetic Type
 by Zach Lieberman.
 Adapted to Python by Jonathan Feinberg
 Using push() and pop() to define the curves of the line_s of type.
"""

words = [
    "sometimes it's like", "the line_s of text", "are so happy",
    "that they want to dance", "or leave the page or jump",
    "can you blame them?", "living on the page like that",
    "waiting to be read..."
]


def setup():
    size(640, 360, P3D)
    hint(DISABLE_DEPTH_TEST)
    text_font(load_font("Univers-66.vlw"), 1.0)
    fill(255)


def draw():
    background(0)
    push_matrix()
    translate(-200, -50, -450)
    rotate_y(0.3)

    # Now animate every line_ object & draw it...
    for i in range(len(words)):
        f1 = sin((i + 1.0) * (millis() / 10000.0) * TWO_PI)
        f2 = sin((8.0 - i) * (millis() / 10000.0) * TWO_PI)
        line_ = words[i]
        push_matrix()
        translate(0.0, i*75, 0.0)
        for j in range(len(line_)):
            if j != 0:
                translate(text_width(line_[j - 1]) * 75, 0.0, 0.0)
            rotate_y(f1 * 0.005 * f2)
            push_matrix()
            scale(75.0)
            text(line_[j], 0.0, 0.0)
            pop_matrix()
        pop_matrix()
    pop_matrix()
