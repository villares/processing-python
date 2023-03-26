from java.lang import System
System.setProperty("jogl.disable.openglcore", "false")
'''
 Brick Tower
 by Ira Greenberg.

 3D castle tower constructed out of individual bricks.
'''

bricks_per_layer = 16.0
brick_layers = 18
brick_width = 60
brick_height = 25
brick_depth = 25
radius = 175.0


def setup():
    size(640, 360, OPENGL)


def draw():
    background(0)
    (temp_x, temp_y, temp_z) = (0, 0, 0)
    fill(182, 62, 29)
    no_stroke()
    # Add basic light setup
    lights()
    translate(width / 2, height * 1.2, -380)
    # Tip tower to see inside
    rotate_x(radians(-45))
    # Slowly rotate tower
    rotate_y(frame_count * PI / 600)
    for i in xrange(brick_layers):
        # Increment rows
        temp_y -= brick_height
        # Alternate brick seams
        angle = 360.0 / bricks_per_layer * i / 2
        for j in xrange(bricks_per_layer):
            temp_z = cos(radians(angle)) * radius
            temp_x = sin(radians(angle)) * radius
            push_matrix()
            translate(temp_x, temp_y, temp_z)
            rotate_y(radians(angle))
            # Add crenelation
            if (i == brick_layers - 1):
                if (j % 2 == 0):
                    box(brick_width, brick_height, brick_depth)
            else:
                # Create main tower
                box(brick_width, brick_height, brick_depth)
            pop_matrix()
            angle += 360.0 / bricks_per_layer
