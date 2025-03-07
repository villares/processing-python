"""
HTTP Client.

Starts a network client that connects to a server on port 80,
sends an HTTP 1.0 GET request, and prints the results.

Note that this code is not necessary for simple HTTP GET request:
Simply calling loadStrings("http://www.processing.org") would do
the same thing as (and more efficiently than) this example.
This example is for people who might want to do something more
complicated later.
"""

add_library('net')  # import processing.net.*


def setup():
    global c
    size(200, 200)
    background(50)
    fill(200)
    c = Client(this, "www.ucla.edu", 80)  # Connect to server on port 80
    # Use the HTTP "GET" command to ask for a Web page
    c.write("GET / HTTP/1.0\r\n")
    c.write("\r\n")


def draw():
    if c.available():  # If there's incoming data from the client...
        data = c.read_string()  # ...then grab it and print it
        print(data)
