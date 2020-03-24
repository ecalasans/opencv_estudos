import cv2
import jupytercv

imagem = cv2.imread('rx.jpg', cv2.IMREAD_GRAYSCALE)

M = imagem.shape[1]
N = imagem.shape[0]

q1 = [(0, 0), ((M-1)//2, (N-1)//2)]
q2 = [(0, (N-1)//2), ((M-1)//2, N)]

print(q1, q2)

