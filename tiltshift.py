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
    linha_sup = im_h_meio - valor
    linha_inf = im_h_meio + valor

    # Desenha as linhas na imagem
    cv.line(canvas, (0, linha_sup), (im_w, linha_sup), color=(0,0,255),
            thickness=1, lineType=cv.LINE_AA)

    # Atualiza a imagem
    cv.imshow("Tilt Shift", canvas)
    canvas[:, 0:480, :] = imagem
    canvas[:, 481:961, :] = 180
    cv.line(canvas, (0, linha_sup), (im_w, linha_sup), color=(0, 0, 255),
            thickness=1, lineType=cv.LINE_AA)
    cv.imshow("Tilt Shift", canvas)

# Ajusta força do decaimento
def ajustaForca(valor):
    pass
# Ajusta posição vertical do desfoque
def ajustaPosicao(valor):
    pass

# Criação dos controles
# Trackbar para tamanho da faixa de foco
cv.createTrackbar("Janela de Foco", "Tilt Shift", 0, im_h_meio, ajustaAltura)

# Trackbar para regular a força do decaimento
cv.createTrackbar("Forca do decaimento(d)", "Tilt Shift", 0, 100, ajustaForca)

# Trackbar para ajustar a posição vertical da janela de foco
cv.createTrackbar("Posição da Janela", "Tilt Shift", 0, im_h_meio, ajustaPosicao)

########################################################################
# Programação
########################################################################


cv.imshow('Tilt Shift', canvas)
cv.waitKey(0)