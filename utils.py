import pyautogui
from time import sleep
from datetime import datetime

pyautogui.pause = 2

def writeDateTime(date):
    pyautogui.write(date.strftime("%d"))
    pyautogui.write(date.strftime("%m"))
    pyautogui.write(date.strftime("%Y"))
    pyautogui.write(date.strftime("%H"))
    pyautogui.write(date.strftime("%M"))

def openChrome():
    pyautogui.press("win")
    sleep(1)
    pyautogui.write("google chrome")
    sleep(2)
    pyautogui.press("enter")
    sleep(5)

def loginSbsWeb(login, password):
    pyautogui.write("SBSWEB")
    pyautogui.press("enter")
    sleep(5)
    pyautogui.write(login)
    pyautogui.press("tab")
    pyautogui.write(password)
    pyautogui.press("enter")
    sleep(5)

def navigate():
    pyautogui.click(198, 346)
    sleep(2)
    pyautogui.click(622, 220)
    sleep(2)
    pyautogui.click(633, 246)
    sleep(2)
    pyautogui.click(640, 243)
    sleep(2)
    pyautogui.click(677, 271)
    sleep(2)
    pyautogui.click(633, 279)
    sleep(2)
    pyautogui.click(465, 155)
    sleep(2)
    pyautogui.click(575, 402)
    sleep(2)
    pyautogui.click(734, 479)
    sleep(2)
    pyautogui.click(583, 277)
    sleep(2)
    pyautogui.click(603, 310)
    sleep(2)
    pyautogui.press("tab")
    sleep(1)
    pyautogui.press("tab")
    sleep(1)
