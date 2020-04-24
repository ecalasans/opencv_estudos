import cv2
import numpy as np

swars = cv2.imread('starwars.jpg')

#Blurring
#  Aplicando kernel próprio
#bk = np.ones((5,5), np.float32)/25
#img = cv2.filter2D(swars, -1, bk)

#  Aplicando funções nativas
img_b = cv2.blur(swars, (10,10))

cv2.imshow('blur', img)
cv2.waitKey(0)