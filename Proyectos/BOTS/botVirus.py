from xmlrpc.client import boolean
import pyautogui as pg
import time as tm

from regex import P

tm.sleep(5)
number = 0
while number <15:
    pg.moveTo(15,1060)
    pg.click()
    pg.typewrite("Bloc de notas")
    pg.press("enter")
    number = number +1

