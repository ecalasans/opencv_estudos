import cv2
import jupytercv
import numpy as np

imagem = cv2.imread('starwars.jpg', cv2.IMREAD_GRAYSCALE)
jupytercv.imshowGrayscale(imagem)

M = imagem.shape[0]
N = imagem.shape[1]

q1 = [(0, 0), ((M)//2, (N)//2)]
q2 = [(0, (N)//2), ((M)//2, N)]
q3 = [((M)//2, 0), (M, (N)//2)]
q4 = [((M)//2, (N)//2),(M, N)]


# Trocar q1 com q4
im_q1 = jupytercv.extractRegion(imagem, q4)
im_q4 = jupytercv.extractRegion(imagem, q1)

# Trocar q2 com q3
im_q2 = jupytercv.extractRegion(imagem, q3)
im_q3 = jupytercv.extractRegion(imagem, q2)


#  Construir nova imagem
new_imagem_sup = np.hstack((im_q1, im_q2))
print(new_imagem_sup.shape)
new_imagem_inf = np.hstack((im_q3, im_q4))
print(new_imagem_inf.shape)

new_imagem = np.vstack((new_imagem_sup, new_imagem_inf))
print(new_imagem.shape)

jupytercv.imshowGrayscale(new_imagem)




