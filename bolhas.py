import cv2
import numpy as np
import jupytercv

# Declaração de variáveis utilizadas

bolhas = cv2.imread('bolhas.png', cv2.IMREAD_GRAYSCALE)

print(bolhas.shape)

linhas = bolhas.shape[0]
colunas = bolhas.shape[1]

jupytercv.imshowGrayscale(bolhas)

# Retirar bolhas das bordas verticais
for l in range(linhas):
    if (bolhas[l, 0] == 255):
        cv2.floodFill(bolhas, None, (0, l), 0)


for l in range(linhas):
    if (bolhas[l, linhas - 1] == 255):
        cv2.floodFill(bolhas, None, (linhas - 1, l), 0)


#Retirar bolhas das bordas horizontais
for c in range(colunas):
    if(bolhas[0, c] == 255):
        cv2.floodFill(bolhas, None, (c, 0), 0)


for c in range(colunas):
    if(bolhas[colunas - 1, c] == 255):
        cv2.floodFill(bolhas, None, (c, colunas - 1), 0)


# Pinta o fundo de outra cor para expor os buracos nas
# bolhas
cv2.floodFill(bolhas, None, (0,0), 150)
jupytercv.imshowGrayscale(bolhas)

#