import aux

# Create a dithered version of the image
def convert_dithering(image):
    width, height = image.size

    # Create new Image and a Pixel Map
    new = aux.create_image(width, height)
    pixels = new.load()

    for i in range(0, width, 2):
        for j in range(0, height, 2):
            # Get Pixels
            p1 = aux.get_pixel(image, i, j)
            p2 = aux.get_pixel(image, i, j+1)
            p3 = aux.get_pixel(image, i+1, j)
            p4 = aux.get_pixel(image, i+1, j+1)

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
                r[x] = aux.get_saturation(red, x)
                g[x] = aux.get_saturation(green, x)
                b[x] = aux.get_saturation(blue, x)

            # Set Dithered Colors
            pixels[i, j]       = (r[0], g[0], b[0])
            pixels[i, j+1]     = (r[1], g[1], b[1])
            pixels[i+1, j]     = (r[2], g[2], b[2])
            pixels[i+1, j+1]   = (r[3], g[3], b[3])

    return new
    
# test main
if __name__ == "__main__":
    original = aux.open_image(input())

    new = convert_dithering(original)
    aux.save_image(new, 'dither.png')