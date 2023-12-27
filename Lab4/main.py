# Челюскіна Юлія КМ-21
import math

import imageio
import numpy

X, Y = 960, 540  # size
image = numpy.zeros((Y, X, 3), dtype=numpy.uint8)  # array of pixels

with open('DS0_affine.txt') as b:
    for line in b:
        line = line.split(" ")

        z = -500
        T = numpy.matrix([[540], [960], [z], [1]])
        Z = 100
        x = int(line[0])
        y = int(line[1])
        step1 = numpy.matrix([[1, 0, 0, 0],
                              [0, 1, 0, 0],
                              [0, 0, -1, 0],
                              [0, 0, 0, 1]])
        step2 = numpy.matrix([[1, 0, 0, 0],
                              [0, 1, 0, 0],
                              [0, 0, 1, 1/Z],
                              [0, 0, 0, 0]])

        res_matrix = numpy.matrix([[x, y, z, 1]]) @ step1  @ step2
        image[int(res_matrix.item(0)/res_matrix.item(3)), int(res_matrix.item(1)/res_matrix.item(3)), :] = (0x0, 0x0, 0xFF)  # fill the pixels from dataset

imageio.imwrite('result.png', image)  # save result
