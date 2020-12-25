import cv2
import numpy as np

swars = cv2.imread('starwars.jpg')

# 1.  Translação
# Matriz de translação: [[1 0 Tx][0 1 Ty]]
h, w = swars.shape[:2]
print(swars.shape)

T = np.float32([[1, 0, w/4], [0, 1, h/4]])
transl = cv2.warpAffine(swars, T, (w, h))

#2.  Rotação
# Matriz de Rotação:  [[cos x -sen x][sen x cos x]]
R = cv2.getRotationMatrix2D((w/2, h/2), 45, 1)
rot = cv2.warpAffine(swars, R, (w, h))

#3.  Scaling
scal1 = cv2.resize(swars, None, fx=0.6, fy=0.6)
scal2 = cv2.resize(swars, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC)
scal3 = cv2.resize(swars, (900,400), interpolation=cv2.INTER_AREA)

#4.  Pyramiding
smaller = cv2.pyrDown(swars)
larger = cv2.pyrUp(swars)

#5.  Cropping
sr, sc = int(h *.25), int(w *.25)
er, ec = int(h *.5), int(w * .5)

cropped = swars[sr:er, sc:ec]

#5.  Funções aritméricas com imagens
# Adição
M = np.ones(swars.shape, dtype="uint8") * 58
adicao = cv2.add(swars, M)
subtracao = cv2.subtract(swars, M)
#cv2.imshow('Translação', transl)
#cv2.imshow('Rotação', rot)
#cv2.imshow('INTER_LINEAR', scal1)
#cv2.imshow('INTER_CUBIC', scal2)
#cv2.imshow('INTER_AREA', scal3)
#cv2.imshow('Pequeno', smaller)
#cv2.imshow('Grande', larger)
#cv2.imshow('Cropped', cropped)
cv2.imshow('Adicao', adicao)
cv2.imshow('Subtracao', subtracao)
cv2.imshow('', swars)
cv2.waitKey(0)
cv2.destroyAllWindows()