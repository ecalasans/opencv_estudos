import cv2
import numpy as np

swars = cv2.imread('starwars.jpg')

# Scaling
# aum = cv2.resize(swars, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

height, width = swars.shape[:2]
# Translating
#M = np.float32([[1,0,200], [0,1,30]]) # Matriz de translação

#Rotating
#M = cv2.getRotationMatrix2D((width/2, height/2), 36, 1)

#Affine
#pts_1 = np.float32([[135, 45], [385, 45], [135, 230]])
#pts_2 = np.float32([[135, 45], [385, 45], [150, 230]])
#M = cv2.getAffineTransform(pts_1, pts_2)
#img = cv2.warpAffine(swars, M, (width, height))

#Cropping
img = swars[80:200, 30:330]

# Aplicando filtros
# Blurring

cv2.imshow('', img)
cv2.waitKey(0)