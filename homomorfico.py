import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def gaussModif(gama_L, gama_H, c, D_0, imagem):
    # Variáveis de interesse
    im_h = imagem.shape[0]
    im_w = imagem.shape[1]

    # Coordenadas do centro
    u_c = im_h/2
    v_c = im_w/2

    H = np.zeros(imagem.shape, dtype='float')

    # Matriz de coordenadas
    u, v = np.meshgrid(range(im_h), range(im_w), indexing='ij')

    # Etapas de cálculo do filtro gaussiano modificado
    D_uv_2 = (((u-u_c)**2 + (v-v_c)**2)**2).astype('float')
    div_D0 = D_uv_2/(D_0**2)
    c_div_D0 = -c * div_D0
    exp_div_D0 = np.exp(c_div_D0)
    um_menos_exp = 1 - exp_div_D0
    mult_delta_gama = (gama_H - gama_L) * um_menos_exp
    H = gama_L + mult_delta_gama

    return H


def zeroPadding(imagem):
    cinza_h2 = cv.getOptimalDFTSize(imagem.shape[0])
    cinza_w2 = cv.getOptimalDFTSize(imagem.shape[1])
    print("x = {} -> {}, y = {} -> {}".format(imagem.shape[0], cinza_h2, imagem.shape[1], cinza_w2))
    imagem_padded = np.zeros((cinza_h2, cinza_w2), dtype='uint8')
    imagem_padded[0:cinza_h, 0:cinza_w] = imagem
    return imagem_padded

original = cv.imread('imagens/rxt.jpg')

cinza = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cinza_h = cinza.shape[0]
cinza_w = cinza.shape[1]

#  Zero padding para otimizar a DFT
cinza_padded = zeroPadding(cinza)


########################################################################
# Programação
########################################################################

H_uv = gaussModif(
    gama_L=0.4, gama_H=3.0, c=5, D_0=20, imagem=cinza_padded
)

cv.imshow("H_uv", H_uv)
cv.waitKey(0)
