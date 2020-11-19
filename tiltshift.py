import numpy as np
import cv2 as cv
import scipy as sc

########################################################################
# Definições
########################################################################
# Imagem utilizada
imagem = cv.imread('ts_480.jpg')

# Filtro da média
media = np.ones((5,5), dtype=np.float32)/25

# Imagem após aplicação do filtro da média
imagem_media = cv.filter2D(imagem, None, media)

# Dimensões da imagem
im_h = imagem.shape[0]
im_w = imagem.shape[1]
im_h_meio = np.int(im_h/2)    # Ponto médio do eixo x

# Inicialização de variáveis de interesse
pivo = im_h_meio   #  Ponto médio entre as linhas
linha_sup = 0   # Limite superior da região de foco
linha_inf = 0   # Limite inferior da região de foco
d = 0   # Força do decaimento

# Canvas para plotagem das imagens
# Dimensões do canvas
canvas = np.zeros((im_h, (2*im_w) + 1, 3), dtype='uint8')
canvas[:, 0:480, :] = imagem
canvas[:, 481:961, :] = imagem_media
cv.namedWindow('Tilt Shift')

# Função de ponderação(calcula alfa e 1-alfa)
def alfa(ls, li, d):
    x = np.zeros((im_h, im_w, 3), dtype=np.float)

    uns = np.ones((im_h, im_w, 3), dtype=np.float)
    alfa = (np.tanh((x-ls)/d) - np.tanh((x-li)/d))*0.5
    um_menos_alfa = np.subtract(uns, alfa)
    return alfa, um_menos_alfa

#Funções para trackbars
# Ajusta altura da faixa em foco
def ajustaAltura(valor):
    # Calcula a altura das linhas superior e inferior
    global linha_sup, linha_inf, pivo
    pivo = cv.getTrackbarPos('Posicao na Janela', 'Tilt Shift')
    linha_sup = pivo - valor
    linha_inf = pivo + valor

    # Desenha as linhas na imagem e a atualiza com a posição das mesmas
    cv.line(canvas, (0, linha_sup), (im_w, linha_sup), color=(0,0,255),
            thickness=1, lineType=cv.LINE_AA)
    cv.line(canvas, (0, linha_inf), (im_w, linha_inf), color=(0, 255, 0),
            thickness=1, lineType=cv.LINE_AA)

    cv.imshow("Tilt Shift", canvas)

    canvas[:, 0:480, :] = imagem

    if d == 0:
        canvas[:, 481:961, :] = imagem_media
    else:
        efeito = tiltShift(linha_sup, linha_inf, d)
        canvas[:, 481:961, :] = efeito

    cv.line(canvas, (0, linha_sup), (im_w, linha_sup), color=(0, 0, 255),
            thickness=1, lineType=cv.LINE_AA)
    cv.line(canvas, (0, linha_inf), (im_w, linha_inf), color=(0, 255, 0),
            thickness=1, lineType=cv.LINE_AA)

    cv.imshow("Tilt Shift", canvas)
    pivo = cv.getTrackbarPos('Posicao na Janela', 'Tilt Shift')

# Ajusta força do decaimento
def ajustaForca(valor):
    global d
    d = valor

    if d == 0:
        canvas[:, 481:961, :] = imagem_media
    else:
        efeito = tiltShift(linha_sup, linha_inf, d)
        canvas[:, 481:961, :] = efeito
    cv.imshow("Tilt Shift", canvas)

# Ajusta posição vertical do desfoque
def ajustaPosicao(valor):
    global linha_sup, linha_inf
    pivo = np.int((linha_sup + linha_inf)/2)
    # Desloca as linhas em bloco para cima ou para baixo
    if valor < pivo:
        # Desloca o bloco
        linha_sup = linha_sup - 1
        linha_inf = linha_inf - 1

        # Desenha as linhas na imagem e a atualiza com a posição das mesmas
        cv.line(canvas, (0, linha_sup), (im_w, linha_sup),
                color=(0, 0, 255), thickness=1, lineType=cv.LINE_AA)
        cv.line(canvas, (0, linha_inf), (im_w, linha_inf),
                color=(0, 255, 0), thickness=1, lineType=cv.LINE_AA)

        cv.imshow("Tilt Shift", canvas)

        canvas[:, 0:480, :] = imagem
        if d == 0:
            canvas[:, 481:961, :] = imagem_media
        else:
            efeito = tiltShift(linha_sup, linha_inf, d)
            canvas[:, 481:961, :] = efeito

        cv.line(canvas, (0, linha_sup), (im_w, linha_sup),
                color=(0, 0, 255), thickness=1, lineType=cv.LINE_AA)
        cv.line(canvas, (0, linha_inf), (im_w, linha_inf),
                color=(0, 255, 0), thickness=1, lineType=cv.LINE_AA)

        cv.imshow("Tilt Shift", canvas)

    else:
        # Desloca o bloco
        linha_sup = linha_sup + 1
        linha_inf = linha_inf + 1

        # Desenha as linhas na imagem e a atualiza com a posição das mesmas
        cv.line(canvas, (0, linha_sup), (im_w, linha_sup), color=(0, 0, 255),
                thickness=1, lineType=cv.LINE_AA)
        cv.line(canvas, (0, linha_inf), (im_w, linha_inf), color=(0, 255, 0),
                thickness=1, lineType=cv.LINE_AA)

        cv.imshow("Tilt Shift", canvas)

        canvas[:, 0:480, :] = imagem
        if d == 0:
            canvas[:, 481:961, :] = imagem_media
        else:
            efeito = tiltShift(linha_sup, linha_inf, d)
            canvas[:, 481:961, :] = efeito

        cv.line(canvas, (0, linha_sup), (im_w, linha_sup), color=(0, 0, 255),
                thickness=1, lineType=cv.LINE_AA)
        cv.line(canvas, (0, linha_inf), (im_w, linha_inf), color=(0, 255, 0),
                thickness=1, lineType=cv.LINE_AA)

        cv.imshow("Tilt Shift", canvas)

# Função para produção do tilt shift e plotagem no canvas
def tiltShift(ls, li, d):
    a, um_menos_a = alfa(ls, li, d)

    im_1 = np.multiply(a, imagem)
    im_2 = np.multiply(um_menos_a, imagem_media)

    return im_1 + im_2


# Criação dos controles
# Trackbar para tamanho da faixa de foco
cv.createTrackbar("Janela de Foco", "Tilt Shift", 0, im_h_meio, ajustaAltura)

# Trackbar para regular a força do decaimento
cv.createTrackbar("Forca do decaimento(d)", "Tilt Shift", 0, 10, ajustaForca)

# Trackbar para ajustar a posição vertical da janela de foco
cv.createTrackbar("Posicao na Janela", "Tilt Shift", 180, im_h, ajustaPosicao)

########################################################################
# Programação
########################################################################
cv.imshow('Tilt Shift', canvas)
cv.waitKey(0)