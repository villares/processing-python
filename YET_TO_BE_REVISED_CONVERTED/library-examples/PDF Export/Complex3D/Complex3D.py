"""
PDF Complex by Marius Watz (workshop.evolutionzone.com).

Example using PDF to output complex 3D geometry for print.
Press "s" to save a PDF.
"""

add_library('pdf')  # import processing.pdf.*

# Trig lookup tables (sinLUT and cosLUT) borrowed from Toxi.
# Cryptic but effective.
SINCOS_PRECISION = 1.0
SINCOS_LENGTH = int(360.0 / SINCOS_PRECISION)
# System data
do_save = False


def setup():
    global sin_lut, cos_lut, num, pt, style
    size(600, 600, OPENGL)
    frame_rate(24)
    background(255)
    # Fill the tables
    sin_lut = [sin(i * DEG_TO_RAD * SINCOS_PRECISION)
               for i in range(SINCOS_LENGTH)]
    cos_lut = [cos(i * DEG_TO_RAD * SINCOS_PRECISION)
               for i in range(SINCOS_LENGTH)]
    num = 150
    pt = [0.0 for _ in range(6 * num)]  # rotx, roty, deg, rad, w, speed
    style = [0 for _ in range(2 * num)]  # color, render style
    # Set up arc shapes
    index = 0
    for i in range(num):
        pt[index + 0] = random(TWO_PI)  # Random X axis rotation
        pt[index + 1] = random(TWO_PI)  # Random Y axis rotation
        pt[index + 2] = random(60, 80)  # Short to quarter-circle arcs
        if random(100) > 90:
            pt[index + 2] = int(random(8, 27) * 10.0)
        # Radius. Space them out nicely
        pt[index + 3] = int(random(2, 50) * 5.0)
        pt[index + 4] = random(4, 32)  # Width of band
        if random(100) > 90:
            pt[index + 4] = random(40, 60)  # Width of band
        pt[index + 5] = radians(random(5, 30)) / 5.0  # Speed of rotation
        index += 6
        # get colors
        prob = random(100)
        if prob < 30:
            style[i * 2] = rgb_blend(random(1), 255, 0, 100, 255, 0, 0, 210)
        elif prob < 70:
            style[i * 2] = rgb_blend(random(1), 0, 153,
                                     255, 170, 225, 255, 210)
        elif prob < 90:
            style[i * 2] = rgb_blend(random(1), 200, 255, 0, 150, 255, 0, 210)
        else:
            style[i * 2] = color(255, 255, 255, 220)
        if prob < 50:
            style[i * 2] = rgb_blend(random(1), 200, 255, 0, 50, 120, 0, 210)
        elif prob < 90:
            style[i * 2] = rgb_blend(random(1), 255, 100, 0, 255, 255, 0, 210)
        else:
            style[i * 2] = color(255, 255, 255, 220)
        style[i * 2 + 1] = int(random(100)) % 3


def draw():
    global do_save
    if do_save:
        # set up PGraphicsPDF for use with beginRaw()
        pdf = begin_raw(PDF, "pdf_complex_out.pdf")
        # set default Illustrator stroke styles and paint background rect.
        pdf.stroke_join(MITER)
        pdf.stroke_cap(SQUARE)
        pdf.fill(0)
        pdf.no_stroke()
        pdf.rect(0, 0, width, height)
    background(0)
    index = 0
    translate(width / 2, height / 2, 0)
    rotate_x(PI / 6.0)
    rotate_y(PI / 6.0)
    for i in range(num):
        with push_matrix():
            rotate_x(pt[index + 0])
            rotate_y(pt[index + 1])
            if style[i * 2 + 1] == 0:
                stroke(style[i * 2])
                no_fill()
                stroke_weight(1)
                arc_line(0, 0, pt[index + 2], pt[index + 3], pt[index + 4])
            elif style[i * 2 + 1] == 1:
                fill(style[i * 2])
                no_stroke()
                arc_line_bars(0, 0, pt[index + 2],
                              pt[index + 3], pt[index + 4])
            else:
                fill(style[i * 2])
                no_stroke()
                arc(0, 0, pt[index + 2], pt[index + 3], pt[index + 4])
            # increase rotation
            pt[index + 0] += pt[index + 5] / 10.0
            pt[index + 1] += pt[index + 5] / 20.0
            index += 6
    if do_save:
        end_raw()
        do_save = False

# Get blend of two colors


def rgb_blend(fract, r, g, b, r2, g2, b2, a):
    r2, g2, b2 = (r2 - r), (g2 - g), (b2 - b)
    return color(r + r2 * fract, g + g2 * fract, b + b2 * fract, a)

# Draw arc line


def arc_line(x, y, deg, rad, w):
    a = int(min(deg / SINCOS_PRECISION, SINCOS_LENGTH - 1.0))
    numlines = int(w / 2)
    for j in range(numlines):
        begin_shape()
        for i in range(a):
            vertex(cos_lut[i] * rad + x,
                   sin_lut[i] * rad + y)
        end_shape()
        rad += 2

# Draw arc line with bars


def arc_line_bars(x, y, deg, rad, w):
    a = int((min(deg / SINCOS_PRECISION, SINCOS_LENGTH - 1.0)))
    a /= 4
    begin_shape(QUADS)
    for i in range(0, a, 4):
        vertex(cos_lut[i] * (rad) + x,
               sin_lut[i] * (rad) + y)
        vertex(cos_lut[i] * (rad + w) + x,
               sin_lut[i] * (rad + w) + y)
        vertex(cos_lut[i + 2] * (rad + w) + x,
               sin_lut[i + 2] * (rad + w) + y)
        vertex(cos_lut[i + 2] * (rad) + x,
               sin_lut[i + 2] * (rad) + y)
    end_shape()

# Draw solid arc


def arc(x, y, deg, rad, w):
    a = int(min(deg / SINCOS_PRECISION, SINCOS_LENGTH - 1.0))
    begin_shape(QUAD_STRIP)
    for i in range(a):
        vertex(cos_lut[i] * (rad) + x,
               sin_lut[i] * (rad) + y)
        vertex(cos_lut[i] * (rad + w) + x,
               sin_lut[i] * (rad + w) + y)
    end_shape()


def key_pressed():
    if (key == 's'):
        do_save = True


def mouse_released():
    background(255)
