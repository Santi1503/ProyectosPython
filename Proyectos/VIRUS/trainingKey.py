from pynput.mouse import Controller
from pynput.keyboard import Controller


def controlMouse():
    mouse = Controller()
    mouse.position = (3000,200)
    
def controlKeyboard():
    keyboard = Controller()
    keyboard.type("Hola que estamos haciendoooooooooooo")

controlKeyboard()

