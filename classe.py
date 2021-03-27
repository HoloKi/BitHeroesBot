import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base


class bit:
    def __init__(self, image, confi):
        self.image = image
        self.confi = confi

    def bottone(self):
        button = pyautogui.locateCenterOnScreen(self.image, grayscale=False, confidence=self.confi)
        logging.debug(f"bottone = {button}")
        if button is not None:
            time.sleep(5)
            pyautogui.click(button)
            time.sleep(2)
            return 1
        else:
            cprint("Errore, bottone non trovato!", "red", attrs=['bold'])
            return 0
