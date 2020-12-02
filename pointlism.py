import cv2 as cv
import numpy as np

lion = cv.imread('imagens/lion.jpg')

h = [x for x in lion.shape[0]]
w = [y for y in lion.shape[1]]

middle_h = np.int(h/2)
middle_w = np.int(w/2)

canvas = np.ones(lion.shape, dtype='uint8')*255







