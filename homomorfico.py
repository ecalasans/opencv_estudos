import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def hmFilter(gama_L, gama_H, c, D_0):
    pass

original = cv.imread('imagens/rxt.jpg')

cinza = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cinza_h = cinza.shape[0]
cinza_w = cinza.shape[1]

#  Zero padding para otimizar a DFT
cinza_h2 = cv.getOptimalDFTSize(cinza_h)
cinza_w2 = cv.getOptimalDFTSize(cinza_w)
print(cinza_h2, cinza_w2)

cinza_padded = np.zeros((cinza_h2, cinza_w2), dtype='uint8')
cinza_padded[0:cinza_h, 0:cinza_w] = cinza
cv.imshow("cinzapadded", cinza_padded)

# f = np.fft.fft2(cinza)
# f_shifted = np.fft.fftshift(f)
# f_mag = np.abs(f_shifted) + 1
# f_log = np.log(f_mag)
# f_norm = cv.normalize(f_log, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
# f_dft = f_norm.astype('uint8')
cv.imshow('Cinza', cinza)
# cv.imshow('DFT', f_dft)
cv.waitKey(0)
