from filter import *
def median(data):
    sorteddata = sorted(data)
    index = len(sorteddata)/2
    return sorteddata[index]

img = open(sys.argv)
img.show()
img = filter(img, median)
img.show()
