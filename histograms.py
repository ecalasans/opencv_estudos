import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

swars = cv2.imread('starwars.jpg')

# Converte imagem para escala de cinza
swars_gray = cv2.cvtColor(swars, cv2.COLOR_BGR2GRAY)

# Calcula histograma da imagem em escala de cinza
hist_gray = cv2.calcHist([swars_gray], [0], None, [64], [0, 256]).T[0]
bins = np.arange(0,64)

# Plota o histograma
fig, ax = plt.subplots()
ax.bar(bins, hist_gray)
plt.show()

# Calcula o histograma da imagem colorida
cores = ['b', 'g', 'r']
hist_cor = []
for (i, cor) in zip(range(3), cores):
    hist_temp = cv2.calcHist([swars], [i], None, [64], [0, 256])
    hist_cor.append(hist_temp)
    plt.plot(hist_temp, color=cor)
plt.show()

# Com np.histogram
#hist, bins = np.histogram(swars_gray, bins=256)
#print(hist)
#print(bins[1:4])

'''
cv2.imshow('grayscale', swars_gray)
cv2.imshow('swars', swars)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''