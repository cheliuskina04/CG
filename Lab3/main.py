# Челюскіна Юлія КМ-21
import math

import imageio
import numpy

X, Y = 960, 960  # size
image = numpy.zeros((Y, X, 3), dtype=numpy.uint8)  # array of pixels

P = 460
q = 10 * (0 + 1)  # кут


with open('DS0.txt') as b:
    for line in b:
        line = line.split(" ")
        x = int(line[0])
        y = int(line[1])
        step1 = numpy.matrix([[1, 0, P],
                              [0, 1, P],
                              [0, 0, 1]])
        step2 = numpy.matrix([[math.cos(q), math.sin(q), 0],
                              [-math.sin(q), math.cos(q), 0],
                              [0, 0, 1]])
        step3 = numpy.matrix([[1, 0, -P],
                              [0, 1, -P],
                              [0, 0, 1]])

        res_matrix = step1 @ step2 @ step3 @ numpy.matrix([[x],[y],[1]])
        image[int(res_matrix.item(0)), int(res_matrix.item(1)), :] = (0x0, 0x0, 0xFF)  # fill the pixels from dataset

imageio.imwrite('result.png', image)  # save result

