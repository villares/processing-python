"""
 * Edge Detection.
 *
 * Exposing areas of contrast within an image
 * by processing it through a high-pass filter.
"""
kernel = ((-1, -1, -1),
          (-1,  9, -1),
          (-1, -1, -1))

size(200, 200)
img = load_image("house.jpg")  # Load the original image
image(img, 0, 0)             # Displays the image from point (0,0)
img.load_pixels()
# Create an opaque image of the same size as the original
edge_img = create_image(img.width, img.height, RGB)
# Loop through every pixel in the image.
for y in range(1, img.height-1):  # Skip top and bottom edges
    for x in range(1, img.width-1):  # Skip left and right edges
        sum = 0  # Kernel sum for this pixel
        for ky in (-1, 0, 1):
            for kx in (-1, 0, 1):
                # Calculate the adjacent pixel for this kernel point
                pos = (y + ky)*img.width + (x + kx)
                # Image is grayscale, red/green/blue are identical
                val = red(img.pixels[pos])
                # Multiply adjacent pixels based on the kernel values
                sum += kernel[ky+1][kx+1] * val
        # For this pixel in the new image, set the gray value
        # based on the sum from the kernel
        edge_img.pixels[y*img.width + x] = color(sum)

# State that there are changes to edgeImg.pixels[]
edge_img.update_pixels()
image(edge_img, 100, 0)  # Draw the new image
