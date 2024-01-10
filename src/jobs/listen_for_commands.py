    
from src.jobs.clicks import *
import speech_recognition as sr

voice_thread_running = True
r = sr.Recognizer()
def listen_for_commands():
    
    global voice_thread_running
    while voice_thread_running:
        with sr.Microphone() as source:
            print("Aguardando comandos de voz...")
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio, language='pt-BR').lower()
                print(f"Comando recebido: {command}")
                perform_click(command)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Erro de serviço; {e}")
