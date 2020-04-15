import cv2
import numpy as np
import constant as ct

swars = cv2.imread('starwars.jpg')
img = np.zeros((400,500,1), dtype='uint8')
img[:] = 125

def pegaPixel(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        print("Posição x = {} e y = {}".format(y, x))
        print("Cor do pixel = {}".format(swars[y,x]))
        cv2.circle(swars, (x,y), 10, 255, 1, 8, 0)
        cv2.imshow('imagem', swars)

cv2.imshow('starwars', swars)
cv2.setMouseCallback('starwars', pegaPixel)
cv2.waitKey(0)
cv2.destroyAllWindows()