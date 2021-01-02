import cv2
import numpy as np

swars = cv2.imread('starwars.jpg')

kernel3x3 = np.ones((3,3), ) / 49
print(kernel3x3)
kernel_sharpening = np.array([[-1,-1,-1], [-1, 9, -1] ,[-1, -1, -1]])

blurred = cv2.blur(swars, (5,5))
sharpened = cv2.filter2D(swars, -1, kernel_sharpening)

cv2.imshow('Normal', swars)
cv2.imshow('Blurred 3x3', blurred)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()