import pyautogui as pg
import time
import keyboard
import random
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:
    if pg.pixel(370, 420)[0] == 0:
        click(370, 420)
    if pg.pixel(455, 420)[0] == 0:
        click(455, 420)
    if pg.pixel(540, 420)[0] == 0:
        click(540, 420)
    if pg.pixel(625, 420)[0] == 0:
        click(625, 420)
