from xmlrpc.client import boolean
import pyautogui as pg
import time as tm
import subprocess

from regex import P

tm.sleep(5)
number = 0
while number < 10:
    """pg.press('win')
    pg.typewrite("Bloc de notas")
    pg.press("enter")
    tm.sleep(1)"""
    
    subprocess.Popen('start cmd', shell=True)
    number = number + 1
