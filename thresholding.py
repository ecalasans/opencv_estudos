import cv2
import numpy as np

swars = cv2.imread('starwars.jpg')
swars_gray = cv2.imread('starwars.jpg', 2)

ret, thres_bin = cv2.threshold(swars_gray, 150, 255, cv2.THRESH_BINARY)
print(type(swars))

masked = cv2.bitwise_and(swars, ret)
cv2.imshow('Normal', swars)
cv2.imshow('Thres binary', thres_bin)
cv2.imshow('Mascara', masked)
cv2.waitKey(0)
cv2.destroyAllWindows()