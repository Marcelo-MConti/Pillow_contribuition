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

# Create a dithered version of the image
def convert_dithering(image):
    width, height = image.size

    # Create new Image and a Pixel Map
    new = create_image(width, height)
    pixels = new.load()

    for i in range(0, width, 2):
        for j in range(0, height, 2):
            # Get Pixels
            p1 = get_pixel(image, i, j)
            p2 = get_pixel(image, i, j+1)
            p3 = get_pixel(image, i+1, j)
            p4 = get_pixel(image, i+1, j+1)

            # Color Saturation by RGB channel
            red = (p1[0]+p2[0]+p3[0]+p4[0])/4
            green = (p1[1]+p2[1]+p3[1]+p4[1])/4
            blue = (p1[2]+p2[2]+p3[2]+p4[2])/4

            # Results by channel
            r = [0, 0, 0, 0]
            g = [0, 0, 0, 0]
            b = [0, 0, 0, 0]

            # Get Quadrant Color
            for x in range(0, 4):
                r[x] = get_saturation(red, x)
                g[x] = get_saturation(green, x)
                b[x] = get_saturation(blue, x)

            # Set Dithered Colors
            pixels[i, j]       = (r[0], g[0], b[0])
            pixels[i, j+1]     = (r[1], g[1], b[1])
            pixels[i+1, j]     = (r[2], g[2], b[2])
            pixels[i+1, j+1]   = (r[3], g[3], b[3])

    return new
    
# test main
if __name__ == "__main__":
    original = open_image(input())

    new = convert_dithering(original)
    save_image(new, 'dither.png')