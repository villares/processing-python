# JCSG library adapted for use with Processing by George Profenza https://stackoverflow.com/users/89766/george-profenza
# https://stackoverflow.com/questions/56999816/is-it-possible-to-use-jcsg-library-with-processing

# You'll need to copy these libs into your Processing libraries folder:
#add_library('VVecMath')
#add_library('jcsg')
import py5
#from VVecMath import *
from jcsg import Cube

def setup():
    global pshape_result
    size(600, 500, P3D)
    no_stroke()
    csg_result = calculate_stuff()
    pshape_result = CSGToPShape(csg_result, 45)


def draw():
    background(0)
    lights()
    translate(width * 0.5, height * 0.5, 0)
    rotate_y(map(mouse_x, 0, width, -PI, PI))
    rotate_x(map(mouse_y, 0, height, PI, -PI))
    shape(pshape_result)


def calculate_stuff():
    # Jsample code:
    # we use cube and sphere_ as base geometries
    cube = Cube(2).to_csg()
    sphere_ = Sphere(1.25).to_csg()

    # perform union, difference and intersection
    cube_plus_sphere = cube.union(sphere_)
    cube_minus_sphere = cube.difference(sphere_)
    cube_intersect_sphere = cube.intersect(sphere_)

    sphere_ = csg_translate(sphere_, 3, 0, 0)
    cube_plus_sphere = csg_translate(cube_plus_sphere, 6, 0, 0)
    cube_minus_sphere = csg_translate(cube_minus_sphere, 9, 0, 0)
    cube_intersect_sphere = csg_translate(cube_intersect_sphere, 12, 0, 0)

    union = cube.union((sphere_,
                        cube_plus_sphere,
                        cube_minus_sphere,
                        cube_intersect_sphere))

    # translate merged geometry back by half to pivot around centre
    return csg_translate(union, -6, 0, 0)


def csg_translate(csg, x, y, z):
    return csg.transformed(Transform.unity().translate(x, y, z))


def CSGToPShape(mesh, scale):
    """
    Convert a CSG mesh to a Processing PShape
    """
    result = create_shape(GROUP)  # allocate a PShape group
    # for each polygon (Note: these can have 3,4 or more vertices)
    for p in mesh.get_polygons():
        # make a child PShape
        poly_shape = create_shape()
        # begin setting vertices to it
        poly_shape.begin_shape()
        # for each vertex in the polygon
        for v in p.vertices:
            # add each (scaled) polygon vertex
            poly_shape.vertex(v.pos.get_x() * scale,
                              v.pos.get_y() * scale,
                              v.pos.get_z() * scale)

        # finish this polygon
        poly_shape.end_shape()
        # append the child PShape to the parent
        result.add_child(poly_shape)

    return result


def key_pressed():
    save_frame("###.png")
