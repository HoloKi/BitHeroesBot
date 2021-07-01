import pyautogui
import time
import cv2 as cv
import classe


def test(name, numero):
    raidcord = pyautogui.locateCenterOnScreen(name, grayscale=False, confidence=numero)
    print(raidcord)
    time.sleep(1)
    pyautogui.click(raidcord)
    return raidcord

def raid():
    prova = classe.bit(r"image\prova.png", 0.5)
    prova.bottone()
