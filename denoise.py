import sys
from PIL import Image
def median(data):
    sorteddata = sorted(data)
    index = len(sorteddata)/2
    return sorteddata[index]

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

# define your flip function here
def denoise(img):
    w, h = img.size
    imgdup = img.copy()
    m = img.load()
    pixels = imgdup.load()
    imgdup.show()
    for x in range(w):
        for y in range(h):
            r = region3x3(img, x, y)
            pixels[x,y] = median(r)
    return imgdup.show()

if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

# call your flip function here
denoise(img)