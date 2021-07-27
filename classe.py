import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
import sys

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base


class bit:
    def __init__(self, image, confi):
        self.image = image
        self.confi = confi

    def bottone(self):
        button = pyautogui.locateCenterOnScreen(self.image, grayscale=False, confidence=float(self.confi))
        logging.debug(f"bottone = {button}")
        if button is not None:
            time.sleep(3)
            pyautogui.click(button)
            time.sleep(1)
            return 1
        else:
            cprint(f"Error, {self.image} not found!", "red", attrs=['bold'])
            logging.error(f"{self.image} not found!")
            return 0

    def ispresence(self):
        presente = pyautogui.locateCenterOnScreen(self.image, grayscale=False, confidence=float(self.confi))
        logging.debug(f"presence = {presente}")
        if presente is not None:
            #logging.debug("DEBUG: è presente!")
            return 1
        else:
            #logging.debug("DEBUG:non è presente!")
            return 0

    def timer(self):
        for i in range(10, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write('remaining time: ' + str(i) + 's  ')
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")

    def getImage(self):
        return self.image
