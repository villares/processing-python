"""
Shared Drawing Canvas (Server) by Alexander R. Galloway.

A server that shares a drawing canvas between two computers.
In order to open a socket connection, a server must select a
port on which to listen for incoming clients and through which
to communicate. Once the socket is established, a client may
connect to the server and send or receive commands and data.
Get this program running and then start the Shared Drawing
Canvas (Client) program so see how they interact.
"""

add_library('net')  # import processing.net.*


def setup():
    global s
    size(450, 255)
    background(204)
    stroke(0)
    frame_rate(5)  # Slow it down a little
    s = Server(this, 12345)  # Start a simple server on a port


def draw():
    if mouse_pressed:
        # Draw our line
        stroke(255)
        line(pmouse_x, pmouse_y, mouse_x, mouse_y)
        # Send mouse coords to other person
        s.write(str(pmouse_x) + " " +
                str(pmouse_y) + " " +
                str(mouse_x) + " " +
                str(mouse_y) + "\n")
    # Receive data from client
    c = s.available()
    if c:  # c not null/None
        input = c.read_string()
        input = input[:input.find("\n")]  # Only up to the newline
        data = [int(coord)
                for coord in input.split()]  # Split values into list
        # Draw line using received coords
        stroke(0)
        line(data[0], data[1], data[2], data[3])
