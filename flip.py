import sys
from PIL import Image

# define your flip function here
def flip(img):
    w, h = img.size
    imgdup = img.copy()
    m = img.load()
    n = imgdup.load()
    for x in range(w):
        for y in range(h):
            n[x, y] = m[w-x-1, y]
    return imgdup.show()


if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

# call your flip function here
flip(img)
