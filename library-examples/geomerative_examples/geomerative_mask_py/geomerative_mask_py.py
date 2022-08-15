add_library('geomerative')    # import geomerative.*


def setup():
    size(400, 400)
    smooth()
    global shp1, shp2, shp3
    global cursor_shape
    RG.init(this)

    shp1 = RG.loadShape("Toucan.svg")
    shp2 = RShape.createStar(0, 0, 100.0, 80.0, 20)

    shp1.center_in(g)


def draw():
    background(255)
    translate(width / 2, height / 2)

    cursor_shape = RShape(shp2)
    cursor_shape.translate(mouse_x - width / 2, mouse_y - height / 2)

    # Only intersection() does not work for shapes with more than one path
    shp3 = RG.intersection(shp1, cursor_shape)

    stroke_weight(3)

    if mouse_pressed:
        fill(0, 220, 0, 30)
        stroke(0, 120, 0)
        RG.shape(shp1)

        fill(220, 0, 0, 30)
        stroke(120, 0, 0)
        RG.shape(cursor_shape)

    else:
        fill(220)
        stroke(120)
        RG.shape(shp3)
