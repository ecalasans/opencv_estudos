import cv2
import numpy as np

fundo = np.zeros((480, 640, 3), dtype="uint8")

fundo[:] = 255

for y in range(0, fundo.shape[1], 20):
    cv2.line(fundo, (y,0), (y, 100), [123,43, 5], thickness=2)

fundo = np.flipud(fundo)

cv2.imshow('Imagem', fundo)
cv2.waitKey(0)
