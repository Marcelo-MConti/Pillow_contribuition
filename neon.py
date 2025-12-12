from PIL import Image, ImageFilter
import math
def sobel_edge_detection(img):
    gray = img.convert("L")

    # Kernels for sobel edge detection
    Kx = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]

    Ky = [ [1,  2,  1],
           [0,  0,  0],
          [-1, -2, -1]]

    width, height = gray.size
    gray_pixels = gray.load()# Access for original gray image pixels

    edge_img = Image.new("L", (width, height))
    edge_pixels = edge_img.load() #Access for the edge pixels

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # Main loop for applying the convolution for all pixels except the borders
            gx = 0
            gy = 0

            # aplicar kernels
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    # Calculating the convolution for a specific pixel(x,y) 
                    value = gray_pixels[x + dx, y + dy]

                    kx = dx +1
                    ky = dy+1

                    gx += value * Kx[kx][ky]
                    gy += value * Ky[kx][ky]

            g = int(min(255, math.sqrt(gx * gx + gy * gy))) # Check if de convolution excceds 255
            edge_pixels[x, y] = g # Applying the result to de edge_img pixel

    return edge_img


# -----------------------------------------------------------
# 2. Aplicar Screen Blend
# -----------------------------------------------------------
def screen(a, b):
    return 255 - (255 - a) * (255 - b) // 255


def glow_image(edge_img):
    width, height = edge_img.size
    edge_pixels = edge_img.load()

    glow_effect = Image.new("L", (width, height))
    glow_pixels = glow_effect.load()

    for y in range(height):
        for x in range(width):
            val = edge_pixels[x, y]
            
            glow_pixels[x, y] = screen(val, val)

    return glow_effect


# -----------------------------------------------------------
# 3. Colorização Neon
# -----------------------------------------------------------
def neon_colorize(glow,color):
    width, height = glow.size
    glow_pixels = glow.load()

    neon_img = Image.new("RGB", (width, height))
    neon_pixels = neon_img.load()

    for y in range(height):
        for x in range(width):
            value = glow_pixels[x, y]

            r = int(value * color[0]/255)
            g = int(value * color[1]/255)
            b = int(value * color[2]/255)
            
            r = min(255,r)
            g = min(255,g)
            b = min(255, b)

            neon_pixels[x, y] = (r, g, b)

    return neon_img


# -----------------------------------------------------------
# 4. Combinar com a imagem original
# -----------------------------------------------------------
def blend(img, neon, alpha=0.55):
    if alpha>1:
        alpha = 1

    width, height = img.size
    img_pixels = img.load()
    neon_pixels = neon.load()

    result = Image.new("RGB", (width, height))
    result_pixels = result.load()

    for y in range(height):
        for x in range(width):
            r1, g1, b1 = img_pixels[x, y]
            r2, g2, b2 = neon_pixels[x, y]

            r = int((1 - alpha) * r1 + alpha * r2)
            g = int((1 - alpha) * g1 + alpha * g2)
            b = int((1 - alpha) * b1 + alpha * b2)

            result_pixels[x, y] = (r, g, b)

    return result


# -----------------------------------------------------------
# 5. Função principal
# -----------------------------------------------------------
def neon_glow(img,color = (128,0,255),alpha = 0.30):
    edges = sobel_edge_detection(img)

    # SUAVIZAÇÃO DAS BORDAS (principal)
    edges = edges.filter(ImageFilter.GaussianBlur(2))

    glow = glow_image(edges)

    neon = neon_colorize(glow,color)

    # SUAVIZAÇÃO NA MISTURA FINAL
    result = blend(img, neon, alpha)

    return result