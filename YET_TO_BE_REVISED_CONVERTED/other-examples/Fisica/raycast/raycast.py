"""
 *    Raycast
 *
 *    by Ricard Marxer
 *
 *    This example shows how to use the raycasts.
 """
from fisica import Fisica, FWorld, FBody, FBox, FRaycastResult
add_library('fisica')

# import org.jbox2d.common.*

world, obstacle = None, None


def setup():
    global world, obstacle
    size(400, 400)
    smooth()
    Fisica.init(this)
    world = FWorld()
    obstacle = FBox(150, 150)
    obstacle.set_rotation(PI/4)
    obstacle.set_position(width/2, height/2)
    obstacle.set_static(True)
    obstacle.set_fill(0)
    obstacle.set_restitution(0)
    world.add(obstacle)


def draw():
    background(255)
    world.draw()
    world.step()

    cast_ray()


def cast_ray():
    result = FRaycastResult()
    b = world.raycast_one(width/2, height, mouse_x, mouse_y, result, True)
    stroke(0)
    line(width/2, height, mouse_x, mouse_y)
    if b:
        b.set_fill(120, 90, 120)
        fill(180, 20, 60)
        no_stroke()

        x = result.get_x()
        y = result.get_y()
        ellipse(x, y, 10, 10)
    else:
        obstacle.set_fill(0)


def key_pressed():
    save_frame("screenshot.png")
