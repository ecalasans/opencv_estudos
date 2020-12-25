import cv2
import numpy as np

swars = cv2.imread('starwars.jpg')
M = np.zeros(swars.shape, dtype='uint8')

cv2.rectangle(M, (200,200), (400,400), [255,255,255], -2)

bitAnd= cv2.bitwise_and(swars, M)

cv2.imshow('normal', swars)
cv2.imshow('Retangulo', M)
cv2.imshow('Mask', bitAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()