add_library('geomerative')


def setup():
    global shp1, shp2
    size(400, 400)
    smooth()

    RG.init(this)

    shp1 = RShape.createRing(0, 0, 120, 50)
    shp2 = RShape.createStar(0, 0, 100.0, 80.0, 20)


def draw():

    background(255)
    translate(width / 2, height / 2)

    cursor_shape = RShape(shp2)
    cursor_shape.translate(mouse_x - width / 2, mouse_y - height / 2)

    # Only intersection() does not work for shapes with more than one path
    shp3 = RG.diff(shp1, cursor_shape)

    stroke_weight(3)

    if(mouse_pressed):
        fill(220, 0, 0, 30)
        stroke(120, 0, 0)
        RG.shape(cursor_shape)

        fill(0, 220, 0, 30)
        stroke(0, 120, 0)
        RG.shape(shp1)

    else:
        fill(220)
        stroke(120)
        RG.shape(shp3)
