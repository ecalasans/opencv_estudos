import cv2
import jupytercv

imagem = cv2.imread('rx.jpg', cv2.IMREAD_GRAYSCALE)

if not imagem.any():
    print("Não tem imagem")
else:
    jupytercv.imshow_grayscale(imagem)
    print("Dimensões:  x = %d \t y = %d" % (imagem.shape[1], imagem.shape[0]))

p1x = int(input("p1x = "))
p1y = int(input("p1y = "))

p2x = int(input("p2x = "))
p2y = int(input("p2y = "))

retangulo = not ((p1x == p2x) or (p1y == p2y))

if retangulo:
    x_i = min(p1x, p2x)
    x_f = max(p1x, p2x)

    y_i = min(p1y, p2y)
    y_f = max(p1y, p2y)

    for x in range(x_i, x_f):
        for y in range(y_i, y_f):
            imagem[x, y] = 255 - imagem[x, y]

jupytercv.imshow_grayscale(imagem)