import numpy as np
import cv2 as cv
import scipy as sc

########################################################################
# Definições
########################################################################
# Imagem utilizada
imagem = cv.imread('ts_480.jpg')
im_h = imagem.shape[0]
im_w = imagem.shape[1]
im_h_meio = np.int(im_h/2)
linha_sup = 0
linha_inf = 0
d = 0

# Canvas para plotagem das imagens
# Dimensões do canvas
canvas = np.zeros((im_h, (2*im_w) + 1, 3), dtype='uint8')
canvas[:, 0:480, :] = imagem
canvas[:, 481:961, :] = 180
cv.namedWindow('Tilt Shift')


#Funções para trackbars
# Ajusta altura da faixa em foco
def ajustaAltura(valor):
    # Calcula a altura das linhas superior e inferior
    global linha_sup, linha_inf

    linha_sup = im_h_meio - valor
    linha_inf = im_h_meio + valor

    # Desenha as linhas na imagem e a atualiza com a posição das mesmas
    cv.line(canvas, (0, linha_sup), (im_w, linha_sup), color=(0,0,255),
            thickness=1, lineType=cv.LINE_AA)
    cv.line(canvas, (0, linha_inf), (im_w, linha_inf), color=(0, 255, 0),
            thickness=1, lineType=cv.LINE_AA)

    cv.imshow("Tilt Shift", canvas)

    canvas[:, 0:480, :] = imagem
    canvas[:, 481:961, :] = 180

    cv.line(canvas, (0, linha_sup), (im_w, linha_sup), color=(0, 0, 255),
            thickness=1, lineType=cv.LINE_AA)
    cv.line(canvas, (0, linha_inf), (im_w, linha_inf), color=(0, 255, 0),
            thickness=1, lineType=cv.LINE_AA)

    cv.imshow("Tilt Shift", canvas)

# Ajusta força do decaimento
def ajustaForca(valor):
    global d
    d = valor

# Ajusta posição vertical do desfoque
def ajustaPosicao(valor):
    global im_h_meio, linha_sup, linha_inf

    im_h_meio = valor
    linha_sup = im_h_meio - valor
    linha_inf = im_h_meio + valor

    # Desloca as linhas em bloco para cima ou para baixo
    if valor <= 180:
        # Desenha as linhas na imagem e a atualiza com a posição das mesmas
        cv.line(canvas, (0, linha_sup-valor), (im_w, linha_sup-valor),
                color=(0, 0, 255), thickness=1, lineType=cv.LINE_AA)
        cv.line(canvas, (0, linha_inf-valor), (im_w, linha_inf-valor),
                color=(0, 255, 0), thickness=1, lineType=cv.LINE_AA)

        cv.imshow("Tilt Shift", canvas)

        canvas[:, 0:480, :] = imagem
        canvas[:, 481:961, :] = 180

        cv.line(canvas, (0, linha_sup-valor), (im_w, linha_sup-valor),
                color=(0, 0, 255), thickness=1, lineType=cv.LINE_AA)
        cv.line(canvas, (0, linha_inf-valor), (im_w, linha_inf-valor),
                color=(0, 255, 0), thickness=1, lineType=cv.LINE_AA)

        cv.imshow("Tilt Shift", canvas)
    else:
        # Desenha as linhas na imagem e a atualiza com a posição das mesmas
        cv.line(canvas, (0, linha_sup+valor), (im_w, linha_sup+valor), color=(0, 0, 255),
                thickness=1, lineType=cv.LINE_AA)
        cv.line(canvas, (0, linha_inf+valor), (im_w, linha_inf+valor), color=(0, 255, 0),
                thickness=1, lineType=cv.LINE_AA)

        cv.imshow("Tilt Shift", canvas)

        canvas[:, 0:480, :] = imagem
        canvas[:, 481:961, :] = 180

        cv.line(canvas, (0, linha_sup+valor), (im_w, linha_sup+valor), color=(0, 0, 255),
                thickness=1, lineType=cv.LINE_AA)
        cv.line(canvas, (0, linha_inf+valor), (im_w, linha_inf+valor), color=(0, 255, 0),
                thickness=1, lineType=cv.LINE_AA)

        cv.imshow("Tilt Shift", canvas)

# Criação dos controles
# Trackbar para tamanho da faixa de foco
cv.createTrackbar("Janela de Foco", "Tilt Shift", 0, im_h_meio, ajustaAltura)

# Trackbar para regular a força do decaimento
cv.createTrackbar("Forca do decaimento(d)", "Tilt Shift", 0, 100, ajustaForca)

# Trackbar para ajustar a posição vertical da janela de foco
cv.createTrackbar("Posicao na Janela", "Tilt Shift", im_h_meio, im_h, ajustaPosicao)

########################################################################
# Programação
########################################################################
print(linha_inf, linha_sup)

cv.imshow('Tilt Shift', canvas)
cv.waitKey(0)