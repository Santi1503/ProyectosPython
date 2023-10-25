import pyautogui as pg
from pynput.mouse import Listener

screenshot_counter = 0

def takeScreenshot(x,y):
    global screenshot_counter
    screenShot = pg.screenshot()
    file_path = r'C:\Users\gomez\Downloads\prueba\screenshot_{}.png'.format(screenshot_counter) 
    # You need to change the path so you can use it
    
    screenShot.save(file_path)
    screenshot_counter += 1

with Listener(on_move=takeScreenshot) as l:
    l.join()