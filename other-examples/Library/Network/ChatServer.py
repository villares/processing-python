"""
Chat Server by Tom Igoe.

Press the mouse to stop the server.
"""

add_library('net')  # import processing.net.*

port = 10002
my_server_running = True
bg_color = 0
direction = 1
text_line = 60


def setup():
    global my_server
    size(400, 400)
    text_font(create_font("SanSerif", 16))
    my_server = Server(this, port)  # Starts a myServer on port 10002
    background(0)


def mouse_pressed():
    global my_server_running
    # If the mouse clicked the myServer stops
    my_server.stop()
    my_server_running = False


def draw():
    if my_server_running:
        text("server", 15, 45)
        this_client = my_server.available()
        if this_client:  # not None
            if this_client.available():  # thisClient.available() > 0
                text("mesage from: " + thisClient.ip() + " : " +
                     this_client.read_string(), 15, text_line)
                text_line = text_line + 35
    else:
        text("server", 15, 45)
        text("stopped", 15, 65)
