import webbrowser
import pyautogui as pg
import time as tm
import speech_recognition as sr
import pyttsx3
tm.sleep(5)

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Habla, te escucho :)")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
    except:
        pass
    return rec


def run():
    rec = listen()
    if 'Mandar' in rec:
        webbrowser.open("https://web.whatsapp.com")
        tm.sleep(10)
        pg.moveTo(84, 197)
        pg.click()
        pg.typewrite("Gerson")
        pg.press("enter")

        tm.sleep(5)
        pg.moveTo(501, 1007)
        pg.click()
        pg.typewrite("Hola soy Corvex, el bot de Santiago :)")
        pg.press("enter")


run()
#currentMouseX, currentMouseY = pg.position()
# print(currentMouseX)
# print(currentMouseY)
