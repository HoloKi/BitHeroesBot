import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
import sys

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base
errore = colored("Please report this bug/error on github or discord\n", 'red', attrs=['bold'])

class bit:
    def __init__(self, image, confi):
        self.image = image
        self.confi = confi


    # Function to find image and click it
    # button return (x,y) as coordinates or None if image not found
    def bottone(self):
        button = pyautogui.locateCenterOnScreen(self.image, grayscale=False, confidence=float(self.confi))
        logging.debug(f"{self.getImage()} = {button}")
        if button is not None:
            time.sleep(3)
            pyautogui.click(button)
            time.sleep(1)
            return 1
        else:
            cprint(f"Error, {self.image} not found!", "red", attrs=['bold'])
            cprint(errore)
            logging.error(f"{self.image} not found!")
            return 0

    def ispresence(self):
        presente = pyautogui.locateCenterOnScreen(self.image, grayscale=False, confidence=float(self.confi))
        logging.debug(f"{self.image} presence = {presente}")
        if presente is not None:
            # logging.debug("DEBUG: è presente!")
            return 1
        else:
            # logging.debug("DEBUG:non è presente!")
            return 0
    # isPresence  without cdebug control so no spam on logging

    def no_shardControl(self):
        no_shard = self.__init__(r"image\noshard.png", 0.5)
        res = no_shard.ispresence()
        if res == 1:
            print("No shards!")
        else:
            print("Ok!")

    def SafeControl(self):
        presente = pyautogui.locateCenterOnScreen(self.image, grayscale=False, confidence=float(self.confi))
        # logging.debug(f"presence = {presente}")
        if presente is not None:
            # logging.debug("DEBUG: è presente!")
            return 1
        else:
            # logging.debug("DEBUG:non è presente!")
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

    # Function to find image and click it
    # button return (x,y) as coordinates or None if image not found
    # using x,y to permit x editing (right)
    # modifier
    def bottoneright(self, modifier):
        x,y = pyautogui.locateCenterOnScreen(self.image, grayscale=False, confidence=float(self.confi))
        logging.debug(f"{self.getImage()} = {(x,y)}")
        if (x,y) is not None:
            time.sleep(3)
            pyautogui.click(x+int(modifier),y)
            time.sleep(1)
            return 1
        else:
            cprint(f"Error, {self.image} not found!", "red", attrs=['bold'])
            cprint(errore)
            logging.error(f"{self.image} not found!")
            return 0
