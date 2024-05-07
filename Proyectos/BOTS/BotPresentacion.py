import webbrowser
import pyautogui as pg
import time as tm
import speech_recognition as sr
import pyttsx3
tm.sleep(5)


webbrowser.open("https://web.whatsapp.com")
tm.sleep(7)
pg.moveTo(278, 215)
pg.click()
pg.typewrite("...")
pg.press("enter")

tm.sleep(3)
pg.moveTo(783, 979)
pg.click()
pg.typewrite("Hola soy Corvex, el bot de Santiago :)")
pg.press("enter")


#currentMouseX, currentMouseY = pg.position()
# print(currentMouseX)
# print(currentMouseY)
