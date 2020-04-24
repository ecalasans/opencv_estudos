import cv2
import numpy as np
import constant as ct

swars = cv2.imread('starwars.jpg')

#b, g, r = cv2.split(swars)  #Consome muito tempo - usa (b, g, r)

#Usando numpy [r, g, b] - usa [r, g, b]
vermelho = swars[:,:,2]
verde = swars[:, :, 1]
azul = swars[:,:,0]


canais = [azul, verde, vermelho]

for canal in canais:
    cv2.imshow('imagem', canal)
    cv2.waitKey(0)

#Eliminando um canal
azul[:] = 0

sem_azul = cv2.merge((azul,verde, vermelho)) #usar bgr na reconstrução
print(sem_azul)
cv2.imshow('Sem azul', sem_azul)
cv2.waitKey(0)
