import numpy as np
import cv2 as cv

# Canvas para a imagem
cv.namedWindow("Canvas")
canvas = np.zeros((480, 641, 3), dtype='uint8')

# Imagem de trabalho
eiffel = cv.imread('eiffel.jpg', cv.COLOR_BGR2GRAY)

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
def selRadioButton(state, vazio):
    pass

# Aplica filtro da média
def aplicaMedia():
    im_result = cv.filter2D(eiffel, None, media, eiffel)
    return im_result

canvas[:, 0:320, :] = eiffel
canvas[:, 321:641, :] = eiffel


cv.createButton("Media", selRadioButton, None, cv.QT_RADIOBOX, 0)
cv.createButton("Mediana", selRadioButton, None, cv.QT_RADIOBOX, 0)
cv.createButton("Gaussiano", selRadioButton, None, cv.QT_RADIOBOX, 0)
cv.createButton("Horizontal", selRadioButton, None, cv.QT_RADIOBOX, 0)
cv.createButton("Vertical", selRadioButton, None, cv.QT_RADIOBOX, 0)
cv.createButton("Laplaciano", selRadioButton, None, cv.QT_RADIOBOX, 0)
cv.createButton("Boost", selRadioButton, None, cv.QT_RADIOBOX, 0)
cv.createButton("Mixar com o Laplaciano", selRadioButton, None, cv.QT_CHECKBOX, 0)

cv.imshow('Canvas', canvas)
cv.waitKey(0)


