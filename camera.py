import cv2

# Cria o objeto de captura da câmera - 0 é o índice da webcam
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Checa se a câmera tá funcionando
if capture.isOpened() == False:
    print("Não conseguiu ligar a webcam")

# Começa a captura
while capture.isOpened():
    # Captura frame-by-frame
    ret, frame = capture.read()

    if ret == True:
        # Mostra uma janela normal
        cv2.imshow("Janela normal", frame)

        # Em escala de cinza
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Cinza", gray_scale)

        # Aperte q para fechar o programa
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    else:
        capture.release()
        cv2.destroyAllWindows()