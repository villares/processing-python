"""
  Noise Wave
  by Daniel Shiffman.

  Using Perlin Noise to generate a wave-like pattern.
"""

xspacing = 8   # How far apart should each horizontal location be spaced

yoff = 0.0       # 2nd dimension of perlin noise
# Using an array to store height values for the wave (not entirely necessary)
yvalues = None


def setup():
    size(200, 200)
    frame_rate(30)
    color_mode(RGB, 255, 255, 255, 100)
    smooth()
    global yvalues
    yvalues = [i for i in range((width + 16) / xspacing)]


def draw():
    background(0)
    calc_wave()
    render_wave()


def calc_wave():
    dx = 0.05
    dy = 0.01
    amplitude = 100.0

    # Increment y ('time')
    global yoff
    yoff += dy

    # xoff = 0.0  # Option #1
    xoff = yoff  # Option #2

    for i in range(len(yvalues)):
        # Using 2D noise function
        #yvalues[i] = (2*noise(xoff,yoff)-1)*amplitude
        # Using 1D noise function
        yvalues[i] = (2 * noise(xoff) - 1) * amplitude
        xoff += dx


def render_wave():
    # A simple way to draw the wave with an ellipse at each location
    for x, v in enumerate(yvalues):
        no_stroke()
        fill(255, 50)
        ellipse_mode(CENTER)
        ellipse(x * xspacing, width / 2 + v, 16, 16)
