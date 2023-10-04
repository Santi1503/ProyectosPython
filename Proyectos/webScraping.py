import urllib.request as ulr
import pyautogui as pg
import time as tm
tm.sleep(3)
datos = ulr.urlopen(
    'https://pyautogui.readthedocs.io/en/latest/').read().decode()

tm.sleep(5)
pg.moveTo(670, 1052)
pg.click()
tm.sleep(1)
pg.typewrite("Bloc de notas")
pg.press("enter")

tm.sleep(3)
pg.typewrite(datos)
