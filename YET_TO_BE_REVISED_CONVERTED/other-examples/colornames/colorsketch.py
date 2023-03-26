"""
Demonstrates using a third-party Python library
author: Jonathan Feinberg
"""
from namethatcolor import NameThatColor

namer = NameThatColor()


def setup():
    size(200, 200)
    global flag
    flag = load_image("flag.jpg")


def draw():
    background(0)
    image(flag, 75, 40)
    if mouse_x >= 0 and mouse_x <= width and mouse_y >= 0 and mouse_y <= height:
        c = 0x00FFFFFF & get(mouse_x, mouse_y)
        fill(c >> 16, c >> 8 & 0xFF, c & 0xFF)
        text(namer.name(hex(c)[2:]).name, 75, 120)
