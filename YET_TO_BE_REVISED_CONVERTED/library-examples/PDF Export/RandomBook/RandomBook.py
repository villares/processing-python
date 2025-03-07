"""
RandomBook

Creates a 768 page book of random lines.
"""

add_library('pdf')  # import processing.pdf.*


def setup():
    global pdf
    size(594, 842)
    # randomSeed(0) # Uncomment to make the same book each time
    pdf = begin_record(PDF, "RandomBook.pdf")
    begin_record(pdf)


def draw():
    background(255)

    for i in range(100):
        r = random(1.0)
        if r < 0.2:
            stroke(255)
        else:
            stroke(0)

        sw = pow(random(1.0), 12)
        stroke_weight(sw * 260)
        x1 = random(-200, -100)
        x2 = random(width + 100, width + 200)
        y1 = random(-100, height + 100)
        y2 = random(-100, height + 100)
        line(x1, y1, x2, y2)

    if frame_count == 768:
        end_record()
        exit()    # Quit
    else:
        pdf.next_page()  # Tell it to go to the next page
