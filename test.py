import pyautogui
import time
import cv2 as cv


def test(name, numero):
    raidcord = pyautogui.locateCenterOnScreen(name, grayscale=False, confidence=numero)
    print(raidcord)
    time.sleep(1)
    pyautogui.click(raidcord)
    return raidcord
