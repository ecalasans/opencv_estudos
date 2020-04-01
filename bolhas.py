import cv2
import numpy as np

bolhas = cv2.imread('bolhas.png', cv2.IMREAD_GRAYSCALE)

print(bolhas.shape)

linhas = bolhas.shape[0]
colunas = bolhas.shape[1]

for i in range(linhas):
    bolhas[i, 44] = 150

cv2.imshow('', bolhas)
cv2.waitKey(0)
