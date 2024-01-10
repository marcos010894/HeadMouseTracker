import cv2
import pyautogui

import threading
from src.jobs.listen_for_commands import *
pyautogui.FAILSAFE = False

# Inicialize a câmera
cap = cv2.VideoCapture(0)

# Inicialize o reconhecedor de voz


# Flag para controlar a thread de reconhecimento de voz


# Iniciar a thread de reconhecimento de voz
voice_thread = threading.Thread(target=listen_for_commands)
voice_thread.start()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Centro da imagem
    img_center_x, img_center_y = frame.shape[1] // 2, frame.shape[0] // 2

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Centro da cabeça
        head_center_x = x + w // 2
        head_center_y = y + h // 2
        multiplicador = 1

        # Mapeie as coordenadas da cabeça para a tela do computador
        screen_x = int((head_center_x / frame.shape[1]) * pyautogui.size().width * multiplicador)
        screen_y = int((head_center_y / frame.shape[0]) * pyautogui.size().height * multiplicador)

        # Mova o mouse para as coordenadas mapeadas
        pyautogui.moveTo(screen_x, screen_y)

    cv2.imshow('Head Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()