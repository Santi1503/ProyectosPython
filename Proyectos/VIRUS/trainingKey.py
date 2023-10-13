from pynput.mouse import Controller
#from pynput.keyboard import Controller

i = 1

def controlMouse():
    mouse = Controller()
    mouse.position = (300,200)
    
while i == 1:
    controlMouse()
"""def controlKeyboard():
    keyboard = Controller()
    keyboard.type("Hola que estamos haciendoooooooooooo")"""
#controlMouse()

