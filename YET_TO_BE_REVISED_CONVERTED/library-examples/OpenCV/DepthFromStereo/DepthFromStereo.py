from org.opencv.calib3d import StereoBM, StereoSGBM
add_library('opencv_processing')


img_l = load_image("scene_l.jpg")
img_r = load_image("scene_r.jpg")
ocv_l = OpenCV(this, img_l)
ocv_r = OpenCV(this, img_r)
size(ocv_l.width * 2, ocv_l.height * 2)
ocv_l.gray()
ocv_r.gray()
left = ocv_l.get_gray()
right = ocv_r.get_gray()
disparity = OpenCV.imitate(left)
stereo = StereoSGBM(0, 32, 3, 128, 256, 20, 16, 1, 100, 20, True)
stereo.compute(left, right, disparity)
depth_mat = OpenCV.imitate(left)
disparity.convert_to(depth_mat, depth_mat.type())
depth1 = create_image(depth_mat.width(), depth_mat.height(), RGB)
ocv_l.to_p_image(depth_mat, depth1)
stereo2 = StereoBM()
stereo2.compute(left, right, disparity)
disparity.convert_to(depth_mat, depth_mat.type())
depth2 = create_image(depth_mat.width(), depth_mat.height(), RGB)
ocv_l.to_p_image(depth_mat, depth2)

image(img_l, 0, 0)
image(img_r, img_l.width, 0)
image(depth1, 0, img_l.height)
image(depth2, img_l.width, img_l.height)
fill(255, 0, 0)
text("left", 10, 20)
text("right", 10 + img_l.width, 20)
text("stereo SGBM", 10, img_l.height + 20)
text("stereo BM", 10 + img_l.width, img_l.height + 20)
