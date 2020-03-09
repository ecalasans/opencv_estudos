import cv2

img = cv2.imread('pythonlogo.png')

print(img.size)

cv2.imshow('Imagem', img)
cv2.waitKey(1000)

img[0:100, 0:200] = (255,255,255)

cv2.imshow("Imagem", img)
cv2.waitKey(10000)