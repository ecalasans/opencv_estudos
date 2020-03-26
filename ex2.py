import cv2
import jupytercv
import numpy as np

imagem = cv2.imread('rx.jpg', cv2.IMREAD_GRAYSCALE)


M = imagem.shape[1]
N = imagem.shape[0]

q1 = [(0, 0), ((M-1)//2, (N-1)//2)]
q2 = [(0, (N-1)//2), ((M-1)//2, N)]
q3 = [((M-1)//2, 0), (M, (N-1)//2)]
q4 = [((M-1)//2, (N-1)//2),(M, N)]


# Trocar q1 com q4
im_q1 = jupytercv.extractRegion(imagem, q4)
im_q4 = jupytercv.extractRegion(imagem, q1)

# Trocar q2 com q3
im_q2 = jupytercv.extractRegion(imagem, q3)
im_q3 = jupytercv.extractRegion(imagem, q2)

print()


