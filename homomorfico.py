import cv2 as cv
import numpy as np

########################################################################
# Definições
########################################################################
# Imagem de trabalho
original = cv.imread('imagens/rxt.jpg')

cinza = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cinza_h = cinza.shape[0]
cinza_w = cinza.shape[1]

# Janela para menu de controles
menu = np.zeros((1, 200), dtype='uint8')
menu[:] = 255
cv.namedWindow("Menu")

########################################################################
# Funções
########################################################################
# Função de transferência gaussiana modificada
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

# Função para adicionar pixels na imagem de forma a otimizar o cálculo da DFT/FFT
def zeroPadding(imagem):
    cinza_h2 = cv.getOptimalDFTSize(imagem.shape[0])
    cinza_w2 = cv.getOptimalDFTSize(imagem.shape[1])
    # print("x = {} -> {}, y = {} -> {}".format(imagem.shape[0], cinza_h2, imagem.shape[1], cinza_w2))
    imagem_padded = np.zeros((cinza_h2, cinza_w2), dtype='uint8')
    imagem_padded[0:cinza_h, 0:cinza_w] = imagem
    return imagem_padded

# Restaura a imagem ao tamanho original
def unpaddingImage(imagem_padded, imagem):
    temp = np.zeros(imagem.shape, dtype='uint8')
    temp[0:imagem.shape[0], 0:imagem.shape[1]] = imagem_padded[0:imagem.shape[0], 0:imagem.shape[1]]
    return temp

# Plota FFT da imagem
def plotaFFT(imagem):
    I_fft = np.fft.fft2(imagem)
    I_shift = np.fft.fftshift(I_fft)
    I_mag = np.abs(I_shift)
    I_log = np.log(1+ I_mag)
    I_int = np.uint8(I_log)
    I_norm = cv.normalize(I_int, None, 0, 255, norm_type=cv.NORM_MINMAX)
    cv.imshow("TF", I_norm)

# Aplica o filtro homomórfico
def aplicaFiltro(func_transf, imagem):
    # Redistribui os pixels do filtro(descentralização)
    h = np.fft.fftshift(func_transf)

    # Imagem no domínio logarítmico
    I_log = np.log(1 + imagem)

    # DFT
    I_fft = np.fft.fft2(I_log)

    # Shift
    I_shifted = np.fft.fftshift(I_fft)

    # Filtragem
    I_filt = h * I_fft

    #  ITF
    I_inv_TF = np.fft.ifft2(I_filt)

    # Exponencial
    I_exp = np.exp(np.real(I_inv_TF)) - 1

    # Converte para uint8
    I_int = np.uint8(I_exp)

    return I_int

# Funções para as trackbars
def getGamaL(valor):
    # # Garante que gama_H seja maior que 1
    # if cv.getTrackbarPos('gama_H', "Menu") < 10:
    #     local_gama_H = 1
    # else:
    #     local_gama_H = cv.getTrackbarPos('gama_H', "Menu")/10
    local_gama_H = 1 if cv.getTrackbarPos('gama_H', "Menu") < 10 else cv.getTrackbarPos('gama_H', "Menu")/10
    local_c = cv.getTrackbarPos("c", "Menu")/100
    local_D0 = cv.getTrackbarPos("D0", "Menu")

    print("De getGamaL -> {}, {}, {}, {}".format(valor/100, local_gama_H, local_c, local_D0))

    H_uv = gaussModif(
        # gama_L=0.9, gama_H=5, c=3, D_0=1000, imagem=cinza_padded
        gama_L = valor/100,
        gama_H = local_gama_H,
        c = local_c,
        D_0 = local_D0,
        imagem = zeroPadding(imagem=cinza)
    )

    cv.imshow("Filtro", H_uv)
    # return valor/100

def getGamaH(valor):
    local_gama_L = cv.getTrackbarPos('gama_L', "Menu")/100
    local_c = cv.getTrackbarPos("c", "Menu")/100
    local_D0 = cv.getTrackbarPos("D0", "Menu")
    print("De getGamaH -> {}, {}, {}, {}".format(local_gama_L, valor/10, local_c, local_D0))

    H_uv = gaussModif(
        # gama_L=0.9, gama_H=5, c=3, D_0=1000, imagem=cinza_padded
        gama_L = local_gama_L,
        gama_H = 1 if valor < 10 else valor/10,
        c = local_c,
        D_0 = local_D0,
        imagem = zeroPadding(imagem=cinza)
    )

    cv.imshow("Filtro", H_uv)
    # return valor/10

def getC(valor):
    local_gama_L = cv.getTrackbarPos('gama_L', "Menu")/100
    local_gama_H = 1 if cv.getTrackbarPos('gama_H', "Menu") < 10 else cv.getTrackbarPos('gama_H', "Menu")/10
    local_D0 = cv.getTrackbarPos("D0", "Menu")
    print("De getGamaC -> {}, {}, {}, {}".format(local_gama_L, local_gama_H, valor/10, local_D0))
    H_uv = gaussModif(
        # gama_L=0.9, gama_H=5, c=3, D_0=1000, imagem=cinza_padded
        gama_L = local_gama_L,
        gama_H = local_gama_H,
        c = valor/100,
        D_0 = local_D0,
        imagem = zeroPadding(imagem=cinza)
    )

    cv.imshow("Filtro", H_uv)

def getD0(valor):
    local_gama_L = cv.getTrackbarPos('gama_L', "Menu")/100
    local_gama_H = 1 if cv.getTrackbarPos('gama_H', "Menu") < 10 else cv.getTrackbarPos('gama_H', "Menu")/10
    local_c = cv.getTrackbarPos("c", "Menu")/100
    print("De getGamaL -> {}, {}, {}, {}".format(local_gama_L, local_gama_H, local_c, valor))
    H_uv = gaussModif(
        # gama_L=0.9, gama_H=5, c=3, D_0=1000, imagem=cinza_padded
        gama_L = local_gama_L,
        gama_H = local_gama_H,
        c = local_c,
        D_0 = valor,
        imagem = zeroPadding(imagem=cinza)
    )

    cv.imshow("Filtro", H_uv)

########################################################################
# Programação
########################################################################
# Cria o menu de controle
# Limite inferior da curva de histerese
cv.createTrackbar("gama_L", "Menu", 1, 100, getGamaL)

# Limite superior da curva de histerese
cv.createTrackbar("gama_H", "Menu", 1, 100, getGamaH)

# Inclinação da curva de histerese
cv.createTrackbar("c", "Menu", 1, 100, getC)

# Frequencia de corte
cv.createTrackbar("D0", "Menu", 30, 3000, getD0)

# #  Zero padding para otimizar a DFT
# cinza_padded = zeroPadding(cinza)

# # Aplica o filtro e retorna a imagem filtrada
# imagem_filtrada = aplicaFiltro(H_uv, cinza_padded)
#
# # Restaura imagem ao tamanho original
# imagem_restaurada = unpaddingImage(imagem_padded=imagem_filtrada, imagem=cinza)

########################################################################
# Exibição
########################################################################
# Menu
cv.imshow("Menu", menu)

# # Imagem original
# cv.imshow("Original", cinza)
#
# # FFT da imagem
# plotaFFT(cinza_padded)

# # Imagem filtrada
# cv.imshow("Imagem filtrada", imagem_restaurada)

cv.waitKey(0)
cv.destroyAllWindows()

