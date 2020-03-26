# Módulo com funções para auxiliar no manejo
# do OpenCV em notebooks jupyter

import cv2
import matplotlib.pyplot as plt
import numpy as np

def imshowGrayscale(matImage):
    rgb = cv2.cvtColor(matImage, cv2.COLOR_BGR2RGB)

    ax = plt.gca()
    ax.imshow(rgb[:, :, 1], cmap='gray', interpolation='none', origin='upper')

    ax.xaxis.set_ticks_position('top')

    plt.show()

def extractRegion(imagem, region):
    x_i = min(region[0][0], region[1][0])
    x_f = max(region[0][0], region[1][0])

    y_i = min(region[0][1], region[1][1])
    y_f = max(region[0][1], region[1][1])

    return np.array(imagem[x_i:x_f, y_i:y_f])