import cv2
import numpy as np
import jupytercv

# Declaração de variáveis utilizadas
buracos = 0
n_bolhas = 0

bolhas = cv2.imread('bolhas2.png', cv2.IMREAD_GRAYSCALE)

linhas = bolhas.shape[0]
colunas = bolhas.shape[1]

cv2.imshow('Original', bolhas)
cv2.waitKey(2000)

# Retirar bolhas das bordas verticais
for l in range(linhas):
    if (bolhas[l, 0] == 255):
        cv2.floodFill(bolhas, None, (0, l), 0)


for l in range(linhas):
    if (bolhas[l, colunas - 1] == 255):
        cv2.floodFill(bolhas, None, (colunas - 1, l), 0)


#Retirar bolhas das bordas horizontais
for c in range(colunas):
    if(bolhas[0, c] == 255):
        cv2.floodFill(bolhas, None, (c, 0), 0)


for c in range(colunas):
    if(bolhas[linhas - 1, c] == 255):
        cv2.floodFill(bolhas, None, (c, linhas - 1), 0)

# Pinta o fundo de outra cor para expor os buracos nas
# bolhas
cv2.floodFill(bolhas, None, (0,0), 80)


# Procurar por bolhas
for l in range(linhas - 1):
    for c in range(colunas - 1):

        # Achou uma bolha
        if((bolhas[l, c] == 255) and (bolhas[l, c - 1] == 80)):
            n_bolhas += 1

            cv2.floodFill(bolhas, None, (c, l), 100)

        if((bolhas[l, c] == 100) and (bolhas[l, c + 1] == 0)):
            buracos += 1
            cv2.floodFill(bolhas, None, (c, l), 80)
            break

cv2.imshow('', bolhas)
cv2.waitKey(0)
cv2.imwrite('resultado.png', bolhas)


print("Temos {} bolhas, {} com buracos.".format(n_bolhas, buracos))