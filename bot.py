import json
import logging
from ClassBot import Menu, DeveloperMode
from colorama import *
import os.path
import pyautogui
import time
import traceback
import cv2 as cv
import os
import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


'''
Function to resize bot window
'''
from ctypes import windll, byref
import ctypes.wintypes as wintypes

init(autoreset=True)

VERSION = "7.1.0"

STDOUT = -11

hdl = windll.kernel32.GetStdHandle(STDOUT)
rect = wintypes.SMALL_RECT(0, 0, 56, 26)  # (left, top, right, bottom)
windll.kernel32.SetConsoleWindowInfo(hdl, True, byref(rect))


def main():
    dependencies()
    print("\n\n\n")
    logging.basicConfig(filename="latest.log", filemode="w", format='%(asctime)s - %(funcName)s :   %(message)s',
                        level=logging.DEBUG)
    logging.info(f"VERSION : {VERSION} - BOT by HoloKi. Info : https://github.com/HoloKi/BitHeroesBot")
    logging.info("https://discord.gg/h98xsssEpe")
    logging.debug(screensize)
    logging.info(
        "The bot is completely free, any sale is prohibited.If someone sold it to you, get your money back and report "
        "it to the developer")
    print(f"BitHeroesBot by Holoki ------ VERSION = {VERSION} ------")
    print("Translate by PastShadie")
    print("All info on latest.log")
    # check if there isnt a data.json
    DeveloperMode.Populate()

    print(" ____  _       _           _")
    print("|  _ \| |     | |         | |")
    print("| |_) | |__   | |__   ___ | |_")
    print("|  _ <| '_ \  | '_ \ / _ \| __|")
    print("| |_) | | | | | |_) | (_) | |_ ")
    print("|____/|_| |_| |_.__/ \___/ \__|")
    while True:
        cycle = Menu.menu()
        if cycle == 0:
            exit()


# Install dependecies
def dependencies():
    try:
        os.system('cmd /c "pip install -r requirements"')
    except Exception as e:
        print(e)
        logging.error(e)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(traceback.format_exc())
        print(e)
