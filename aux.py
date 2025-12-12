from PIL import Image

# Open an Image
def open_image(path):
    newImage = Image.open(path)
    return newImage

# Save Image
def save_image(image, path):
    image.save(path, 'png')

# Create a new Image with the given size
def create_image(i, j):
    image = Image.new("RGB", (i, j), "white")
    return image

# get the pixel from the given image
def get_pixel(image, i, j):

    # verify if it is a image bounds
    width, height = image.size
    if i > width or j > height:
        return None
    
    # get Pixel
    pixel = image.getpixel((i, j))
    return pixel

# return color value depending on quadrant and saturation
def get_saturation(value, quadrant):
    if value > 233:
        return 255
    elif value > 159:
        if quadrant != 1:
            return 255
        return 0
    elif value > 95:
        if quadrant == 0 or quadrant == 3:
            return 255
        return 0
    elif value > 32:
        if quadrant == 1:
            return 255
        return 0
    else:
        return 0
