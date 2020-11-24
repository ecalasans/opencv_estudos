import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
########################################################################
# Definições
########################################################################
# Vídeo utilizado
video_in = cv.VideoCapture('imagens/universal.mp4')

# Filtro da média
media = np.ones((3,3), dtype=np.float32)/9

# Dimensões e propriedades do arquivo de vídeo
video_in_h = np.int(video_in.get(cv.CAP_PROP_FRAME_HEIGHT))
video_in_w = np.int(video_in.get(cv.CAP_PROP_FRAME_WIDTH))
video_in_meio = np.int(video_in_h/2)    # Ponto médio do eixo x

# Inicialização de variáveis de interesse
pivo = video_in_meio   #  Ponto médio entre as linhas
linha_sup = 0   # Limite superior da região de foco
linha_inf = 0   # Limite inferior da região de foco
d = 0   # Força do decaimento

# Matriz para um frame


# Canvas para plotagem das imagens
# Dimensões do canvas
canvas = np.zeros((video_in_h, (2*video_in_w) + 1, 3), dtype='uint8')
cv.namedWindow('Tilt Shift')

# Função de ponderação(calcula alfa e 1-alfa)
def alfa(ls, li, d):
    x = np.zeros((video_in_h, video_in_w, 3), dtype='float32')
    l1 = ls - video_in_meio
    l2 = li - video_in_meio

    for i in range(0, video_in_h):
        x[i, :, :] = i - video_in_meio

    uns = np.ones((video_in_h, video_in_w, 3), dtype=np.float)
    alfa = (np.tanh((x-l1)/d) - np.tanh((x-l2)/d))*0.5

    # fig, ax = plt.subplots()
    # ax.plot(range(0, im_h), alfa[:, 0, 1])
    # ax.set_title('Função de ponderação α')
    # ax.set_xlabel('Coord. x no sistema OpenCV')
    # ax.set_ylabel('α')
    # plt.savefig('imagens/alfa.jpg')
    # plt.show()

    um_menos_alfa = np.subtract(uns, alfa)
    return alfa, um_menos_alfa

#Funções para trackbars
# Ajusta altura da faixa em foco
def ajustaAltura(valor, frame):
    # Calcula a altura das linhas superior e inferior
    global linha_sup, linha_inf, pivo
    pivo = cv.getTrackbarPos('Posicao na Janela', 'Tilt Shift')
    linha_sup = pivo - valor
    linha_inf = pivo + valor

    # Desenha as linhas na imagem e a atualiza com a posição das mesmas
    cv.line(canvas, (0, linha_sup), (video_in_w, linha_sup), color=(0,0,255),
            thickness=1, lineType=cv.LINE_AA)
    cv.line(canvas, (0, linha_inf), (video_in_w, linha_inf), color=(0, 255, 0),
            thickness=1, lineType=cv.LINE_AA)

    cv.imshow("Tilt Shift", canvas)

    canvas[:, 0:480, :] = frame
    canvas[:, 481:961, :] = 200

    #  Mostra o efeito na imagem resultante se d for diferente de zero(evita
    #  o erro de divisão por 0
    # if d == 0:
    #     canvas[:, 481:961, :] = 200
    # else:
    #     efeito = tiltShift(linha_sup, linha_inf, d)
    #     canvas[:, 481:961, :] = efeito

    cv.line(canvas, (0, linha_sup), (video_in_w, linha_sup), color=(0, 0, 255),
            thickness=1, lineType=cv.LINE_AA)
    cv.line(canvas, (0, linha_inf), (video_in_w, linha_inf), color=(0, 255, 0),
            thickness=1, lineType=cv.LINE_AA)

    cv.imshow("Tilt Shift", canvas)
    pivo = cv.getTrackbarPos('Posicao na Janela', 'Tilt Shift')

