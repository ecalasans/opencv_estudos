'''
Módulo com funções para auxiliar no manejo
do OpenCV em notebooks jupyter

por Eric Calasans
20/03/2020
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

'''
Função imshoGrayscale - mostra a imagem em escala de cinza utilizando
Matplotilb

Parâmetros:  matImage - matriz obtida pelo método cv2.imread do OpenCV ou
    uma matriz do tipo np.array
'''
def imshowGrayscale(matImage):
    #Converte o modo de cor de BGR para RGB - modo de cor utilizado pelo Matplotlib
    rgb = cv2.cvtColor(matImage, cv2.COLOR_BGR2RGB)

    #Plota a imagem
    ax = plt.gca()
    ax.imshow(rgb[:, :, 1], cmap='gray', interpolation='none', origin='upper')

    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    ax.set_ylabel('x')
    ax.set_xlabel('y')

    plt.show()


'''
Função extractRegion - extrai uma região de uma imagem definida
por um retângulo 

Parâmetros:  imagem - matriz obtida pelo método cv2.imread do OpenCV ou
    uma matriz do tipo np.array
             region - lista contendo coordenadas do canto superior esquerdo e
    inferior direito do tipo [(x1,y1), (x2,y2)]

Retorno:  np.array (abs(x2-x1), abs(y2-y1))
'''
def extractRegion(imagem, region):
    # Constrói o retângulo desejado
    x_i = min(region[0][0], region[1][0])
    x_f = max(region[0][0], region[1][0])

    y_i = min(region[0][1], region[1][1])
    y_f = max(region[0][1], region[1][1])

    return np.array(imagem[x_i:x_f, y_i:y_f])