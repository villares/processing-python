# import fontastic.*
# import geomerative.*
add_library('Fontastic')
add_library('geomerative')

version = 0
char_width = 512
font_built = False


def setup():
    global font
    size(600, 400)
    fill(0)

    # always initialize the library in setup
    RG.init(this)

    # load the initial font
    font = RFont("FreeSans.ttf", 150)
    # get the points on the curve's shape
    # set style and segment resultion
    RCommand.setSegmentLength(10)
    RCommand.setSegmentator(RCommand.UNIFORMLENGTH)
    init_font()
    update_font()


def draw():
    update_font()
    background(255)
    number_of_letters = 10    # the number of letters to display
    for i in range(number_of_letters):
        push_matrix()
        translate(width / 2, height / 3)
        scale(char_width / 1000. / 5.)
        translate(-(number_of_letters - 1) *
                  char_width / 2 + i * char_width, 0)
        translate(-char_width / 2, char_width / 2)
        no_stroke()
        fill(0, 128, 255)
        render_glyph_solid(Fontastic.alphabet[i], f)
        pop_matrix()

    if font_built:
        push_matrix()
        text_font(my_font)
        text_align(CENTER, CENTER)
        fill(0)
        text_size(char_width / 5.)
        text(str(subset(Fontastic.alphabet, 0, number_of_letters)),
             width / 2, height * 0.6)
        pop_matrix()
        for i in range(number_of_letters):
            push_matrix()
            translate(width / 2, height / 3)
            scale(char_width / 1000. / 5.)
            translate(-(number_of_letters - 1) *
                      char_width / 2 + i * char_width, 0)
            translate(-char_width / 2, height * 0.6)
            no_stroke()
            fill(0, 128, 255)
            render_glyph_solid(Fontastic.alphabet[i + 5], f)
            pop_matrix()


def init_font():
    global f
    # create new Fontastic object
    f = Fontastic(this, "Confetti" + nf(version, 4))
    # add letters to the font, adding glyph shapes
    for c in Fontastic.alphabet:
        # add all uppercase letters from the alphabet
        f.add_glyph(c)
    for c in Fontastic.alphabetLc:
        # add all lowercase letters from the alphabet
        f.add_glyph(c)


# f.setFontFamilyName("Confetti");    # if font has same name, won't be
# loaded twice by Processing during runtime
    f.set_author("Andreas Koller")
    f.set_version("0.1")
    f.set_advance_width(int(char_width * 1.1))


def update_font():
    for c in Fontastic.alphabet:
        shp = font.to_shape(c)
        pnts = shp.get_points()  # RPoint[]
        f.get_glyph(c).clear_contours()
        for i in range(len(pnts)-1):
            p = pnts[i]
            circle_size = 20
            resolution = 6  # the resolution of a confetti circle
            points = [Py5Vector()]*resolution
            for j in range(resolution):
                angle = TWO_PI/(resolution * 1.) * j
                x = p.x * 5 + sin(angle) * circle_size
                y = -p.y * 5 + cos(angle) * circle_size
                x += (mouse_x - width/2.) / width/2. * \
                    noise(i+millis()/1000.) * 2000
                y -= (mouse_y - height/2.) / height/2. * \
                    noise(i * 2+millis()/1000.) * 2000
                points[j] = Py5Vector(x, y)
            f.get_glyph(c).add_contour(points)


def create_my_font():
    global my_font, version, font_built
    f.build_font()  # write ttf file
    # delete all glyph files that have been created while building the font
    f.cleanup()
    font_built = True
    # set the font to be used for rendering
    # print f.getTTFfilename()
    my_font = create_font(f.get_tt_ffilename(), 200)
    version += 1
    init_font()  # and make a new font right away

# A function to preview a glyph in Processing


def render_glyph_solid(c, f):
    contours = f.get_glyph(c).get_contours_array()  # FContour[]

    for j in range(len(contours)):
        # FPoint[]
        points = f.get_glyph(c).get_contour(j).get_points_array()

        if len(points) > 0:  # just to be sure
            # Draw the solid shape in Processing
            begin_shape()
            for i, p1 in enumerate(points):
                # p1 = points[i]
                p2 = points[(i + 1) % len(points)]
                if p1.has_control_point2() and p2.has_control_point1():
                    if i == 0:
                        vertex(points[0].x, -points[0].y)

                    bezier_vertex(p1.control_point2.x, -
                                  p1.control_point2.y, p2.control_point1.x, -
                                  p2.control_point1.y, p2.x, -
                                  p2.y)
                else:
                    vertex(p1.x, -p1.y)
            end_shape()


def key_pressed():
    if key == 's':
        create_my_font()
