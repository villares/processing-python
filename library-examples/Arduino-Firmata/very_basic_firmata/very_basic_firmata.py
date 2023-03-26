"""
Requires Firmata (Arduino) to be installed on Processing
Ajust SERIAL to the USB port where your Arduino is connected
May require 'sudo chmod 666 /dev/ttyUSB0' (YMMV).
"""

# ARDUINO
add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

for num, port in enumerate(Arduino.list()):  # Serial ports
    print(str(num)+":"+port)               # on console
SERIAL = 0  # Please change if needed!

POT_1 = 5   # Pin number for 1st Pot
POT_2 = 0   # Pin number for 2nd Pot


def setup():
    color_mode(HSB)  # Not using RGB mode this time ;)
    frame_rate(30)
    size(1024, 1024)  # Screen size
    global arduino
    arduino = Arduino(this, Arduino.list()[SERIAL], 57600)
    background(255)
    no_stroke()


def draw():
    # background(0)
    X = arduino.analog_read(POT_1)
    Y = arduino.analog_read(POT_2)
    fill(frame_count % 255, 200, 255)  # notice HSB mode on setup!
    ellipse(X, Y, 20, 20)
    clear_screen = key_pressed  # arduino.digitalRead(2)
    if clear_screen:
        background(195, 183, 242)  # light blue
