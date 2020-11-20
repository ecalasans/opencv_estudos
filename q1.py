import cv2
import numpy as np

# Cria matriz que vai abrigar as duas imagens
tela = np.zeros((480, 1280), dtype='uint8')

# Cria o objeto de captura de video
capture = cv2.VideoCapture(0)

# Ajusta o tamanho da imagem e a taxa de captura
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
capture.set(cv2.CAP_PROP_FPS, 30)

# Checa se a camera está funcionando
if not capture.isOpened():
    print("A camera nao estah funcionando")

# Setup do histograma
# Ajuste do histograma
hist_altura = 128
hist_largura = 256
nbins = 256

while capture.isOpened():
    # Captura frame a frame
    sucesso, frame = capture.read()

    # Matriz da imagem dos histograma com zeros e preenche com fundo branco
    HN = np.zeros((hist_altura, hist_largura), dtype="uint8")
    HE = np.zeros((hist_altura, hist_largura), dtype="uint8")
    HN[:] = 255
    HE[:] = 255

    # Matriz dos bins
    B = np.arange(nbins, dtype=np.int32).reshape(nbins, 1)

    # Se houve sucesso na captura exibe a imagem
    if sucesso:
        # Converte a imagem em tom de cinza
        cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calcula o histograma normal
        hist_normal = cv2.calcHist(cinza, [0], None, [nbins], [0, 256])

        # Calcula o histograma equalizado
        hist_eq, bins_eq = np.histogram(cinza, bins=256, density=True)
        hist_acum = np.cumsum(hist_eq)
        s_k = np.round(255*hist_acum, 0)
        hist_equalizado = np.clip(s_k, 1, 256).astype('uint8')


        # Normaliza o histograma para o maior valor da altura da imagem do histograma
        cv2.normalize(hist_normal, hist_normal, 0, hist_altura, norm_type=cv2.NORM_MINMAX)
        hist_arred = np.int32(np.around(hist_normal))

        # Monta uma matriz com os bins do histograma normal e do histograma equalizado
        bins_hist_normal = np.column_stack((B, hist_arred))
        bins_hist_equal = np.column_stack((B, hist_equalizado))


        # Cria os retângulos que denotam os valores do histograma
        for x, y in bins_hist_normal:
            cv2.rectangle(HN, (x, 0), (x, y), (0, 0, 0), -1)
        for u, v in bins_hist_equal:
            cv2.rectangle(HE, (u, 0), (u, v), (0, 0, 0), -1)

        # Inverte a matriz da imagem do histograma para ser plotada na posição normal
        HN = np.flipud(HN)
        HE = np.flipud(HE)

        # Cria a imagem equalizada
        cinza_eq = hist_equalizado[cinza]

        # Sobrepõe o histograma na imagem
        cinza[0:HN.shape[0], 0:HN.shape[1]] = HN[0:HN.shape[0], 0:HN.shape[1]]
        cinza_eq[0:HE.shape[0], 0:HE.shape[1]] = HE[0:HE.shape[0], 0:HE.shape[1]]

        # Cria a tela com as imagens normal e equalizada
        tela[:, 0:640] = cinza[:]
        tela[:, 640:1280] = cinza_eq[:]

        # Exibe a imagem
        cv2.imshow('Normal e Equalizada', tela)

        # Espera pela tecla 'q' ou 'Q' para sair
        if cv2.waitKey(50) and (0xFF == ord('q') or 0xFF == ord('Q')):
            break
    else:
        print("Algum problema com a camera que nao estah capturando!  Verifique o dispositivo")
        break

# Libera a camera e os recursos da memoria
capture.release()
cv2.destroyAllWindows()