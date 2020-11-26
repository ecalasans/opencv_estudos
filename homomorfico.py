import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import cmath

def gaussModif(gama_L, gama_H, c, D_0, imagem):
    # Variáveis de interesse
    im_h = imagem.shape[0]
    im_w = imagem.shape[1]

    # Coordenadas do centro
    u_c = im_h/2
    v_c = im_w/2

    H = np.zeros(imagem.shape, dtype='float')
    temp = np.zeros(imagem.shape, dtype='complex')

    # Matriz de coordenadas
    u, v = np.meshgrid(range(im_h), range(im_w), indexing='ij')

    # Etapas de cálculo do filtro gaussiano modificado
    D_uv_2 = (((u-u_c)**2 + (v-v_c)**2)**2).astype('float')
    div_D0 = D_uv_2/(D_0**2)
    c_div_D0 = (-1)* c * div_D0
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

def plotaFFT(imagem):
    I_fft = np.fft.fft2(imagem)
    I_shift = np.fft.fftshift(I_fft)
    I_mag = np.abs(I_shift)
    I_log = np.log(1+ I_mag)
    I_int = np.uint8(I_log)
    I_norm = cv.normalize(I_int, None, 0, 255, norm_type=cv.NORM_MINMAX)
    cv.imshow("TF", I_norm)

original = cv.imread('imagens/rxt.jpg')

cinza = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cinza_h = cinza.shape[0]
cinza_w = cinza.shape[1]

########################################################################
# Programação
########################################################################

#  Zero padding para otimizar a DFT
cinza_padded = zeroPadding(cinza)
plotaFFT(cinza_padded)

# Constrói o filtro
H_uv = gaussModif(
    gama_L= 0.9, gama_H=5, c=3, D_0=1000, imagem=cinza_padded
)
h = np.fft.fftshift(H_uv)
cv.imshow("Filtro", H_uv)

# Imagem no domínio logarítmico
I_log = np.log(1 + cinza_padded)

# DFT
I_fft = np.fft.fft2(I_log)

# Shift
I_shifted = np.fft.fftshift(I_fft)
# I_mag = np.abs(I_shifted)
# I_int = np.uint8(I_mag)
# I_norm = cv.normalize(I_int, None, 0, 255, cv.NORM_MINMAX)
# cv.imshow("TF imagem Log", I_norm)

# Filtragem
I_filt = h * I_fft

#  ITF
I_inv_TF = np.fft.ifft2(I_filt)

# Exponencial
I_exp = np.exp(np.real(I_inv_TF)) - 1

# Converte para uint8
I_int = np.uint8(I_exp)


# Normal e filtrada
cv.imshow("Normal", cinza_padded)
cv.imshow("Filtrada", I_int)
cv.waitKey(0)
cv.destroyAllWindows()

