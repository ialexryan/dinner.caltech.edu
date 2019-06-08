from PIL import Image

ORANGE = (255, 102, 0)
WHITE = (255, 255, 255)

def parse_pair(im):
    pix = im.load()
    width, height = im.size

    div_line_bottom = -1
    div_line_left = -1
    div_line_right = -1
    div_line_top = -1

    for y in range(height - 1, -1, -1):
        for x in range((width // 2) - 20, (width // 2) + 20):
            val = pix[x, y]
            if div_line_left == -1 and val == ORANGE:
                div_line_left = x
                div_line_bottom = y
            elif div_line_left != -1 and val != ORANGE:
                div_line_right = x - 1
                break
        if div_line_left != -1:
            break

    div_line_mid = (div_line_left + div_line_right) // 2

    for y in range(div_line_bottom, -1, -1):
        if pix[div_line_mid, y] != ORANGE:
            div_line_top = y + 1
            break

    assert(div_line_bottom != -1)
    assert(div_line_left != -1)
    assert(div_line_right != -1)
    assert(div_line_top != -1)

    left = im.crop((0, div_line_top - 60, div_line_left - 1, div_line_bottom))
    right = im.crop((div_line_right + 1, div_line_top - 60, width, div_line_bottom))
    return left, right

def parse_single(im):
    pix = im.load()
    width, height = im.size

    left_boundary = -1
    right_boundary = -1
    bottom_boundary = -1
    top_boundary = -1

    for x in range(width - 1):
        val1 = pix[x, height // 2]
        val2 = pix[x + 1, height // 2]
        if val1 != WHITE and val2 == WHITE:
            left_boundary = x + 1
            break
    assert(left_boundary != -1)

    for x in range(width - 1, 0, -1):
        val1 = pix[x, height // 2]
        val2 = pix[x - 1, height // 2]
        if val1 != WHITE and val2 == WHITE:
            right_boundary = x - 1
            break
    assert(right_boundary != -1)

    for y in range(height // 2, height):
        if pix[left_boundary - 1, y] == WHITE:
            bottom_boundary = y
            break
    assert(bottom_boundary != -1)

    for y in range(height // 2, -1, -1):
        if pix[left_boundary - 1, y] == WHITE:
            top_boundary = y
            break
    assert(top_boundary != -1)

    return im.crop((left_boundary, top_boundary - 60, right_boundary, bottom_boundary))

def crop_sides(im, margin = 50):
    width, height = im.size
    pix = im.load()

    content_left = -1
    content_right = -1

    for x in range(width):
        if any(pix[x, y] != WHITE for y in range(height)):
            content_left = x
            break
    assert(content_left != -1)

    for x in range(width - 1, -1, -1):
        if any(pix[x, y] != WHITE for y in range(height)):
            content_right = x
            break
    assert(content_right != -1)

    margin = min(margin, content_left, width - content_right)
    return im.crop((content_left - margin, 0, content_right + margin, height))


im1 = Image.open("menu-1.png")
im2 = Image.open("menu-2.png")
im3 = Image.open("menu-3.png")

mon, tues = parse_pair(im1)
wed, thurs = parse_pair(im2)
fri = parse_single(im3)

mon = crop_sides(mon)
tues = crop_sides(tues)
wed = crop_sides(wed)
thurs = crop_sides(thurs)
fri = crop_sides(fri)

mon.save("Monday.png", "PNG")
tues.save("Tuesday.png", "PNG")
wed.save("Wednesday.png", "PNG")
thurs.save("Thursday.png", "PNG")
fri.save("Friday.png", "PNG")
