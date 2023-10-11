import pyautogui as pg
import time as tm
tm.sleep(3)

currentMouseX, currentMouseY = pg.position()
print(currentMouseX)
print(currentMouseY)
