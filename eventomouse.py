import cv2
import numpy as np

swars = cv2.imread('starwars.jpg')

def pegaPixel(event, x, y, flags, param):
    global mx, my
    if event == cv2.EVENT_LBUTTONDOWN:
       print("Posição x = {} e y = {}".format(x, y))
       print("Cor do pixel = {}".format(swars[y,x]))

cv2.imshow('starwars', swars)
cv2.setMouseCallback('starwars', pegaPixel)
cv2.waitKey(0)
cv2.destroyAllWindows()