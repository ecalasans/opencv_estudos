import cv2
import numpy as np

swars = cv2.imread('starwars.jpg')

###   Blurring   ###
#  Aplicando kernel próprio
#bk = np.ones((5,5), np.float32)/25
#img = cv2.filter2D(swars, -1, bk)

#  Aplicando funções nativas
#img_b = cv2.blur(swars, (10,10))
#cv2.imshow('blur', img_b)

#  Gaussian blur
#img_g = cv2.GaussianBlur(swars, (9,9), 0)
#cv2.imshow('blur', img_g)

#  Median blur
#img_med = cv2.medianBlur(swars, 25)
#cv2.imshow('blur', img_med)

#  Bilateral blur
#img_bil = cv2.bilateralFilter(swars, 5, 150, 150)
cv2.imshow('normal', swars)
#cv2.imshow('blur', img_bil)



### Sharpening  ###
# Unsharp masking - uma versão smoothed é subtraída da imagem original
# smoothed = cv2.GaussianBlur(swars, (9,9), 10)
# unsharped = cv2.addWeighted(swars, 1.5, smoothed, -0.5, 0)
#
# cv2.imshow('smoothed', smoothed)
# cv2.imshow('unsharped', unsharped)

### Aplicando filtros nativos ###
filtro = np.array([[0.0, 1.0, 0.0], [1.0, 2.0, 1.0], [0.0, 1.0, 0.0]]) / 40
aplicada = cv2.filter2D(swars, -1, filtro)

cv2.imshow('filtro', aplicada)

cv2.waitKey(0)
