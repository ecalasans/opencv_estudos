import cv2
import numpy as np

tela = np.zeros((480, 1280), dtype='uint8')
tela[:, 0:640] = 0
tela[:, 640:1280] = 255

imagem = cv2.imread('imagens/eric.jpg')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
#print(cinza)

hist_orig, bins = np.histogram(cinza, bins=256)
hist_dens, bins2 = np.histogram(cinza, bins=256, density=True)
#print(hist_orig)
#print(np.round(hist_dens, 4))

acum = np.cumsum(hist_dens)
#print(np.round(acum, 2))

s_k = np.round(255*acum, 0)

s_k = np.clip(s_k, 0, 255).astype('uint8')

#print(s_k)

cinza2 = s_k[cinza]
print(cinza[0,0])
print(cinza2[0,0])

cv2.imshow('Normal', cinza)
cv2.imshow('Equalizada', cinza2)
cv2.imshow('Tela', tela)
cv2.waitKey(0)
cv2.destroyAllWindows()