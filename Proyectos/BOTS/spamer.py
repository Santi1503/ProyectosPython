import pyautogui
import webbrowser
from time import sleep

webbrowser.open("https://web.whatsapp.com/send?phone=+34")
sleep(10)
"""
pyautogui.typewrite("XD")
pyautogui.press("enter")
"""

with open("mensajes.txt", "r") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
