import matplotlib.pyplot as plt
import cv2
import jupytercv


img = cv2.imread('rosas.jpeg')
jupytercv.imshow_grayscale(img)

