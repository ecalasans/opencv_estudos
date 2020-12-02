import cv2 as cv
import numpy as np
import random as rd
import time

rd.seed(np.int(time.time()))
RAIO = 3

lion = cv.imread('imagens/lion.jpg')
canvas = np.ones((lion.shape[0], lion.shape[1], 3), dtype='uint8') * 255

def pointlismImage(imagem, canvas, raio, precisao):
    h = [x for x in range(imagem.shape[0])]
    w = [y for y in range(imagem.shape[1])]

    sample_count = np.int((imagem.shape[0] * imagem.shape[1])/precisao)

    for i in range(sample_count):
        x = rd.sample(h, 1)[0]
        y = rd.sample(w, 1)[0]
        b, g, r = lion[x, y, :]
        cor = (int(b), int(g), int(r))
        # canvas[x, y, :] = lion[x, y, :]
        cv.circle(canvas, (y,x), raio, cor, thickness=-1, lineType=cv.LINE_AA)

    return canvas

pointled = pointlismImage(lion,canvas,RAIO,10)
cv.imshow('Points', pointled)

cv.waitKey(0)
cv.destroyAllWindows()