# # Ajusta força do decaimento
# def ajustaForca(valor):
#     global d
#     d = valor
#
#     if d == 0:
#         canvas[:, 481:961, :] = imagem_media
#     else:
#         efeito = tiltShift(linha_sup, linha_inf, d)
#         canvas[:, 481:961, :] = efeito
#     cv.imshow("Tilt Shift", canvas)
#
# # Ajusta posição vertical do desfoque
# def ajustaPosicao(valor):
#     global linha_sup, linha_inf
#     pivo = np.int((linha_sup + linha_inf)/2)
#     # Desloca as linhas em bloco para cima ou para baixo
#     if valor < pivo:
#         # Desloca o bloco
#         linha_sup = linha_sup - 1
#         linha_inf = linha_inf - 1
#
#         # Desenha as linhas na imagem e a atualiza com a posição das mesmas
#         cv.line(canvas, (0, linha_sup), (im_w, linha_sup),
#                 color=(0, 0, 255), thickness=1, lineType=cv.LINE_AA)
#         cv.line(canvas, (0, linha_inf), (im_w, linha_inf),
#                 color=(0, 255, 0), thickness=1, lineType=cv.LINE_AA)
#
#         cv.imshow("Tilt Shift", canvas)
#
#         canvas[:, 0:480, :] = imagem
#         if d == 0:
#             canvas[:, 481:961, :] = imagem_media
#         else:
#             efeito = tiltShift(linha_sup, linha_inf, d)
#             canvas[:, 481:961, :] = efeito
#
#         cv.line(canvas, (0, linha_sup), (im_w, linha_sup),
#                 color=(0, 0, 255), thickness=1, lineType=cv.LINE_AA)
#         cv.line(canvas, (0, linha_inf), (im_w, linha_inf),
#                 color=(0, 255, 0), thickness=1, lineType=cv.LINE_AA)
#
#         cv.imshow("Tilt Shift", canvas)
#
#     else:
#         # Desloca o bloco
#         linha_sup = linha_sup + 1
#         linha_inf = linha_inf + 1
#
#         # Desenha as linhas na imagem e a atualiza com a posição das mesmas
#         cv.line(canvas, (0, linha_sup), (im_w, linha_sup), color=(0, 0, 255),
#                 thickness=1, lineType=cv.LINE_AA)
#         cv.line(canvas, (0, linha_inf), (im_w, linha_inf), color=(0, 255, 0),
#                 thickness=1, lineType=cv.LINE_AA)
#
#         cv.imshow("Tilt Shift", canvas)
#
#         canvas[:, 0:480, :] = imagem
#
#         if d == 0:
#             canvas[:, 481:961, :] = imagem_media
#         else:
#             efeito = tiltShift(linha_sup, linha_inf, d)
#             canvas[:, 481:961, :] = efeito
#
#         cv.line(canvas, (0, linha_sup), (im_w, linha_sup), color=(0, 0, 255),
#                 thickness=1, lineType=cv.LINE_AA)
#         cv.line(canvas, (0, linha_inf), (im_w, linha_inf), color=(0, 255, 0),
#                 thickness=1, lineType=cv.LINE_AA)
#
#         cv.imshow("Tilt Shift", canvas)
#
#
# Função para produção do tilt shift e plotagem no canvas
def tiltShift(ls, li, d, frame):
    a, um_menos_a = alfa(ls, li, d)

    frame_media = cv.filter2D(frame, None, media)

    im_1 = np.multiply(a, frame)
    im_2 = np.multiply(um_menos_a, frame_media)

    im_1 = im_1.astype('uint8')
    im_2 = im_2.astype('uint8')
    return im_1 + im_2

# # Função que salva a saída num arquivo
# def salvaArquivo(state, param):
#     ts = tiltShift(linha_sup, linha_inf, d)
#     cv.imwrite('tiltshift_result.jpg',ts)
#     print("Imagem salva!!")

if video_in.isOpened() is False:
    print('Erro ao abrir arquivo de video')

while video_in.isOpened():
    cap, video_frame = video_in.read()
    global M_frame

    if cap is True:
        M_frame = video_frame

        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

# Criação dos controles
# Trackbar para tamanho da faixa de foco
cv.createTrackbar("Janela de Foco", "Tilt Shift", 0, video_in_h, ajustaAltura)

# # Trackbar para regular a força do decaimento
# cv.createTrackbar("Forca do decaimento(d)", "Tilt Shift", 0, 50, ajustaForca)
#
# # Trackbar para ajustar a posição vertical da janela de foco
# cv.createTrackbar("Posicao na Janela", "Tilt Shift", 180, im_h, ajustaPosicao)
#
# # Cria o botão para salvar a figura
# cv.createButton("Salvar foto", salvaArquivo, None, cv.QT_PUSH_BUTTON)
########################################################################
# Programação
########################################################################
#alfa(190, 250, 5)


video_in.release()
cv.destroyAllWindows()