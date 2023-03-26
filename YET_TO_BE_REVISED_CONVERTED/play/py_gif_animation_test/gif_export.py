# -*- coding: utf-8 -*-

"""
gif_export.py - a GIF Animation export helper for Processing Python mode - v2020_06_01
Alexandre B A Villares http://abav.lugaralgum.com - Licensed under GPL v3
Inspired by an example by Art Simon https://github.com/APCSPrinciples/AnimatedGIF/

This is for use with the gifAnimation library https://github.com/extrapixel/gif-animation/tree/3.0
Download the library from github.com/extrapixel/gif-animation/archive/3.0.zip
Unzip and copy the gifAnimation folder into your libraries folder, like shown below:
    user/sketchbook/libraries/gifAnimation (Linux) or
    user/Documents/Processing/libraries/gifAnimation (Mac/Windows)

# This file should be saved as a 'tab' named gif_export.py in your Processing Python Mode sketch
# Restart the IDE and add these lines at the start of your sketch:
add_library('gifAnimation')
from gif_export import gif_export

# then add this at the end of draw():
gif_export(GifMaker, "filename")

"""


def gif_export(GifMaker,             # gets a reference to the library
               filename="exported",  # .gif will be added
               repeat=0,             # 0 makes it an "endless" animation
               quality=100,
               # quality range 0 - 255 test yourself,my guess is 0 best/high
               # 255 worst/low
               delay=170,            # this is quick
               frames=0,             # 0 will stop only if 'e' key pressed
               transparent=None,     # set a transparent color
               finish=False):        # force stop
    global gif_exporter
    try:
        gif_exporter
    except NameError:
        gif_exporter = GifMaker(this, filename + ".gif")
        gif_exporter.set_repeat(repeat)
        gif_exporter.set_quality(quality)
        gif_exporter.set_delay(delay)
        if transparent is not None:
            gif_exporter.set_transparent(transparent)
        print("gif recording started")

    gif_exporter.add_frame()

    if frames == 0:
        if key_pressed and key == 'e':
            finish = True
    elif frame_count >= frames:
        finish = True

    if finish:
        gif_exporter.finish()
        print("gif saved, exit")
        exit()
