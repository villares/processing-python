"""
 Interactive Toroid
 PDE by Ira Greenberg, rewritten in Python by Jonathan Feinberg

 Illustrates the geometric relationship between Toroid, Sphere, and Helix
 3D primitives, as well as lathing principal.

 Instructions:
 UP arrow key pts++
 DOWN arrow key pts--
 LEFT arrow key segments--
 RIGHT arrow key segments++
 'a' key toroid radius--
 's' key toroid radius++
 'z' key initial polygon radius--
 'x' key initial polygon radius++
 'w' key toggle wireframe/solid shading
 'h' key toggle sphere/helix
"""

pts = 40
radius = 60.0

# lathe segments
segments = 60
lathe_radius = 100.0

# for shaded or wireframe rendering
is_wire_frame = False

# for optional helix
is_helix = False
helix_offset = 5.0

# The extruded shape as a list of quad strips
strips = []


def setup():
    size(640, 360, OPENGL)


def extrude():
    d_theta = TWO_PI / pts
    helical_offset = 0
    if is_helix:
        helical_offset = - (helix_offset * segments) / 2
    vertices1 = [[lathe_radius + sin(d_theta * x) * radius,
                 cos(d_theta * x) * radius + helical_offset]
                for x in range(pts + 1)]
    vertices2 = [[0.0, 0.0, 0.0] for x in range(pts + 1)]

    # draw toroid
    lathe_angle = 0
    d_theta = TWO_PI / segments
    if is_helix:
        d_theta *= 2
    for i in range(segments + 1):
        verts = []
        for j in range(pts + 1):
            v2 = vertices2[j]
            if i > 0:
                verts.append(v2[:])

            v2[0] = cos(lathe_angle) * vertices1[j][0]
            v2[1] = sin(lathe_angle) * vertices1[j][0]
            v2[2] = vertices1[j][1]
            # optional helix offset
            if is_helix:
                vertices1[j][1] += helix_offset

            verts.append(v2[:])
        strips.append(verts)
        lathe_angle += d_theta


def draw():
    if not len(strips):
        extrude()

    background(50, 64, 42)
    # basic lighting setup
    lights()

    # 2 rendering styles
    # wireframe or solid
    if is_wire_frame:
        stroke(255, 255, 150)
        no_fill()
    else:
        no_stroke()
        fill(150, 195, 125)

    text(f'{get_frame_rate()}', 20, 40)
    # center and spin toroid
    translate(width / 2, height / 2, -100)
    rotate_x(frame_count * PI / 150)
    rotate_y(frame_count * PI / 170)
    rotate_z(frame_count * PI / 90)

    # draw toroid
    for strip in strips:
        begin_shape(QUAD_STRIP)
        for v in strip:
            vertex(v[0], v[1], v[2])
        end_shape()


"""
 left/right arrow keys control ellipse detail
 up/down arrow keys control segment detail.
 'a','s' keys control lathe radius
 'z','x' keys control ellipse radius
 'w' key toggles between wireframe and solid
 'h' key toggles between toroid and helix
 """


def key_pressed():
    global pts, segments, is_helix, is_wire_frame, lathe_radius, radius

    # clear the list of strips, to force a re-evaluation
    del strips[:]

    if key == CODED:
        # pts
        if key_code == UP:
            if pts < 40:
                pts += 1
        elif key_code == DOWN:
            if pts > 3:
                pts -= 1
        # extrusion length
        if key_code == LEFT:
            if segments > 3:
                segments -= 1
        elif key_code == RIGHT:
            if segments < 80:
                segments += 1
    # lathe radius
    elif key == 'a':
        if lathe_radius > 0:
            lathe_radius -= 1
    elif key == 's':
        lathe_radius += 1
    # ellipse radius
    elif key == 'z':
        if radius > 10:
            radius -= 1
    elif key == 'x':
        radius += 1
    # wireframe
    elif key == 'w':
        is_wire_frame = not is_wire_frame
    # helix
    elif key == 'h':
        is_helix = not is_helix
