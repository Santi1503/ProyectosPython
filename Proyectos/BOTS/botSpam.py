import pyautogui as pg
import time as tm

tm.sleep(5)

with open("/Proyectos/FEATURES/mensaje1.txt", "r") as file:
    for line in file:
        pg.typewrite(line)
        pg.press("enter")
