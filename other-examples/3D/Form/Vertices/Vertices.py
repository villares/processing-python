from java.lang import System
System.setProperty("jogl.disable.openglcore", "false")
"""
  Vertices
  by Simon Greenwold.
  (Rewritten in Python by Jonathan Feinberg.)

  Draw a cylinder centered on the y-axis, going down
  from y=0 to y=height. The radius at the top can be
  different from the radius at the bottom, and the
  number of sides drawn is variable.
 """


def setup():
    size(640, 360, P3D)


def draw():
    background(0)
    lights()
    translate(width / 2, height / 2)
    rotate_y(map(mouse_x, 0, width, 0, PI))
    rotate_z(map(mouse_y, 0, height, 0, -PI))
    no_stroke()
    fill(255, 255, 255)
    translate(0, -40, 0)
    draw_cylinder(10, 180, 200, 16)  # Draw a mix between a cylinder and a cone
    # drawCylinder(70, 70, 120, 64) # Draw a cylinder
    # drawCylinder(0, 180, 200, 4) # Draw a pyramid


def draw_cylinder(top_radius, bottom_radius, tall, sides):
    angle = 0
    angle_increment = TWO_PI / sides
    begin_shape(QUAD_STRIP)
    for i in range(sides + 1):
        vertex(top_radius * cos(angle), 0, top_radius * sin(angle))
        vertex(bottom_radius * cos(angle), tall, bottom_radius * sin(angle))
        angle += angle_increment
    end_shape()

    # If it is not a cone, draw the circular top cap
    if top_radius:
        angle = 0
        begin_shape(TRIANGLE_FAN)
        # Center point
        vertex(0, 0, 0)
        for i in range(sides + 1):
            vertex(top_radius * cos(angle), 0, top_radius * sin(angle))
            angle += angle_increment
        end_shape()

    # If it is not a cone, draw the circular bottom cap
    if bottom_radius:
        angle = 0
        begin_shape(TRIANGLE_FAN)
        # Center point
        vertex(0, tall, 0)
        for i in range(sides + 1):
            vertex(
                bottom_radius *
                cos(angle),
                tall,
                bottom_radius *
                sin(angle))
            angle += angle_increment
        end_shape()
