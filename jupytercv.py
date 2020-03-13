# Módulo com funções para auxiliar no manejo
# do OpenCV em notebooks jupyter

import cv2
import numpy as np
import matplotlib.pyplot as plt

def imshow_grayscale(matImage):
    rgb = cv2.cvtColor(matImage, cv2.COLOR_BGR2RGB)

    ax = plt.gca()
    ax.imshow(rgb[:, :, 1], cmap='gray', interpolation='none', origin='upper')

    ax.xaxis.set_ticks_position('top')

    plt.show()