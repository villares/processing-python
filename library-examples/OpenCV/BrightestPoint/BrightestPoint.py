add_library('opencv_processing')

src = load_image("robot_light.jpg")
src.resize(800, 0)
size(src.width, src.height)
opencv = OpenCV(this, src)
image(opencv.get_output(), 0, 0)
loc = opencv.max()
stroke(255, 0, 0)
stroke_weight(4)
no_fill()
ellipse(loc.x, loc.y, 10, 10)