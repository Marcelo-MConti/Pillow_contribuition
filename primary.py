import aux

def convert_primay(image):
    # get size
    width, height = image.size

    # create new Image and a Pixel Map
    new = aux.create_image(width, height)
    pixels = new.load()

    # Transform to primary
    for i in range(width):
        for j in range(height):

            # Get Pixel
            pixel = aux.get_pixel(image, i, j)

            # Get R, G, B values 
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2] 

            # Transform to primary
            if red > 127:
                red = 255
            else:
                red = 0
            if green > 127:
                green = 255
            else:
                green = 0
            if blue > 127:
                blue = 255
            else:
                blue = 0

            # Set Pixel in new Image
            pixels[i, j] = (int(red), int(green), int(blue))

    return new
