def setup():
    size(400, 400)
    no_fill()


def draw():
    background(200)
    stroke_weight(remap(mouse_x, 0, width, 1, 10))
    stroke(255)
    ellipse(100, 100, 30, 30)
    ellipse(100, 300, 30, 30)
    stroke(0)
    arrow(100, 100, 100, 300, shorter=30, head=30)
    arrow(150, 100, 150, 300, tail_func=rect)
    arrow(200, 100, 200, 300, 30, 30, tail_func=ellipse)
    arrow(50, 100, 350, 300)


def arrow(x1, y1, x2, y2, shorter=0, head=None,
          tail_func=None, tail_size=None):
    """
    O código para fazer as setas, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    e para o tamanho da cabeça da seta: head
    """
    L = dist(x1, y1, x2, y2)
    if not head:
        head = max(L / 10, 10)
    with push_matrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = shorter / 2
        stroke_cap(ROUND)
        line(0, L - offset, -head / 3, L - offset - head)
        line(0, L - offset, head / 3, L - offset - head)
        stroke_cap(SQUARE)
        line(0, offset, 0, L - offset)

        if tail_func:
            if not tail_size:
                tail_size = head
            tail_func(0, 0, tail_size, tail_size)