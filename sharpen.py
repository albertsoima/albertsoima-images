from filter import *
def laplace(data):
    return data[1] + data[3] + data[5] + data[7] - 4*data[0]

def minus(A, B):
    w, h = A.size
    imgdup = A.copy()
    pixels = imgdup.load()
    A1 = A.load()
    B2 = B.load()
    for x in range(w):
        for y in range(h):
            pixels[x, y] = A1[x,y] - B2[x,y]
    return imgdup

img = open(sys.argv)
img.show()
edges = filter(img, laplace)
sharpen = minus(img, edges)
sharpen.show()