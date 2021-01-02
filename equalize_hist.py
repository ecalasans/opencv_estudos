import numpy as np
import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('starwars.jpg')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
gray_hist, b1 = np.histogram(cinza, bins=256, density=True)

gray_eq = cv2.equalizeHist(cinza)
gray_eq_hist, bins = np.histogram(gray_eq, bins=256, density=True)

pontos = range(0,256)

plt.bar(pontos, gray_eq_hist)
plt.bar(pontos, gray_hist, color='r', alpha=0.5)
plt.show()


# cv2.imshow('Normal', cinza)
# cv2.imshow('Cinza equalizado', gray_eq)
# cv2.waitKey(0)
# cv2.destroyAllWindows()