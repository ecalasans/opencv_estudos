import cv2 as cv
import numpy as np
import random as rd
import time

rd.seed(np.int(time.time()))

RAIO = 5

img = cv.imread('imagens/lion.jpg')
canvas = cv.imread('imagens/lion.jpg')
canny_img = np.zeros(img.shape, dtype='uint8')
cv.namedWindow('Canny')

def pointlismImage(imagem, canvas, raio, precisao):
    # Vetores de coordenadas da imagem
    h = [x for x in range(imagem.shape[0])]
    w = [y for y in range(imagem.shape[1])]

    # Quantidade de círculos que farão parte da imagem pontilhista
    sample_count = np.int((imagem.shape[0] * imagem.shape[1])/precisao)

    for i in range(sample_count):
        # Faz a amostragem aleatória de coordenadas da imagem
        x = rd.sample(h, 1)[0]
        y = rd.sample(w, 1)[0]

        # Captura a informação de cor da imagem original
        b, g, r = img[x, y, :]
        cor = (int(b), int(g), int(r))

        # Desenha o círculo no container
        cv.circle(canvas, (y,x), raio, cor, thickness=-1, lineType=cv.LINE_AA)

    return canvas

def cannyThreshold(valor):
    # Variáveis globais
    global pointled
    global canny_img

    # Faz a detecção das bordas da imagem
    canny_img = cv.Canny(img, valor, 3 * valor)
    cv.imshow('Canny', canny_img)

    # Desenha um círculo de raio proporcional ao limite inferior(T1) do parâmetro
    # do algoritimo de Canny em uma localização nas proximidades do pixel de borda
    # detectado
    for x in range(canny_img.shape[0]):
        for y in range(canny_img.shape[1]):
            if canny_img[x,y] == 255:
                b, g, r = img[x, y, :]
                cor = (int(b), int(g), int(r))
                # Deslocamento aleatório
                desl = rd.sample([-2,-1,1,2], 1)[0]
                # Raio proporcional a T1
                raio = np.int(RAIO/(valor+1))
                cv.circle(canvas, (y+desl, x+desl), raio, cor,
                          thickness=-1, lineType=cv.LINE_AA)

    cv.imshow('Points', pointled)

pointled = pointlismImage(img,canvas,RAIO,50)

cv.createTrackbar('T1', 'Canny', 1, 100, cannyThreshold)

cv.imshow('Points', pointled)
cv.imshow('Canny', canny_img)
cv.waitKey(0)
cv.destroyAllWindows()








