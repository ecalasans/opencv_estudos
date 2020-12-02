import cv2 as cv
import numpy as np

lion = cv.imread('imagens/lion.jpg')
canny = np.zeros(lion.shape, dtype='uint8')
cv.namedWindow('Canny')


def limite(valor):
    canny = cv.Canny(lion, threshold1=valor, threshold2=3*valor)
    cv.imshow('Canny', canny)

cv.createTrackbar('T1', 'Canny', 0, 300, limite)
cv.imshow('Lion', lion)
cv.imshow('Canny', canny)
cv.waitKey(0)
cv.destroyAllWindows()