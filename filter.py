import sys
from PIL import Image


def getpixel(img, x, y):
    w, h = img.size
    if x < 0:
        x = 0
    elif x >= w:
        x = w - 1
    if y < 0:
        y = 0
    elif y >= h:
        y = h - 1
    return img.load()[x, y]


def region3x3(img, x, y):
    me = getpixel(img, x, y)
    N = getpixel(img, x, y - 1)
    NE = getpixel(img, x + 1, y - 1)
    E = getpixel(img, x + 1, y)
    SE = getpixel(img, x + 1, y + 1)
    S = getpixel(img, x, y + 1)
    SW = getpixel(img, x - 1, y + 1)
    W = getpixel(img, x - 1, y)
    NW = getpixel(img, x - 1, y - 1)
    return [me, N, NE, E, SE, S, SW, W, NW]

def open(argv):
    if len(argv) <= 1:
        print "missing image filename"
        sys.exit(1)
    img = Image.open(argv[1])
    img = img.convert("L")
    return img


def filter(img, f):
    w, h = img.size
    imgdup = img.copy()
    pixels = imgdup.load()
    for x in range(w):
        for y in range(h):
            r = region3x3(img, x, y)
            pixels[x, y] = f(r)
    return imgdup
