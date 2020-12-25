import numpy as np
import cv2

swars = cv2.imread('starwars.jpg')

# Converter para HSV
hsv_color = cv2.cvtColor(swars, cv2.COLOR_BGR2HSV)

cv2.imshow('BGR', swars)
cv2.imshow('HSV', hsv_color)

cv2.waitKey(0)