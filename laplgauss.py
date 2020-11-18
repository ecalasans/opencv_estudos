import numpy as np
import cv2 as cv

# Canvas para a imagem
cv.namedWindow("Canvas")
canvas = np.zeros((480, 641, 3), dtype='uint8')

# Imagem de trabalho
eiffel = cv.imread('eiffel.jpg')
im_result = np.zeros((eiffel.shape[0], eiffel.shape[1], 3), dtype='uint8')

# Kernels dos filtros
# Filtro da média
media = np.ones((3,3), dtype=np.float32)/9
# Filtro gaussiano
gauss = np.array([
    [0.0625, 0.125, 0.0625],
    [0.0625, 0.25, 0.0625],
    [0.0625, 0.125, 0.0625],
], dtype=np.float32)
# Filtro detector de bordas horizontais
horizontal = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])
# Filtro detector de bordas verticais
vertical = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
], dtype=np.float32)
# Filtro laplaciano
laplacian = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
], dtype=np.float32)
# Filtro boost
boost = np.array([
    [0, -1, 0],
    [-1, 5.2, -1],
    [0, -1, 0]
], dtype=np.float32)

# Função para os botões
# Variável global que armazena o status do botão de mixagem com o laplaciano
status_mix = 0
# Aplica filtro laplaciano sobre outro filtro já aplicado
def mixLaplaciano(state, param):
    global status_mix
    status_mix = state

# Mantém imagem sem filtro
def imagemNormal(state, param):
    if state == 1:
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = eiffel

        cv.imshow('Canvas', canvas)

# Aplica filtro da média
def aplicaMedia(state, param):
    im_result = cv.filter2D(eiffel, None, media)
    if state == 1:
        if status_mix == 1:
            im_result = cv.filter2D(im_result, None, laplacian)
        else:
            pass
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = im_result

        cv.imshow('Canvas', canvas)
    else:
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = eiffel

        cv.imshow('Canvas', canvas)

# Aplica filtro gaussiano
def aplicaGaussiano(state, param):
    im_result = cv.filter2D(eiffel, None, gauss)
    if state == 1:
        if status_mix == 1:
            im_result = cv.filter2D(im_result, None, laplacian)
        else:
            pass
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = im_result

        cv.imshow('Canvas', canvas)
    else:
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = eiffel

        cv.imshow('Canvas', canvas)
# Aplica filtro detector de bordas horizontais
def aplicaHorizontal(state, param):
    im_result = cv.filter2D(eiffel, None, horizontal)
    if state == 1:
        if status_mix == 1:
            im_result = cv.filter2D(im_result, None, laplacian)
        else:
            pass
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = im_result

        cv.imshow('Canvas', canvas)
    else:
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = eiffel

        cv.imshow('Canvas', canvas)
# Aplica filtro detector de bordas verticais
def aplicaVertical(state, param):
    im_result = cv.filter2D(eiffel, None, vertical)
    if state == 1:
        if status_mix == 1:
            im_result = cv.filter2D(im_result, None, laplacian)
        else:
            pass
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = im_result

        cv.imshow('Canvas', canvas)
    else:
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = eiffel

        cv.imshow('Canvas', canvas)
# Aplica filtro laplaciano
def aplicaLaplaciano(state, param):
    if state == 1:
        im_result = cv.filter2D(eiffel, None, laplacian)
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = im_result

        cv.imshow('Canvas', canvas)
    else:
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = eiffel

        cv.imshow('Canvas', canvas)
# Aplica filtro boost
def aplicaBoost(state, param):
    im_result = cv.filter2D(eiffel, None, boost)
    if state == 1:
        if status_mix == 1:
            im_result = cv.filter2D(im_result, None, laplacian)
        else:
            pass
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = im_result

        cv.imshow('Canvas', canvas)
    else:
        canvas[:, 0:320, :] = eiffel
        canvas[:, 321:641, :] = eiffel

        cv.imshow('Canvas', canvas)

cv.createButton("Normal", imagemNormal, 0, cv.QT_RADIOBOX, 1)
cv.createButton("Media", aplicaMedia, 1, cv.QT_RADIOBOX, 0)
cv.createButton("Gaussiano", aplicaGaussiano, 2, cv.QT_RADIOBOX, 0)
cv.createButton("Horizontal", aplicaHorizontal, 3, cv.QT_RADIOBOX, 0)
cv.createButton("Vertical", aplicaVertical, 4, cv.QT_RADIOBOX, 0)
cv.createButton("Laplaciano", aplicaLaplaciano, 5, cv.QT_RADIOBOX, 0)
cv.createButton("Boost", aplicaBoost, 6, cv.QT_RADIOBOX, 0)
cv.createButton("Mixar com o Laplaciano", mixLaplaciano, 1,
                cv.QT_CHECKBOX, 0)

canvas[:, 0:320, :] = eiffel
canvas[:, 321:641, :] = eiffel

cv.imshow('Canvas', canvas)
cv.waitKey(0)


