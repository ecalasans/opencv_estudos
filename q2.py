import cv2
import numpy as np
import time

def mudaSensibilidade(valor):
    return valor

cv2.namedWindow("Imagem")
# Histogramas individuais

# Ajuste do histograma
#Dimensões
hist_altura = 120
hist_largura = 320
nbins = 256

# Matriz dos histogramas individuais:  referência e atrasado
H1 = np.zeros((256, 2), dtype='uint8')
H2 = np.zeros((256, 2), dtype='uint8')

# Preenche a primeira coluna da matriz com bins(0-255)
H1[:, 0] = range(0, 256)
H2[:, 0] = range(0, 256)

# Telas dos histogramas individuais
tela_H1 = np.zeros((hist_altura, hist_largura), dtype='uint8')
tela_H2 = np.zeros((hist_altura, hist_largura), dtype='uint8')

# Container os 2 histogramas
histogramas = np.zeros((hist_altura,640), dtype='uint8')
histogramas[0:hist_altura, 0:320] = 255
histogramas[0:hist_altura, 321:640] = 200

#Container do frame e dos histogramas
tela = np.zeros((600, 640), dtype='uint8')
tela[:] = 255

# Cria uma trackbar para ajustar a tolerância do detector
cv2.createTrackbar("Tolerancia", "Imagem", 0, 100, mudaSensibilidade)

# Objeto de captura de video
cap = cv2.VideoCapture(0)

# Ajusta o tamanho da imagem e a taxa de captura
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

# Checa se a camera está funcionando
if not cap.isOpened():
    print("A camera nao estah funcionando")

while cap.isOpened():
    #Inicia a captura do histograma referência
    cap1, frame1 = cap.read()

    # Divide a imagem nos seus canais para exibição
    b, g, r = cv2.split(frame1)

    # Telas dos histogramas
    tela_H1 = np.zeros((hist_altura, hist_largura), dtype='uint8')
    tela_H2 = np.zeros((hist_altura, hist_largura), dtype='uint8')

    #Inicializa as variáveis que conterão os histogramas com 0
    hist1 = 0
    hist2 = 0

    # Diferencia os dois containers com cores de fundo diferentes
    tela_H1[:] = 255
    tela_H2[:] = 200

    # Se a primeira captura for bem sucedida
    if cap1:
        # Calcula o primeiro histograma utilizando o canal g
        hist1 = cv2.calcHist(frame1, channels=[1], mask=None, histSize=[nbins], ranges=[0,256])

        # Normaliza o histograma
        cv2.normalize(src=hist1, dst=hist1, alpha=0, beta=hist_altura, norm_type=cv2.NORM_MINMAX)

        # Preenche a segunda coluna da matriz do histograma com valores do histograma normalizado
        H1[:,1] = hist1[:,0]

        # Desenha o primeiro histograma
        for x, y in H1:
            cv2.rectangle(tela_H1, (x,0), (x,y), (150, 12, 20), -1)

    # Delay para cálculo do novo histograma
    time.sleep(0.25)

    # Inicia a captura do histograma atrasado
    cap2, frame2 = cap.read()

    # Se a segunda captura for bem sucedida
    if cap2:
        # Calcula o segundo histograma
        hist2 = cv2.calcHist(frame2, channels=[1], mask=None, histSize=[nbins], ranges=[0, 256])

        # Normaliza o histograma
        cv2.normalize(src=hist2, dst=hist2, alpha=0, beta=hist_altura, norm_type=cv2.NORM_MINMAX)

        # Preenche a segunda coluna da matriz do histograma com valores do histograma normalizado
        H2[:, 1] = hist2[:, 0]

        # Desenha o segundo histograma
        for u, v in H2:
            cv2.rectangle(tela_H2, (u, 0), (u, v), (10, 125, 210), -1)

    # Rotaciona a imagem para exibição
    tela_H1 = np.flipud(tela_H1)
    tela_H2 = np.flipud(tela_H2)

    #Coloca os histogramas na tela de exibição
    histogramas[0:hist_altura, 0:320] = tela_H1[:]
    histogramas[0:hist_altura, 320:640] = tela_H2[:]

    # Coloca labels para serem exibidos junto com os histogramas
    cv2.putText(histogramas, "Histograma atual", (60,25), cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.5, color=(0, 0, 0), thickness=1, lineType=cv2.LINE_4)
    cv2.putText(histogramas, "Histograma apos 0.25s", (380,25), cv2.FONT_HERSHEY_SIMPLEX,
               fontScale=0.5, color=(240, 240, 240), thickness=1, lineType=cv2.LINE_4)

    # Desenha a imagem com os histogramas
    tela[0:120, 0:640] = histogramas[:]
    tela[120:600, 0:640] = g[:]

    # Compara os 2 histogramas
    diferenca = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    # Calcula um indicativo de movimento e compara com a tolerância ajustada:
    # Se for maior que a tolerância imprime mensagem na imagem
    indice_mov = np.round(1-diferenca, 4)
    tolerancia = cv2.getTrackbarPos("Tolerancia", "Imagem")/100


    if indice_mov > tolerancia:
        cv2.putText(tela, 'Movimento detectado!!', (150, 180), cv2.FONT_HERSHEY_DUPLEX,
                    fontScale=1, color=(255,255,255), thickness=2, lineType=cv2.LINE_4)

    cv2.imshow('Imagem', tela)
    # Espera pela tecla 'q' ou 'Q' para sair
    if cv2.waitKey(50) and (0xFF == ord('q') or 0xFF == ord('Q')):
        break