"""
Perspective.

Move the mouse left or right to change the field of view (fov).
Click to modify the aspect ratio. The perspective() function
sets a perspective projection applying foreshortening, making
distant objects appear smaller than closer ones. The parameters
define a viewing volume with the shape of truncated pyramid.
Objects near to the front of the volume appears to be in their actual size,
while farther objects appears to be smaller than original. This projection simulates
the perspective of the world more accurately than orthographic projection.
The version of perspective without parameters sets the default
perspective and the version with four parameters allows the programmer
to set the area precisely.
"""


def setup():
    size(640, 360, P3D)
    no_stroke()


def draw():
    lights()
    background(204)
    camera_y = height / 2.0
    fov = mouse_x / float(width) * PI / 2
    camera_z = camera_y / max(1, tan(fov / 2.0))
    aspect = float(width) / float(height)
    if mouse_pressed:
        aspect = aspect / 2.0

    perspective(fov, aspect, camera_z / 10.0, camera_z * 10.0)
    translate(width / 2 + 30, height / 2, 0)
    rotate_x(-PI / 6)
    rotate_y(THIRD_PI + PI * mouse_y / height)
    box(45)
    translate(0, 0, -50)
    box(30)
