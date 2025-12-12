from PIL import Image, ImageFilter
def sepia(img):
    width, height = img.size
    gray_img = Image.new("RGB",(width,height))
    pixels = img.load()

    for w in range(width):
        for h in range(height):
            r,g,b = pixels[w,h]

            sepia_r = 0.393*r + 0.769*g + 0.189*b
            sepia_g = 0.349*r + 0.686*g + 0.168*b
            sepia_b = 0.272*r + 0.534*g + 0.131*b
            gray_img.putpixel((w,h),(int(sepia_r),int(sepia_g),int(sepia_b)))
    
    return gray_img