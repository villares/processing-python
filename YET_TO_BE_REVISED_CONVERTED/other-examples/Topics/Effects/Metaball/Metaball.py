"""
  Metaball Demo Effect
  by luis2048. (Adapted to Python by Jonathan Feinberg)

  Organic-looking n-dimensional objects. The technique for rendering
  metaballs was invented by Jim Blinn in the early 1980s. Each metaball
  is defined as a function in n-dimensions.
"""

num_blobs = 3

# Position vector for each blob
blog_px = [0, 90, 90]
blog_py = [0, 120, 45]

# Movement vector for each blob
blog_dx = [1, 1, 1]
blog_dy = [1, 1, 1]

pg = None


def setup():
    global pg
    size(640, 360)
    pg = create_graphics(160, 90)

    this.surface.set_title("Processing.py")


def draw():
    vx, vy = [], []
    for i in range(num_blobs):
        blog_px[i] += blog_dx[i]
        blog_py[i] += blog_dy[i]

        # bounce across screen
        if blog_px[i] < 0:
            blog_dx[i] = 1
        if blog_px[i] > pg.width:
            blog_dx[i] = -1
        if blog_py[i] < 0:
            blog_dy[i] = 1
        if blog_py[i] > pg.height:
            blog_dy[i] = -1

        vx.append(tuple(sq(blog_px[i] - x) for x in xrange(pg.width)))
        vy.append(tuple(sq(blog_py[i] - y) for y in xrange(pg.height)))

  # Output into a buffered image for reuse
    pg.begin_draw()
    for y in range(pg.height):
        for x in range(pg.width):
            m = 1
            for i in range(num_blobs):
                # Increase this number to make your blobs bigger
                m += 60000 / (vy[i][y] + vx[i][x] + 1)
                pg.set(x, y, color(0, m + x, (x + m + y) / 2))
    pg.end_draw()

  # Display the results
    image(pg, 0, 0, width, height)
