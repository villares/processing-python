def setup():
    size(200, 200)
    rect_mode(CENTER)


def draw():
    background(255)
    fill(100)
    rect(40, 40, 40, 40)
    with push_matrix():
        translate(mouse_x, mouse_y)
        rotate(radians(frame_count))
        fill(255)
        rect(0, 0, 40, 40)
        with push_matrix():
            translate(20, 20)
            rotate(radians(frame_count*3))
            fill(200)
            rect(0, 0, 20, 20)
