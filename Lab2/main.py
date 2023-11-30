# Челюскіна Юлія КМ-21
import imageio
import numpy

X, Y = 960, 540  # size
image = numpy.zeros((Y, X, 3), dtype=numpy.uint8)  # array of pixels

with open('DS0.txt') as b:
    for line in b:
        line = line.split(" ")
        image[int(line[0]), int(line[1]), :] = (0xFF, 0xFF, 0xFF)   # fill the pixels from dataset

imageio.imwrite('result.png', image)   # save result
