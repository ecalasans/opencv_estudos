import cv2
import numpy as np

### Operações aritméticas com imagens
swars = cv2.imread('starwars.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('normal', swars)

# # 1.  Saturation
# x = np.uint8([250])
# y = np.uint8([50])
#
# # Valores são truncados para caber no tipo do array
# result_opencv = cv2.add(x, y)
# print("cv2.add(x: '{}', y: '{}') = '{}'".format(x, y, result_opencv))
#
# # Aplicada operação resto
# result_numpy = x + y
# print("x:'{}' + y:'{}' = '{}'".format(x, y, result_numpy))

# 2.  Adição e subtração
# M = np.ones(swars.shape, dtype='uint8') * 60
# print(M)
# scalar = np.ones(swars.shape, dtype='uint8') * 110
# print(scalar)
#
# add_scalar = cv2.add(swars, scalar)
# cv2.imshow('add_scalar', add_scalar)
# cv2.waitKey(0)
#
# swars_ad = cv2.add(swars, M)
# swars_sub = cv2.subtract(swars, M)
# cv2.imshow('add', swars_ad)
# cv2.imshow('sub', swars_sub)
# cv2.waitKey(0)

# 3.  Blending
# gradient_x = cv2.Sobel(swars, cv2.CV_16S, 1,0,3)
# gradient_y = cv2.Sobel(swars, cv2.CV_16S, 1,0,3)
#
# abs_gradient_x = cv2.convertScaleAbs(gradient_x)
# abs_gradient_y = cv2.convertScaleAbs(gradient_y)
#
# sobel_image = cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y, 0.5, 0)
#
# cv2.imshow('gradx', abs_gradient_x)
# cv2.imshow('grady', abs_gradient_y)
# cv2.imshow('sobel', sobel_image)
# cv2.waitKey(0)