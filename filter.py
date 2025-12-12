from PIL import Image


def _get_saturation(value, quadrant):
    if value > 233:
        return 255
    if value > 159:
        return 255 if quadrant != 1 else 0
    if value > 95:
        return 255 if quadrant in (0, 3) else 0
    if value > 32:
        return 255 if quadrant == 1 else 0
    return 0


def _convert_primary(image):
    image = image.convert("RGB")
    width, height = image.size

    src = image.load()
    out = Image.new("RGB", (width, height))
    dst = out.load()

    for x in range(width):
        for y in range(height):
            r, g, b = src[x, y]
            dst[x, y] = (
                255 if r > 127 else 0,
                255 if g > 127 else 0,
                255 if b > 127 else 0,
            )

    return out


def _convert_dithering(image):
    image = image.convert("RGB")
    width, height = image.size

    src = image.load()
    out = Image.new("RGB", (width, height))
    dst = out.load()

    for x in range(0, width - 1, 2):
        for y in range(0, height - 1, 2):
            p1 = src[x, y]
            p2 = src[x, y + 1]
            p3 = src[x + 1, y]
            p4 = src[x + 1, y + 1]

            red = (p1[0] + p2[0] + p3[0] + p4[0]) / 4
            green = (p1[1] + p2[1] + p3[1] + p3[1]) / 4
            blue = (p1[2] + p2[2] + p3[2] + p4[2]) / 4

            r = [_get_saturation(red, q) for q in range(4)]
            g = [_get_saturation(green, q) for q in range(4)]
            b = [_get_saturation(blue, q) for q in range(4)]

            dst[x, y] = (r[0], g[0], b[0])
            dst[x, y + 1] = (r[1], g[1], b[1])
            dst[x + 1, y] = (r[2], g[2], b[2])
            dst[x + 1, y + 1] = (r[3], g[3], b[3])

    return out


def filter_composition(image):
    """
    Apply a primary color reduction followed by ordered dithering.
    """
    image = image.convert("RGB")
    image = _convert_primary(image)
    image = _convert_dithering(image)
    return image
