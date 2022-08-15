"""
 Space Junk
 by Ira Greenberg.
 Zoom suggestion
 by Danny Greenberg.
 (Rewritten in Python by Jonathan Feinberg.)

 Rotating cubes in space.
 Color controlled by light sources.
 Move the mouse left and right to zoom.
"""

# Cube count-lower/raise to test P3D/OPENGL performance
limit = 500

# List of cubes, where each cube is a tuple
# (width, height, depth, x, y, z)
cubes = [(random(-10, 10), random(-10, 10), random(-10, 10),
          random(-140, 140), random(-140, 140), random(-140, 140))
         for i in range(limit)]


def setup():
    size(1024, 768, OPENGL)
    background(0)
    no_stroke()


def draw():
    background(0)
    fill(200)

    # Set up some different colored lights
    point_light(51, 102, 255, 65, 60, 100)
    point_light(200, 40, 60, -65, -60, -150)

    # Raise overall light in scene
    ambient_light(70, 70, 10)

    # Center geometry in display windwow.
    # you can change 3rd argument ('0')
    # to move block group closer(+)/further(-)
    translate(width / 2, height / 2, -200 + mouse_x * 0.65)

    # Rotate around y and x axes
    rotate_y(frame_count * .01)
    rotate_x(frame_count * .01)

    # Draw cubes
    for cube in cubes:
        push_matrix()
        translate(cube[3], cube[4], cube[5])
        box(cube[0], cube[1], cube[2])
        pop_matrix()
        rotate_y(.01)
        rotate_x(.01)
        rotate_z(.01)
